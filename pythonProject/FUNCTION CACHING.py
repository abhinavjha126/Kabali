import time
from functools import lru_cache
@lru_cache(maxsize=4)
def some_work(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    print(some_work(3))
    print(some_work(2))
    print(some_work(5))
    print(some_work(9))
    print("In Progress......")
    print(some_work(9))
    print(some_work(5))
    print(some_work(2))
    print(some_work(3))
    # print(some_work(9))
    # print(some_work(9))
    print("Done")