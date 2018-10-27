import threading
class x(threading.Thread):
    def run(self):
        for p in range(1,21):
            print(p)
x1=x()
x1.start()
x2=x()
x2.start()
