#!/usr/bin/python

import sys
import time
import serial
from enum import Enum
import array


# debug print function that prints byte array
def asciiPrintBytes(ba):
    for b in ba:
        print b
    print ''

def asciiPrintString(s):
    for c in s:
        print ord(c)


def setupSerialComms():
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    # flush serial input buffer
    while ser.inWaiting() > 0:
        ser.read(1)


    ser.close()



def basicSerial():
    # configure the serial connections (the parameters differs on the device you are connecting to)
    ser = serial.Serial(
        port='/dev/ttyAMA0',
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )


    # why is this needed? are we not closing properly?
    if ser.isOpen():
        ser.close()


    ser.open()

    # dump = ''
    #
    # while ser.inWaiting() > 0:
    #     dump += ser.read(1)


    ba = bytearray.fromhex(u'48 49 6c 6F 0a')


    # 255 31 0 0 1 246

    ser.write(ba)

    ser.write("Hello String")

    out = ''

    time.sleep(0.02)
    while ser.inWaiting() > 0:
        out += ser.read(1)



    print "output was:"
    print out

    print ""

    for b in out:
        # print b
        print ord(b)

    ser.close()



def basicPrint():
    print 'hello world'


if __name__ == '__main__':
    basicSerial()

    # setupSerialComms()

    # basicPrint()

