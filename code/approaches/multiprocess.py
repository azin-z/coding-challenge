from multiprocessing import Process, Manager
from config import *


class MultiProcess:
    def __init__(self, work_function, num_of_workers=10):
        self.num_of_workers = num_of_workers
        self.manager = Manager()
        self.results = self.manager.list()
        self.work = self.manager.Queue(self.num_of_workers)
        self.process_item = work_function
        self.work_count = 0

        self.pool = []
        self.start_workers()

    def do_work(self, in_queue, out_list):
        while True:
            item = in_queue.get()
            line_no, line = item

            if line == None:
                return
            self.process_item(line)

            result = (line_no, line)

            out_list.append(result)

    def start_workers(self):
        for i in range(self.num_of_workers):
            p = Process(target=self.do_work, args=(self.work, self.results))
            p.start()
            self.pool.append(p)

    def add_work(self, num_and_line):
        self.work.put(num_and_line)
        self.work_count += 1

    def collect_results(self):
        for p in self.pool:
            p.join()

        logging.debug(sorted(self.results))

