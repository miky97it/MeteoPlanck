import time
import serial

# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB4',
    baudrate=1200,
)

ser.isOpen()

while 1 :
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        print ">>" + out