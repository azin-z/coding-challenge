from multiprocessing import Process, Manager, cpu_count
from config import *

# The multiprocess approach avoids the Global Interpreter Lock problem.
# It would be easiest to start a process pool and map the input file to it and the pool would take care of the rest.
# However, this would have a high memory cost since the pool loads the entire file into memory
# To avoid this, we manually iterate through the file and supply the queue with work.
# At the end, we also need to add a None item in the queue for each one of the processes.
# To achieve this we use the itertools.chain function and use a None value as an exit signal in the work function

class MultiProcess:
    def __init__(self, work_function):
        self.num_of_workers = cpu_count
        self.manager = Manager()
        self.results = self.manager.list()
        self.work = self.manager.Queue(self.num_of_workers)
        self.process_item = work_function
        self.work_count = 0
        self.done_count = 0
        self.pool = []
        self.start_workers()

    def do_work(self, in_queue, out_list):
        while True:
            item = in_queue.get()
            if item is None:
                return
            self.process_item(item)
            self.done_count += 1
            if self.done_count % 10000 == 0:
                logging.info("{} done".format(self.done_count))
            out_list.append(item)

    def start_workers(self):
        self.pool = [Process(target=self.do_work, args=(self.work, self.results)) for _ in range(self.num_of_workers)]
        for p in self.pool:
            p.start()

    def add_work(self, item):
        self.work.put(item)
        self.work_count += 1

    def collect_results(self):
        for p in self.pool:
            p.join()

