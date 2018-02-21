import time
import serial
from bson.son import SON
# configure the serial connections (the parameters differs on the device you are connecting to)
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=1200,
)
ser.isOpen()

offset=0; #since last checked char
endString="FINE PROGR.40 "
buffer=''
debug=True

def storer(message):
    print "saving"
    insert()
# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
def insert():
    db.test.insert_many([
    {"item": "journal",
     "qty": 25,
     "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
     "status": "A"},
    {"item": "notebook",
     "qty": 50,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "A"},
    {"item": "paper",
     "qty": 100,
     "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
     "status": "A"}])
    
while 1 :
    out = ''
    while ser.inWaiting() > 0:
        out += ser.read(1)

    if out != '':
        buffer+=out
        if debug:
            print ">>" + out
        ##for in range(0, len(buffer)-offset):
        if endString in buffer:
            storer(buffer)
            if debug:
                print "->" + out
            buffer=''


"""
example of message
    PROG. N.40 ORE 15 :54 :14 DEL 8 /2 /18 
    SAT. N. 1 
    SONDA N. 1.01: 8.3 GC 
    SONDA N. 2.01: 34 UR% 
    SONDA N. 2.02: 1004 HPA 
    SONDA N. 2.03: 82.3 W/M2 
    SONDA N. 2.04: 0 GN 
    SONDA N. 3.01: 0 M/SEC 
    SONDA N. 3.02: 0 MMH2O 
    SONDA N. 1.05: 2.8 GC 
    SONDA N. 1.09: 8.9 GC 
    SONDA N. 2.05: 10 UR% 
    SONDA N. 2.09: 64 UR% 
    SONDA N. 2.06: 997 HPA 
    SONDA N. 2.10: 1004 HPA 
    FINE PROGR.40 
"""

            
    

                