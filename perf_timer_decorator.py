'''
 [mst] perf_timer_decorator.py
 basics of optimization in python. performance counters and
 decorators (aka wrappers)

 log:
 -2022.01:  -using easy lru_caching as a wrapper for intensive tasks
                by https://youtu.be/DnKxKFXB4NQ
            -perf counter as a wrapper by https://youtu.be/qUeud6DvOWI
            with arguments and different syntaxes


Created on Jan 11, 2021
@author: mst
'''

import time
from functools import lru_cache
from sys import getsizeof

#[here]
def perf_count_decorator(func):
    '''[demo] function performance timer wrapper'''

    def inner(*args, **kwargs):
        '''decorator inner functions (can access outer functions)'''
        start = time.perf_counter() # [bp] time the start with performance counter
        func(*args, **kwargs)
        diff = time.perf_counter()-start
        print (f'task {func.__name__} ran for {diff} secs')
    return inner    # this is the wrapper call



# the naive top-bottom recursive fibonacci calculation is infamously
# inefficient. we can use built in caching to remember (cache)
# calculated values
@lru_cache(maxsize=5)
def fib (n):
    if n <= 1: # fib(0) = 0; fib(1) = 1
        return n
    return fib(n-1) + fib(n-2)


def some_func():
    print ('something')

################## DRIVER
def main():
    print ("[mst] wrappers and decorators doodle")
    fib(20)
    #counted = perf_count_decorator(fib(20))
    #counted()
    #print(f'{ans=}')
'''
    # using fibo as an example
    # stress the naive function...
    #start = time.perf_counter() # [bp] time the start with performance counter
    for i in range (30):
        fibc = fib(i)
        print (f'fib number {i} is: {fibc} sized {getsizeof(fibc)} bytes')
    # time the end of then running code
    #print (f'task ran for {time.perf_counter()-start}')
'''



if __name__ == ("__main__"):
    main()
