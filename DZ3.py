import random
import keyboard
import random 
import time
from threading import Thread
a=[]
for i in range(200):
    a.append(i)
def potreb():
    while True:
        if (len(a)>=80) and (len(a)<=100):
            a.append(random.randint(1,100))
            print(a)
        if keyboard.is_pressed('q'):
            return

def pokyp():
    while True:
        if len(a)>=0:
            del(a[-1])
            print(a)

potreb1=Thread(target=potreb)
potreb2=Thread(target=potreb)
potreb1.start()
potreb2.start()

pokyp1=Thread(target=pokyp)
pokyp1.start()
pokyp2=Thread(target=pokyp)
pokyp2.start()
pokyp3=Thread(target=pokyp)
pokyp3.start()
