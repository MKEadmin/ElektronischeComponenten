from machine import Pin, I2C
import time

# MAX30102 I2C address and registers
MAX30102_I2C_ADDR = 0x57
REG_MODE_CONFIG = 0x09
REG_FIFO_CONFIG = 0x08
REG_SPO2_CONFIG = 0x0A
REG_LED1_PA = 0x0C  # Red LED Pulse Amplitude
REG_LED2_PA = 0x0D  # IR LED Pulse Amplitude
REG_FIFO_DATA = 0x07  # FIFO data register

class MAX30102:
    def __init__(self, i2c):
        self.i2c = i2c
        self.address = MAX30102_I2C_ADDR
        self.setup_sensor()
    
    def write_register(self, register, value):
        """Writes a byte to a specified register."""
        self.i2c.writeto_mem(self.address, register, bytes([value]))
    
    def read_register(self, register, num_bytes):
        """Reads num_bytes from a specified register."""
        return self.i2c.readfrom_mem(self.address, register, num_bytes)

    def setup_sensor(self):
        """Initializes the MAX30102 sensor with default settings."""
        # Reset the sensor
        self.write_register(REG_MODE_CONFIG, 0x40)  # Reset
        time.sleep(0.1)  # Give some time for reset

        # Configure FIFO (no averaging, FIFO rolls over on full, almost full at 32 samples)
        self.write_register(REG_FIFO_CONFIG, 0x0F)

        # Configure SpO2 sensor (ADC range 4096nA, sample rate 100Hz, pulse width 411µs)
        self.write_register(REG_SPO2_CONFIG, 0x27)

        # Reduce LED current to prevent saturation
        self.write_register(REG_LED1_PA, 0x24)  # Set Red LED current to a moderate level
        self.write_register(REG_LED2_PA, 0x24)  # Set IR LED current to a moderate level

        # Enable SpO2 mode (Red and IR LEDs enabled)
        self.write_register(REG_MODE_CONFIG, 0x03)
    
    def read_fifo(self):
        """Reads data from the FIFO buffer and returns Red and IR readings."""
        data = self.read_register(REG_FIFO_DATA, 6)  # Read 6 bytes (3 bytes Red, 3 bytes IR)
        
        # Extract Red and IR values (left-justified 18-bit values)
        red_val = (data[0] << 16) | (data[1] << 8) | data[2]
        ir_val = (data[3] << 16) | (data[4] << 8) | data[5]
        
        # Mask to get valid 18-bit values
        red_val &= 0x03FFFF
        ir_val &= 0x03FFFF

        return red_val, ir_val

# Simple moving average to smooth the data
def moving_average(data, window_size):
    """Applies a simple moving average to smooth the IR signal."""
    if len(data) < window_size:
        return data  # Not enough data to smooth yet
    return [sum(data[i:i+window_size]) // window_size for i in range(len(data) - window_size)]

# Peak detection function to calculate BPM
def detect_peaks(data, threshold=10000):
    """Detects peaks in the PPG signal based on a threshold."""
    peaks = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > threshold:
            peaks.append(i)
    return peaks

# Calculate heart rate from peaks
def calculate_bpm(peaks, sample_rate=100):
    """Calculates BPM based on detected peaks and sample rate."""
    if len(peaks) < 2:
        return 0  # Not enough peaks detected to calculate BPM
    # Calculate time intervals between successive peaks
    intervals = [peaks[i] - peaks[i-1] for i in range(1, len(peaks))]
    # Average the intervals and convert to BPM
    avg_interval = sum(intervals) / len(intervals)
    bpm = (sample_rate / avg_interval) * 60
    return bpm

# Initialize I2C (SDA=Pin 0, SCL=Pin 1) - adjust pins for your board
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# Create sensor object
sensor = MAX30102(i2c)

# Buffer to store the IR data
buffer_size = 100  # Adjust as needed
ir_buffer = []

x = 0
# Main loop to read sensor data and detect heart rate
while True:
    red, ir = sensor.read_fifo()
    ir_buffer.append(ir)
    
    # Keep the buffer size constant
    if len(ir_buffer) > buffer_size:
        ir_buffer.pop(0)
    
    # Apply moving average to smooth the signal
    smoothed_ir = moving_average(ir_buffer, window_size=5)
    
    # Detect peaks in the smoothed IR data
    peaks = detect_peaks(smoothed_ir)
    
    # Calculate BPM based on detected peaks
    bpm = calculate_bpm(peaks)
    
    print(f"{x}| IR: {ir}, BPM: {bpm}")
    x += 1
    time.sleep(0.1)  # Delay between readings
