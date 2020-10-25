import threading
import queue

from config import *

# Multithreading is sometimes not a good solution in python because of
# the Global Interpreter Lock in CPython.
# But this is only when the task is CPU bound.
# It does not affect this example, because in each thread we're merely calling a sleep function
# which releases the GIL and lets other threads execute.
# Since the email sending code will also be an IO bound work,
# the concurrency that a multithreaded code allows greatly speeds things up
# it won't let the CPU sit idle and runs other threads as one is waiting for the API call


class MultiThread:
    def __init__(self, work_function, num_of_workers=10):
        self.work = queue.Queue()
        self.results = queue.Queue()
        self.num_of_workers = num_of_workers
        self.process_item = work_function
        self.start_workers()
        self.work_count = 0

    def do_work(self, in_queue, out_queue):
        while True:
            item = in_queue.get()
            self.process_item(item)
            result = item
            out_queue.put(result)
            in_queue.task_done()

    def start_workers(self):
        for i in range(self.num_of_workers):
            t = threading.Thread(target=self.do_work, args=(self.work, self.results))
            t.daemon = True
            t.start()

    def add_work(self, work):
        self.work.put(work)
        self.work_count += 1

    def collect_results(self):
        self.work.join()
        for i in range(self.work_count):
            logging.debug(self.results.get())
