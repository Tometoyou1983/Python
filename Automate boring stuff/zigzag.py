import time, sys
print("Lets try a ZigZag program")
print("Am gonna keep zig zagging until you press CTRL + Z")
indent = 0
indentIncreasing = True
try:
    while True:
        print (' ' * indent, end='')
        print ('**********')
        time.sleep(0.1) # pause for 0.1 sec

        if indentIncreasing:
            indent =  indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent -  1
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    print("Exiting the program now. Hope you had fun")
    sys.exit()

