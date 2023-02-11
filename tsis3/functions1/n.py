#13     =
from math import *
import random
c=random.randint(1,20)
name=input("Hello! What is your name? ")
def sayhi(name):
    print("Well, ", name, ", I am thinking of a number between 1 and 20.\n ", " Take a guess.")
sayhi(name) 
b=1 
cnt=0
def urnum(b,cnt):
    b=int(input())
    if(b>c):
        print("Your guess is too big.")
        cnt+=1
        urnum(b,cnt)
    elif(b<c):
        print("Your guess is too low.")
        cnt+=1
        urnum(b,cnt)
    else:
        print("Good job, KBTU! You guessed my number in " , cnt, " guesses!")
urnum(b,cnt) 
