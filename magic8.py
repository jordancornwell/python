import random
import time

list_1 = ['yes','no','maybe so?', 'answer unclear', 'ask another question', '99% chance of success', '99% chance of failure',]

def ballAsk():
    print "Ask the ball your question, mortal:"
    question = raw_input("> ")

    print ('\nThinking..\n')
    time.sleep(3)

    ran = random.choice(list_1)
    print ran
    time.sleep(3)

    ballQuestion()

def ballQuestion():
    print "\nWould you like to ask another question?:\nYes or no, mortal."
    ballAnswer()

def ballAnswer():
    answer = raw_input('> ')
    if answer[0] == 'y' or 'Y':
        print '\n*sigh*\nSo be it!\n'
        ballAsk()
    elif answer[0] == 'n' or 'N':
        print 'Good answer.'
    else:
        print 'I asked you yes or no. Try again'
        ballAnswer()

ballAsk()