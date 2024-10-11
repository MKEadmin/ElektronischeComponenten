## Micro SD Card Adapter

<img src="Micro SD Card Adapter_Photo.jpg" alt="Photo of the component">

<img src="Micro SD Card Adapter_QR_code.jpg" alt="QR code to this page" width="80" height="80">


## Description
The **Micro SD Card Adapter Module** for the **Raspberry Pi Pico** is a small and simple interface that allows you to connect a micro SD card to the Pico, providing a way to expand its storage capacity. This module is useful for projects that require storing large amounts of data, such as logging sensor readings, saving files, or running programs that need additional storage beyond the internal flash memory of the Pico.

### Key Features:
1. **Micro SD Card Slot**:
   - The module has a micro SD card slot that supports standard micro SD and micro SDHC cards.
   - It can accommodate cards with a wide range of capacities, typically from 2GB to 32GB or higher, depending on the format.

2. **SPI Communication**:
   - The SD card module communicates with the Raspberry Pi Pico via the **SPI (Serial Peripheral Interface)** protocol, using the Pico's GPIO pins.
   - The SPI interface is fast and efficient, making it ideal for reading from and writing to the SD card.

3. **Pinout**:
   - The module typically comes with six pins, which need to be connected to the corresponding SPI pins on the Pico:
     - **VCC**: Power supply (typically 3.3V or 5V).
     - **GND**: Ground.
     - **MISO**: Master In Slave Out, used for data output from the SD card to the Pico.
     - **MOSI**: Master Out Slave In, used for sending data from the Pico to the SD card.
     - **SCK**: Serial Clock, controls the timing of data transmission.
     - **CS**: Chip Select, used to select the SD card for communication.

4. **File System Support**:
   - The module allows the Raspberry Pi Pico to interact with the SD card using standard file systems such as **FAT16** or **FAT32**. This makes it compatible with most modern SD cards and allows easy reading and writing of files from other devices (like computers).

5. **Low Power Consumption**:
   - The module is designed to consume low power, making it suitable for battery-powered or energy-efficient projects where power conservation is important.

### Advantages:
1. **Expanded Storage**: It provides significant additional storage, allowing for much larger data handling than the onboard flash memory of the Raspberry Pi Pico.
2. **Simple SPI Interface**: The use of the SPI protocol makes interfacing straightforward, with plenty of libraries and examples available for the Raspberry Pi Pico to read and write data to an SD card.
3. **File Management**: You can store a variety of files, such as **sensor logs**, **configuration files**, **images**, or even **audio files**, and easily transfer them between your Pico and other devices.
4. **Widely Supported**: The SD card adapter is compatible with popular microcontroller platforms like **Arduino** and **Raspberry Pi**, with many resources available for implementation.

### Applications:
- **Data Logging**: Ideal for projects where you need to store large amounts of sensor data or real-time information over an extended period.
- **Audio/Video Storage**: Useful for projects that require saving or accessing media files, such as audio recorders or video playback systems.
- **File-Based Programs**: Enables running file-based applications that require large external storage, such as those that save and retrieve data frequently.

### Example Usage:
- **Wiring**: Connect the VCC, GND, MISO, MOSI, SCK, and CS pins of the module to the appropriate pins on the Raspberry Pi Pico. For instance:
  - **VCC** to 3.3V.
  - **GND** to Ground.
  - **MISO** to GPIO16.
  - **MOSI** to GPIO19.
  - **SCK** to GPIO18.
  - **CS** to GPIO17.
  
- **Libraries**: You can use the **MicroPython** or **C/C++ SDK** to access the SD card. Popular libraries such as **FatFs** (a file system library) allow you to work with files and directories, much like you would on a computer.

### Limitations:
- **Speed**: While SPI is generally fast, the speed of reading and writing to the SD card may be slower compared to more advanced interfaces like SDIO, which is used in some other microcontroller systems.
- **Card Size Limitations**: The module typically supports micro SD cards formatted in **FAT16/FAT32**, which may limit the card size (usually up to 32GB, depending on the specific implementation).

In summary, the **Micro SD Card Adapter Module** for the Raspberry Pi Pico provides an easy and efficient way to add external storage to your projects. It’s especially useful for data logging, file storage, and media-related applications, allowing you to easily transfer data between your Pico and other devices via a standard micro SD card.

## specs


## Order
<a href="https://nl.aliexpress.com/item/1005005981296699.html">https://nl.aliexpress.com/item/1005005981296699.html</a>
<img src="Micro SD Card Adapte_Order.jpg" alt="Photo of the Order">

## Wiring to Raspberry Pi Pico

<img src="Micro SD Card Adapter_Wiring.jpg" alt="Wiring" >

## Installation libraries
Copy next files to the Raspberry Pi Pico

```bash
sdcard.py
```

## Example code
```python
import machine
import uos
import sdcard

cs_pin = machine.Pin(17, machine.Pin.OUT)
spi = machine.SPI(0, baudrate=1000000, polarity=0, phase=0,bits=8, firstbit=machine.SPI.MSB,
                  sck=machine.Pin(18), mosi=machine.Pin(19), miso=machine.Pin(16))

sd = sdcard.SDCard(spi, cs_pin)

vfs = uos.VfsFat(sd)
uos.mount(vfs, "/sd")
fn = "/sd/sdtest.txt"

with open(fn, "w") as f:
    print("Writing data to file sdtest.txt...")
    f.write("This is a test for micro SD card\r\n")
    print("Writing to file completed")
    
with open(fn, "r") as f:
    print("Reading data from file sdtest.txt...")
    data = f.read()
    print("Data read completed")
    print("Data:",data)
```





