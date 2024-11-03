from concurrent.futures import ProcessPoolExecutor
import time

def printNumber(num):
    print(f" number is: {num}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



with ProcessPoolExecutor(max_workers = 3) as executor:
    res = executor.map(printNumber, numbers)
    time.sleep(5)  # simulate IO bound task, delay for 5 seconds

for result in res:
    print(result)