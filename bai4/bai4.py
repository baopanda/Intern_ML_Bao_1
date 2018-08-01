from threading import Thread
import time

tong = 0
start = time.time()

class myThread(Thread):
    def __init__(self, name,range1,range2):
        super(myThread, self).__init__()
        self.name= name
        self.range1= range1
        self.range2= range2

    def run(self):
        global tong
        print ("san sang chay" + self.name)
        for i in range(int(self.range1),int(self.range2)):
            tong += i
        print ("ket thuc vong lap", self.name)

try:
    while True:
        n = int(input("Nhap so n:"))
        if(n<0):
            print("So n phai lon hon 0")
            print("Moi ban nhap lai so!")
            continue
        else:
            break

    thread1 = myThread("thread 1",1,n/2+1)
    thread2 = myThread("thread 2",n/2+1,n+1)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(tong)

    print('Entire job took:', time.time() - start)

except:
    print ("Error")