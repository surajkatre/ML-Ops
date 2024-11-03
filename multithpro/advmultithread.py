# multithreading with thread pool executor 


from concurrent.futures import ThreadPoolExecutor
import time

def printNUmber(number):
    print(f" the no is : {number}")

number= [1,2,3,4,5,6,7,8,9,10,11,12,13]

with ThreadPoolExecutor(max_workers=3) as executor:
    res= executor.map(printNUmber, number)
    time.sleep(5)  # simulate IO bound task, delay for 5 seconds
for result in res:
    print(result) # prin