import os
import random
import time

from questions import questions as qs

def loading():
    for i in range(3):
        out = "." * (i + 1)
        print(out, end="\r")
        time.sleep(1)

def pickRandomNum(min, max):
    diff = max - min
    return (random.random() * max) % diff + min

def askQuestion(q, a):
    answer = input(str(q) + "\n\n")
    print("")
    loading()
    if answer == a:
        print("You are correct")
        return 1;
    else:
        print("You are wrong! The answer was \n" + str(a))
        return 0;

def loop():
    correct = 1
    streak = 0
    while(correct == 1):
        os.system('clear')
        question = qs[int(pickRandomNum(0, len(qs)))]
        correct = askQuestion(question["q"], question["a"])
        if correct == 1:
            streak += 1
            time.sleep(1.5)
        if correct == 0:
            print("\nYour streak was " + str(streak))
            quit = input("\nIf you want to quit enter y, otherwise enter n:\n\n")
            if quit == "y":
                break
            if quit == "n":
                os.system('clear')
                print("Continuing...")
                time.sleep(1.5)
                correct = 1

loop()
