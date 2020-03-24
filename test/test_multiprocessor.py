import multiprocessing
import timeit
import time

start = time.time()

def count(name):
    for i in range(1, 400):
        print(name, ' : ', i)


num_list = ['p1', 'p2', 'p3', 'p4']


if __name__ == '__main__':
    # 멀티 쓰레딩 pool 사용
    pool = multiprocessing.Pool(processes=8) # 현재 시스템에서 사용할 프로세스 개수
    pool.map(count, num_list)
    pool.close()
    pool.join()
