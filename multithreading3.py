import threading
class a(threading.Thread):
    def run(self):
        for i in range (1,101):
            print(i)
class b(threading.Thread):
    def run(self):
        for j in range (1,101):
            print(j)
x1=a()
y1=b()
x1.start()  
y1.start()         
