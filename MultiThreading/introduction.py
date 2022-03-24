from threading import *

from time import *

class Hello(Thread): #<-- (parameter to create multiThreads)
    def run(self):
        for i in range(5):
            print("Hello", ctime(time()))
            sleep(1)
            
            


class Hi(Thread): 
    def run(self):
        for i in range(5):
            print("Hi",ctime(time()))
            sleep(1)

t1 = Hello()
t2 = Hi()
t1.start() #functions to call def run(), it's allowed to pass tasks 
sleep(0.3)
t2.start()
t1.join() 
t2.join() #prohibited/prevents you from exceeding, until you finish all your tasks  
print("finished")