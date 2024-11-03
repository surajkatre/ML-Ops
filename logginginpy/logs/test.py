from loggers import logging
def add(a,b):
    logging.debug('adding the numbers')
    return a + b

logging.debug('adding the numbers right  o')
add(10,19)