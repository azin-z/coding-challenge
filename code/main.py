from data import Data
from approaches.multithread import MultiThread
import time
from utils.utils import timing_decorator
import argparse


def send_email(item):
    time.sleep(1)
    print('sent email to', item)


@timing_decorator
def main(args):
    data = Data()
    if args.approach == 'not-parallel':
        for item in data.iterate_items():
            send_email(item)

    if args.approach == 'multithread':
        multithread = MultiThread(send_email)
        for item in data.iterate_items():
            multithread.add_work(item)
        multithread.collect_results()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run program to send emails from a list')
    parser.add_argument('--approach', '-a', type=str, required=False, default='multithread',
                        help='Choose which approach to use to parallelize email sending')
    main(parser.parse_args())
