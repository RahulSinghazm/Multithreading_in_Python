import threading
class x (threading.Thread):
    def run(self):
        for i in range(1,10):
            print(i)
class y(threading.Thread):
    def run(self):
        for j in range(21,31):
            print(j)
x1=x()
x1.start()
y1=y()
y1.start()
