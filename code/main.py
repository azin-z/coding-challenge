from data import Data
from approaches.multithread import MultiThread
from approaches.multiprocess import MultiProcess
import time
from utils.utils import timing_decorator
import argparse

from config import *

def send_email(item):
    time.sleep(1)
    logging.debug(item)


@timing_decorator
def main(args):
    data = Data()
    if args.approach == 'not-parallel':
        for item in data.iterate_items():
            send_email(item)

    if args.approach == 'multithread':
        multithread = MultiThread(send_email, args.workers)
        for item in data.iterate_items():
            multithread.add_work(item)
        multithread.collect_results()

    if args.approach == 'multiprocess':
        multiprocess = MultiProcess(send_email, args.workers)
        for item in data.iterate_parallel(args.workers):
            multiprocess.add_work(item)
        multiprocess.collect_results()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run program to send emails from a list')
    parser.add_argument('--approach', '-a', type=str, required=False, default='multithread',
                        help='Choose which approach to use to parallelize email sending')
    parser.add_argument('--workers', '-w', type=int, required=False, default=10,
                        help='Choose how many threads to use when runnning in multithread')
    main(parser.parse_args())
