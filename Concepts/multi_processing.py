import multiprocessing
import time


def worker():
    """worker function"""
    print("worker ")
    return


if __name__ == '__main__':
    start_time = time.time()
    jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()
    print(f"Finshed, run time is: {time.time() - start_time}")
