"""Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers,
involve significant computational work. Multiprocessing
can be used to distribute the workload across multiple
CPU cores, improving performance"""

import multiprocessing
import time
import math 
import sys
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n* factorial(n-1)
# process = multiprocessing.Process(target = factorial)
# process.start()
# process.join()

# print(f"Factorial of 5 is {factorial(5)}")


# process = [ ]
# for 
sys.set_int_max_str_digits(100000)


# fuction  creation to compute facorial of a given nuber 



def compute_facorial(num):
    print(f" factorial of a number {num}")
    res = math.factorial(num)
    print(f"The factorial of {num} is {res}")
if __name__ == "__main__":
    numbers = [1000, 10000, 20000, 50000]
    start = time.time()

    # create a pool of worker processor  
    with multiprocessing.Pool() as pool:
        rsults  = pool.map(compute_facorial, numbers)
        end = time.time()
        print( rsults)
        print(f"Time taken : {end - start}")
         