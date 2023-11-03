# ******************************************
# Python multiprocessing
# ******************************************
# multiprocessing   = Running tasks in parallel on different cpu cores, bypass GIL used for threads
#                   = Better for cpu bound tasks (heavy cpu usage)
#                   = Better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():
    print(cpu_count())

    # a = Process(target=counter, args=(1000000000,))

    # a = Process(target=counter, args=(500000000,))
    # b = Process(target=counter, args=(500000000,))

    a = Process(target=counter, args=(250000000,))
    b = Process(target=counter, args=(250000000,))
    c = Process(target=counter, args=(250000000,))
    d = Process(target=counter, args=(250000000,))

    # a = Process(target=counter, args=(125000000,))  # This will take more time than above 4, because cpu_count is 4
    # b = Process(target=counter, args=(125000000,))  # When run more than 4, it will delay with significant overhead
    # c = Process(target=counter, args=(125000000,))
    # d = Process(target=counter, args=(125000000,))
    # e = Process(target=counter, args=(125000000,))
    # f = Process(target=counter, args=(125000000,))
    # g = Process(target=counter, args=(125000000,))
    # h = Process(target=counter, args=(125000000,))

    a.start()
    b.start()
    c.start()
    d.start()
    # e.start()
    # f.start()
    # g.start()
    # h.start()

    a.join()
    b.join()
    c.join()
    d.join()
    # e.join()
    # f.join()
    # g.join()
    # h.join()

    print("Finished in: ", time.perf_counter(), "seconds")


if __name__ == '__main__':
    main()


