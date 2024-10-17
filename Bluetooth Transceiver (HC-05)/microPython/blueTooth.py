from machine import UART
from utime import sleep

uart = UART(0, 9600)


def listenBasic():
    while True:
        sleep(0.1)
        if uart.any():
            command = uart.readline()
            print(command)


# CMD{}
# TXT{}
# VOL{23.4}
# COL{(123,43,76)}
# POS{(x,y):char}
DATA_START = b"{"
DATA_END = b"}"


def init(brightness):
    write('VOL', f'{brightness}')


def write(cmd, data):
    line = f'{cmd}{{{data}}}'
    print("Writing data to phone : ", line)
    uart.write(line)


def anyMessageReceiving():
    if uart.any():
        return uart.readline()
    return None


def listenOnce(whileAction=None):
    print("--> Listen to message")
    readAction = True
    readData = False
    action = ""
    data = ""
    while True:
        if whileAction is not None:
            whileAction()

        if uart.any():
            command = uart.readline()
            # print("line : ", command)
            # print(command)   # uncomment this line to see the recieved data
            if command == DATA_START:
                readData = True
                readAction = False
                data = ""
            elif command == DATA_END:
                readData = False
                readAction = True
                return action, data
            elif readAction:
                action += command.decode("utf-8")
            elif readData:
                data += command.decode("utf-8")


# whileAction is a function withoud parameters
# that is colled in the while loop
def listen(commandDataHandler, whileAction=None):
    if commandDataHandler is None:
        return
    print("Start listening to blueTooth messages")

    while True:
        cmd, data = listenOnce(whileAction)
        commandDataHandler(cmd, data)


if __name__ == "__main__":
    uart.write('AT')
    listenBasic()
