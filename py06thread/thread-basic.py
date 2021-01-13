import threading

def runThread1(x, y):
    # _ 언터바는 반복에 i를 안쓰겠다.
    for _ in range(x): #range를 안쓰면 0~x-1번까지 반복, 1
        print('1번', y)

def runThread2(x, y):
    for i in range(x+y):
        print('2번', i)

def runThread3(x, y):
    sum = 0
    for i in range(x, y+1):
        sum = sum + i
        print('3번', sum)


threading1 = threading.Thread(target=runThread1, args=(100,'hong'))
threading2 = threading.Thread(target=runThread2, args=(1,100))
threading3 = threading.Thread(target=runThread3, args=(1,100))

threading1.start()
threading2.start()
threading3.start()