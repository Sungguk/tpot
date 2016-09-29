import multiprocessing, time

def task(args):
    count = args[0]
    queue = args[1]
    for i in xrange(count):
        queue.put("%d mississippi" % i)
    return "Done"


def main():
    manager = multiprocessing.Manager()
    q = manager.Queue()
    pool = multiprocessing.Pool()
    result = pool.map_async(task, [(x, q) for x in range(10)])
    time.sleep(1)
    while not q.empty():
        print(q.get())
    print(result.get())

if __name__ == "__main__":
    main()
