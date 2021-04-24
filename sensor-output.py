import time
PREVIOUS_LINE="\x1b[1F"
RED_BACK="\x1b[41;37m"
GREEN_BACK="\x1b[42;30m"
YELLOW_BACK="\x1b[43;30m"
RESET="\x1b[0m"
import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()
adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)
GAIN = 1
adc.start_adc(1, gain=GAIN)
import os
import sys
import datetime
from datetime import date
import calendar
tooday = date.today()
sys.stdout = open("/home/pi/Documents/Week1/Day: " + calendar.day_name[tooday.weekday()] + " " + str(tooday), "a")
print('Reading ADS1x15 channel 1 for 5 seconds...')
print("Date & Time: " + str(datetime.datetime.now()))
start = time.time()
while (time.time() - start) <= 10.0:
    value = adc.get_last_result()
    if value <  800:
       print ('too_much_water {0}'.format(value))
    elif value < 1000:
       print ('ok {0}'.format(value))
    elif  value > 1350:
       print ('Completly_dry! {0}'.format(value))
    elif  value > 1200:
        print ('needs_water {0}'.format(value))
    else:
        print('bone_dry: {0}'.format(value))
    time.sleep(.5)
sys.stdout = sys.stdout
adc.stop_adc()
