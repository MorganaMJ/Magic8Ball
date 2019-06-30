import random
import time


ANSWERS = [
    'It is certain',
    'It is decidedly so',
    'Without a doubt',
    'Yes - definitely',
    'You may rely on it',
    'As I see it, yes',
    'Most likely',
    'Outlook good',
    'Yes',
    'Signs point to yes',
    'Reply hazy, try again',
    'Ask again later',
    'Better not tell you now',
    'Cannot predict now',
    'Concentrate and ask again',
    'Don\'t count on it',
    'My reply is no',
    'My sources say no',
    'Outlook not so good',
    'Very doubtful'
]


def wait():
    print('thinking')
    time.sleep(3)


def magic_ball():
    input('Ask your question.')
    index = random.randint(0, 19)
    wait()
    print(ANSWERS[index])

    qu2 = input('Do you want to ask another question?')
    qu2 = qu2.strip().lower()
    if qu2 == 'yes':
        magic_ball()
    elif qu2 == 'no':
        qu3 = input('Do you want to end the game?')
        qu3 = qu3.strip().lower()
        if qu3 == 'yes':
            exit()
        elif qu3 == 'no':
            magic_ball()
        else:
            print('Answer must be yes or no.')
    else:
        print('Answer must be yes or no.')



