import time
import os

def bounce(text):
    while True:
        for i in range(len(text)):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" " * i + text[i] + "\n" + text[:i] + " " + text[i+1:])
            time.sleep(0.2)
        for i in range(len(text)-1, -1, -1):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(text[:i] + " " + text[i+1:] + "\n" + " " * i + text[i])
            time.sleep(0.2)

bounce("hello world")
