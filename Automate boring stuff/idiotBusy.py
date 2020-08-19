import os, time,  pyinputplus as pyip 

os.system("cls")

while True:
    start_time = time.time()
    response = pyip.inputYesNo(prompt= 'Want to know how to keep an idiot busy for hours?: ')
    if response == 'no':
        break
seconds = time.time() - start_time

print('This program kept you busy for %s ' %(time.strftime("%H:%M:%S", time.gmtime(seconds))) + ' Seconds')
print('Have a nice day')
