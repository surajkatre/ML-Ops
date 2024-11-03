# when to use multithreading 
# I/O bound tasks   
# concrunnct execution  
import threading
import time 
def printNum():
    for i in range(5):
        time.sleep(2)  # simulate I/O bound task, delay for 0.1 second
        print(f"number: {i} ")
def printLetter():
    for i in 'abcde':
        time.sleep(2)  # simulate I/O bound task, delay for 0.1 second
        print(f"letter: {i} ")



# start = time.time()
# printLetter()
# printNum()
# print(time.time() - start)

# print(a)

t1 = threading.Thread(target=printLetter)
t2 = threading.Thread(target=printNum)
new = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
endtime = time.time()-  new
print(endtime)