import os.path
import logging

path_to_data_file = os.path.dirname(os.path.dirname(__file__)) + '/email_list.txt'
number_of_entries = 1000000
logging.basicConfig(level=logging.INFO)