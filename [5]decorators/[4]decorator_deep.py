from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        time_start = time()
        response = fn(*args, **kwargs)
        time_end = time()
        print(f'took {time_end - time_start} | ⏳s.')
        return response
    return wrapper

get = []

@performance
def range_test():
    for idx in range(10000):
        idx * 4


range_test()