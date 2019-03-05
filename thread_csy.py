import threading
import time

def countdown(n,t):
    while n>0:
        print('n =',n,'t = ',t)
        n -= 1
        time.sleep(t)


thd = threading.Thread(target=countdown,args=(5,1))

thd.start()
print(thd.ident)

# thd2 = threading.Thread(target=thd)
print(thd.is_alive())
