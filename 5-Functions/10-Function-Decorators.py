# A decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function. See more: https://www.programiz.com/python-programming/decorator

import time

def tictoc(func):
  def wrapper():
    t1 = time.time()
    func()
    t2 = time.time() - t1
    print(f'{func.__name__} ran in {t2} seconds')
  return wrapper

# Pass do_this into tictoc
@tictoc
def do_this():
  # Simulating running code..
  time.sleep(1.3)

@tictoc
def do_that():
  # Simulating running code..
  time.sleep(.4)

do_this()
do_that()
print('Done')