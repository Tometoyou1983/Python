# python 3
#stopwatch program that tracks time of the tasks
# This program:
#        tracks the amount of time elapsed between presses of enter key
#        each key press will start a new lap
#        prints the lap number, total time and lap time
# Prettified with left and right justify to make more sense.

import os, time
os.system('cls')
print('Press ENTER to begin. Once done, press ENTER to "click" the stopwatch. Press Ctrl-C to quit')
input()
print('started')
startTime = time.time()
lastTime = startTime
lapNum = 1

# start tracking laptimes
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f'Lap #{str(lapNum).ljust(2)}: {str(totalTime).rjust(6)} ({str(lapTime).rjust(4)})', end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print('\nDone')