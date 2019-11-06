import time
import threading

def job():
    print(threading.current_thread().getName(),"Started")
    start = time.time()
    k = 0
    for i in range(1000):
        for j in range(1000):
            k = i + j
    end = time.time()
    total = end - start
    print(threading.current_thread().getName(), "Completed")

print(threading.current_thread().getName())

for i in range(5):
    t = threading.Thread(target=job, name='t{}'.format(i))
    t.start()