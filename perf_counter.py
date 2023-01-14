import time

#[here] check performances..., use the %time thing
def perf_count_decorator(func):
    '''[demo] function performance timer wrapper'''

    def inner(*args, **kwargs):
        '''decorator inner functions (can access outer functions)'''
        start = time.perf_counter() # [bp] time the start with performance counter
        func(*args, **kwargs)
        diff = time.perf_counter()-start
        print (f'task {func.__name__} ran for {diff} secs')
    return inner    # this is the wrapper call