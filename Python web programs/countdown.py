# python 3
# countdown.py A simple countdown script
# this program counts down from 60
# plays a alarm sound once its reaches 0

import time, subprocess, os
os.system('cls')
timeLeft = 10
while timeLeft > 0:
    print(timeLeft, end=' ', flush=True),
    time.sleep(1)
    timeLeft = timeLeft - 1

print('\nBreak time is over!')
subprocess.Popen(['start', 'alarm.wav'], shell=True)