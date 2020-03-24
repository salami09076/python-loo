import time


def logging_time(original_fn):
    def wrapper_fn(*args, **kwargs):
        start = time.time()
        result = original_fn(*args, **kwargs)
        end = time.time()
        print('WorkingTime[{}]: {} sec'.format(original_fn.__name__, end - start))
        return result
    return wrapper_fn


@logging_time
def count(cnt):
    for i in range(cnt):
        print(i)

if __name__ == '__main__':
    count(500000)