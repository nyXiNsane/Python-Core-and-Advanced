import threading
from threading import Thread

def DisplayNumbers():
    i = 0
    print(threading.current_thread().getName())
    while i <= 10:
        print(i)
        i+=1

print(threading.current_thread().getName())
t = Thread(target=DisplayNumbers)
t.start()