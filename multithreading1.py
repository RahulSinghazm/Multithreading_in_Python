import threading
class a(threading.Thread):
    def run(self):
        for p in range(1,101):
            print(p)
class b(threading.Thread):
    def run(self):
        for q in range(101,201):
            print(q)
x1=a()
x1.start()
y1=b()
y1.start()
                                
