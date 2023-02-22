import time


def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('time is %s' % (end - start))
    return wrapper
