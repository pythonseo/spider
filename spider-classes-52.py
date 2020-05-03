import threading
import time
def targer(second):
    print(f'Threading {threading.current_thread().name} is runing')
    print(f'Threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'Threading {threading.current_thread().name} is ended')
print(f'Threading {threading.current_thread().name} is running')
threads=[]
for i in [1,5]:
    thread = threading.Thread(target=targer,args=[i])
    threads.append(thread)
    thread.start()
print(threads) #show threads
for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')



class MyThread(threading.Thread):
    def __init__(self,second):
        threading.Thread.__init__(self)
        self.second = second
    def run(self):
        print(f'Threading {threading.current_thread().name} is running')
        print(f'Threading {threading.current_thread().name} sleep {self.second}s')
        time.sleep(self.second)
        print(f'Threading {threading.current_thread().name} is ended')
print(f'Threading {threading.current_thread().name} is running')
threads=[]
for i in [1,5]:
    thread = MyThread(i)
    threads.append(thread)
    thread.start()
print(threads) #show threads
for thread in threads:
    thread.join()
print(f'Threading {threading.current_thread().name} is ended')

count=0
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count
        lock.acquire()#上锁
        temp=count +1
        time.sleep(0.01)
        count =temp
        lock.release()#解锁
lock=threading.Lock()
threads=[]
for _ in range(500):
    thread=MyThread()
    thread.start()
    threads.append(thread)
for thread in threads:
    thread.join()
print(f'Final count:{count}')