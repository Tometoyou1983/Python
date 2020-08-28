# python 3
# demo of multi threading in python
import os, threading, time
os.system('cls')

print('Start of the program')

def takeANAP():
    time.sleep(5)
    print('Wake Up!')

threadObj = threading.Thread(target=takeANAP)
threadObj.start()


threadObj = threading.Thread(target=print, args=['cats', 'Dogs', 'Frogs'], kwargs={'sep': ' & '})
threadObj.start()

print('End of program')
