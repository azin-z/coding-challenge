from data import Data
import time
from utils.utils import timing_decorator, email_is_valid
import argparse
import threading
import queue

from config import *


class MultiThreadedRun:
    def __init__(self, num_of_workers=10):
        self.data = Data()
        self.work = queue.Queue()
        self.results = queue.Queue()
        self.num_of_workers = num_of_workers
        self.work_count = 0

    def do_work(self):
        while True:
            item = self.work.get().decode('utf-8')
            if not email_is_valid(item):
                logging.info('invalid email address')
                return
            time.sleep(wait_time)  # instead of sending an email
            self.results.put(item)
            self.work.task_done()

    def start_workers(self):
        for i in range(self.num_of_workers):
            t = threading.Thread(target=self.do_work)
            t.daemon = True
            t.start()

    def add_work(self, work):
        self.work.put(work)
        self.work_count += 1

    def collect_results(self):
        self.work.join()
        for i in range(self.work_count):
            logging.debug(self.results.get())

    def run(self):
        self.start_workers()
        for item in self.data.iterate_items():
            self.add_work(item)
        self.collect_results()


@timing_decorator
def main(args):
    multi_threaded_run = MultiThreadedRun(args.workers)
    multi_threaded_run.run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run program to send emails from a list')
    parser.add_argument('--workers', '-w', type=int, required=False, default=100,
                        help='Choose how many workers to run in parallel')
    main(parser.parse_args())
