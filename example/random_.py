from random import random
from time import sleep
from scrapic import Scrapic

a = 10

scrapic = Scrapic()
for i in range(100):
    sleep(1)
    a += 1
    print(scrapic.closure('test', lambda: random() + a, 10))
