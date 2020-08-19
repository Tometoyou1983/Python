# python 3
import os, pyinputplus as pyip, random, time
os.system("cls")

numberofQ = 10
correctAnswers = 0

for questionNumber in range(numberofQ):
    num1 = random.randint(0,10)
    num2 = random.randint(0,10)
    prompt = '#%s: %s X %s = ' %(questionNumber+1, num1, num2)
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
        blockRegexes=[('.*', 'Incorrect!')],
        timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of Time!')
    except pyip.RetryLimitException:
        print('Out of Tries!')
    else:
        print('Correct!')
        correctAnswers += 1

time.sleep(1)
print('Score: %s / %s' % (correctAnswers, numberofQ))