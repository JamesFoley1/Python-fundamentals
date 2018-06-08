import random

def randInt(min=0, max=100):
    print(round(random.random()*(max-min) + min))
randInt(min=50,max=500)
