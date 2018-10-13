import threading
import time
class x(threading.Thread):
    def run(self):
        time.sleep(10)
        for i in range(1,101):
            print(i)
class y(threading.Thread):
    def run(self):
        for j in range(101,201):
            print(j)
x1=x()
x1.start()
y1=y()
y1.start()
