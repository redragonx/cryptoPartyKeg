import serial
import threading
import os
import subprocess
import json
import qrcode

SERIAL_PORT="/dev/ttyACM0"
mSatsPerMS = 2840

def start_serial():
    try:
            serialport = serial.Serial(
                        port=SERIAL_PORT,
                        baudrate = 57600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS
            )
            serialport.flushInput()
            serialport.flushOutput()
            return serialport
    except(serial.SerialException):
        print("Could not open {}".format(SERIAL_PORT))

def msg_decode(msg):
    msg = msg[:-2]
    msg = msg.decode('utf-8')
    return msg

   

def main():
    if __name__ == '__main__':
        print("Trying to access: {}".format(SERIAL_PORT))
        sp = start_serial()
        if (sp is None):
            print("Exiting!")

        print("We opened {}".format(sp.name))
        while(True):
            millis = int(msg_decode(sp.readline()))
            tab = mSatsPerMS * millis
            inv = subprocess.Popen(['sudo', 'sh','bitcoin-lightning-cli.sh', 'invoice', str(tab), '{}ms of beer pouring'.format(millis), 'rate 2840 sat/sec'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            stdout,stderr = inv.communicate()
            invDict = json.loads(stdout)
            print("invoice for {} milliseconds of beer pouring at the rate of {} millisatoshis per second".format(millis,mSatsPerMS))
            print(invDict)
            qr = qrcode.QRCode()
            qr.add_data(invDict['bolt11'])
            qr.print_ascii()
        
main()
