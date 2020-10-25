import os.path
import logging
number_of_entries = 1000000

path_to_data_file = os.path.dirname(os.path.dirname(__file__)) + '/email_list_' + str(number_of_entries) + ' .txt'
logging.basicConfig(level=logging.INFO)

wait_time = 0.5
