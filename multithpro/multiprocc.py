# processes runs in  parallel  
# when to use 
# cpu bond task ., heavy task   
# parallel execution  : when want to use multiple cores 


import multiprocessing
import time
def sq_number():
    for i in range(5):
        time.sleep(1)  # simulate cpu bound task, delay for 0.1 second  # 1 second = 1000 millisecond
        print(f"sq : {i*i}" )
def cube_number():
    for i in range(5):
        time.sleep(1.5)  # simulate cpu bound task, delay for 0.1 second
        print(f"cube : {i*i*i}" )
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=sq_number)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()


    # start the process  


    p1.start()
    p2.start()
    # waiting for processs to complete 
    p1.join()
    p2.join()

    final_time = time.time() - t
    print(final_time)