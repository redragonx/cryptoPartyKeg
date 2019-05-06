import serial
import threading
from timeit import default_timer as timer

SERIAL_PORT="/dev/ttyACM0"
global beginTimer

global paymentTotalSecs
SatoshiAmtPerSec = 2840
beginTimer = False
global elapsed_time
global startTime

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

def msg_parse(msg):
    msg = msg_decode(msg)
    return msg

def timerCheck():
    global beginTimer

    if (beginTimer):
        endTime = timer()
        elapsed_time = endTime - firstTime
        print(elapsed_time)

## Gets the serial data
def read_keg_data(sp):
    global beginTimer

    while(True):
        raw_data = sp.readline()
        msg = msg_parse(raw_data)

        # Arduino sends numbers when the button is pushed
        # btn:idle when not pushed
        if msg == "-1":
            firstTime = timer()
            beginTimer = True
        else:
            global paymentTotalSecs

            paymentTotalSecs = paymentTotalSecs + int(msg)
            beginTimer = False

        # print(msg)

def main():
    if __name__ == '__main__':
        print("Trying to access: {}".format(SERIAL_PORT))
        sp = start_serial()
        if (sp is None):
            print("Exiting!")

        print("We opened {}".format(sp.name))

        print("Starting a new thread for the serial...")
        serial_thread = threading.Thread(target=read_keg_data, args=(sp, ))
        serial_thread.start()

        print("Starting a new thread for the timer...")
        timer_thread = threading.Thread(target=timerCheck, args=())
        timer_thread.start()

main()
