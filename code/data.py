import os.path
import random
import string
import itertools

from config import *

class Data:
    def __init__(self):
        if not os.path.isfile(path_to_data_file):
            self.build_data_file()
        self.data_file = open(path_to_data_file, 'rb')
    '''
    returns an email address with a valid format. 
    However, the domains are invalid domains so the addresses don't actually exist
    '''
    def make_valid_email(self):
        domains = ['gmail.net', 'aol.net', 'yahoo.care', 'hotmail.org', 'outlook.de']

        domain = random.choice(domains)

        recipient_length = random.randint(1, 64)
        allowed_chars = string.ascii_lowercase + string.digits + '_.-'

        recipient = ''.join(random.choice(allowed_chars) for _ in range(recipient_length))

        return recipient + "@" + domain

    '''
    returns an invalid email address
    '''
    def make_invalid_email(self):
        email_length = random.randint(1, 64)
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(email_length))

    def build_data_file(self):
        with open(path_to_data_file, 'w') as data_file:
            for i in range(number_of_entries):
                data_file.write(self.make_valid_email() + '\n')

    def iterate_items(self):
        for line in self.data_file:
            yield line

    def iterate_with_sentinel(self, workers):
        iters = itertools.chain(self.data_file, (None,) * workers)
        for line in iters:
            yield line
