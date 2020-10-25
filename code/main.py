from data import Data
from approaches.multithread import MultiThread
from approaches.multiprocess import MultiProcess
import time
from utils.utils import timing_decorator
import argparse
import re

from config import *


# This is not a complete check for every possible valid email address
# but catches most of the normal ones
def email_is_valid(address):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", address)


def send_email(address):
    address = address.decode('utf-8')
    # if not email_is_valid(address):
    #     logging.info('invalid email address')
    #     return
    time.sleep(wait_time)


@timing_decorator
def main(args):
    data = Data()

    if args.approach == 'multithread':
        multithread = MultiThread(send_email, args.workers)
        for item in data.iterate_items():
            multithread.add_work(item)
        multithread.collect_results()

    if args.approach == 'multiprocess':
        multiprocess = MultiProcess(send_email)
        for item in data.iterate_with_sentinel(args.workers):
            multiprocess.add_work(item)
        multiprocess.collect_results()

    if args.approach == 'not-parallel':
        for item in data.iterate_items():
            send_email(item)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run program to send emails from a list')
    parser.add_argument('--approach', '-a', type=str, required=False, default='multiprocess',
                        help='Choose which approach to use to parallelize email sending')
    parser.add_argument('--workers', '-w', type=int, required=False, default=10,
                        help='Choose how many workers to run in parallel')
    main(parser.parse_args())
