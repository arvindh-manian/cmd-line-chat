import time
import sys


def type(text):
    for char in text:
        print(char, end='')
        time.sleep(0.1)
        sys.stdout.flush()
    print('')
