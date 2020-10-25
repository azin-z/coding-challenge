import functools
import time
import psutil
import os
import re


from config import *


def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        output = func(*args, **kwargs)
        arguments = vars(*args)
        approach = str(arguments['workers']) + ' workers'
        logging.info("{} took {} second(s)".format(approach, round(time.time() - start_time)))
        process = psutil.Process(os.getpid())
        logging.info("program took {} MB memory".format(str(int(int(process.memory_info().rss)/1000000))))  # in bytes
        return output
    return wrapper


# This is not a complete check for every possible valid email address
# but catches most of the normal ones
def email_is_valid(address):
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", address)
