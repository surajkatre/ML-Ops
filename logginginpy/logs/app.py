import logging

logging.basicConfig( level=logging.DEBUG,

                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler("app1.log"),
                                  logging.StreamHandler()]
,
                        
                        )
logger = logging.getLogger("Arithmatic logger")

def add(a,b):
    result = a+b


    logging.debug(f"Adding {a} + {b} to , {result} ")
    return result

def subtract(a,b):
    result = a-b
    logging.debug(f"Subtracting {b} from {a} to , {result} ")
    return result
def multiply(a,b):
    result = a*b
    logging.debug(f"Multiplying {a} by {b} to , {result} ")
    return result


def divide(a,b):
    result = a/b
    logging.debug(f"Dividing {a} by {b} to , {result} ")
    return result



add(10,10)
subtract(11,10)
multiply(10,10)
divide(10,2)
