import threading
class x(threading.Thread):
    def run(self):
        print(self.getName())
class y(threading.Thread):
    def run(self):
        print(self.getName())
x1=x()
x1.start()
x1.setName('X Thread')
x2=x()
x2.start()
y1=y()
y1.start()
