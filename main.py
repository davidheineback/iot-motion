import time
from machine import Pin


#config
motionDetected = 1
noMotionDetected = 0
hold_time_sec = 5
pir = Pin('P13',mode=Pin.IN)

motionSignal = 3

print("Starting Detection")
while True:
    if pir()==motionDetected:
        print("Motion Detected!")
        pybytes.send_signal(motionSignal, "Motion Detected!")

    if pir()==noMotionDetected:
        pass

    time.sleep(hold_time_sec)
