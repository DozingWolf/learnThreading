import threading
import time

def countdown(n,t,started_evt):
    print('countdown starting')
    # started_evt.set()
    while n>0:
        print('n =',n,'t = ',t)
        n -= 1
        time.sleep(t)
print(1)
s_evt = threading.Event()
print(2)
thd = threading.Thread(target=countdown,args=(5,1,s_evt))
print(3)
thd.start()
print(4)
s_evt.wait()
print(5)
print('countdown is running')
