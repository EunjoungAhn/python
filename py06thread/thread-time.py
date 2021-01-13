import time
import threading
def thread_run():
    print('===='+time.ctime(),'====')
    for i in range(0,10):
        print('Thead running - ', i)
        #(3초에 한번씩, 함수를 실행해라)
    threading.Timer(3, thread_run).start()

thread_run()