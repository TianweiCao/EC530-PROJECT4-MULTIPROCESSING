from multiprocessing import Pool, cpu_count
import os
import time


def sample_task(i):
    print('child-process: {} - mission{}'.format(os.getpid(), i))
    time.sleep(4)
    print("result: {}".format(20 ** 20))


if __name__=='__main__':
    print("CPU corn-number:{}".format(cpu_count()))
    print('current main-process: {}'.format(os.getpid()))
    start = time.time()
    p = Pool(4)
    for i in range(4):
        p.apply_async(sample_task, args=(i,))
    print('wait for all child to complete')
    p.close()
    p.join()
    end = time.time()
    print("it takes {} seconds in sum".format((end - start)))