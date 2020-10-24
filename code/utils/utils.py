import functools
import time
import psutil
import os

from config import *


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        arguments = vars(*args)
        approach = arguments['approach'] + ' with ' + str(arguments['workers']) + ' workers'
        logging.info("{} took {} second(s)".format(approach, round(time.time() - start_time)))
        process = psutil.Process(os.getpid())
        logging.info("program took {} MB memory".format(str(int(int(process.memory_info().rss)/1000000))))  # in bytes
        return output
    return wrapper
