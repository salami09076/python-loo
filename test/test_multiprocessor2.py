from multiprocessing import Process
import time
import os

start_time = time.time()


# 멀티 스레드 사용 (40만 카운트)
def count(cnt):
    proc = os.getpid()
    for i in range(cnt):
        print('Process ID : ', proc, ' -- ', i)


if __name__ == '__main__':
    # 멀티 스레딩 process 사용
    num_arr = [100000, 100000, 100000, 100000]
    procs = []

    for index, number in enumerate(num_arr):
        # Process 객체 생성
        proc = Process(target=count, args=(number,))
        procs.append(proc)
        proc.start()

    # 프로세스 종료 대기
    for proc in procs:
        proc.join()

print('--- %s seconds' % (time.time() - start_time))