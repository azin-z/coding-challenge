# coding-challenge
program to send out emails to recipients from a huge list

## justification for the picked approach
A multithreaded approach is used to send the emails concurrently.
Multithreading is sometimes not a good solution in python because of the Global Interpreter Lock in CPython.
But this is only a problem when the task is CPU bound.
It does not affect this example, because in each thread we're merely calling a sleep function which releases the GIL and lets other threads execute.
Since the email sending code will also be an IO bound work, the concurrency of a multithreaded program greatly speeds things up.
It won't let the CPU sit idle and runs other threads as one thread is waiting for the API call to finish.

## Requirements
This code runs in Python 3.

## How to run
from the code folder, run:
```bash
python main.py
```
Optionally you can provide a -w parameter that chooses how many worker threads to use. By default this number is set to 100.
```bash
python main.py -w 10
```

