import threading
import time

def runThread1(x, y):
    for i in range(x+y):
        time.sleep(1)
        print('1번', i)

def runThread2(x, y):
    for i in range(x, y+1):
        time.sleep(0.5)
        print('----2번', i)

threading1 = threading.Thread(target=runThread1, args=(1,100))
threading2 = threading.Thread(target=runThread2, args=(1,100))

threading1.start()
threading2.start()