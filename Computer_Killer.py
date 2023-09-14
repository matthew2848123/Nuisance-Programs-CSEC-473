#Matthew Repecki
#Let it burn
import math
import random
import threading

import psutil


def eater():
    '''
    Creates an infinite loop that does computationally expensive work to kill a computer.
    :return: None
    '''
    i = 10000001
    while True:
        if (i*i) < math.pow(2,63)-1:
            #Then we arent gonna have an integer overflow
            i = math.pow(i,2)
            b = i%random.randint(9999,10000)
            #print(psutil.cpu_stats())
            #print(psutil.virtual_memory())
        else:
            #Reset the counter
            i = 10000001
def create_threads():
    for i in range(10000):
        thread = threading.Thread(target=eater)
        thread.start()

create_threads()