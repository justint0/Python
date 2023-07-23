# A generator is a function that returns an iterator that produces a sequence of values when iterated over.

import random

def lottery():

  # Returns first 3 random numbers between 1 and 10
  for _ in range(3):
    yield random.randint(1, 10)
  
  # Returns a 4th number between 10 and 20
  yield random.randint(10, 20)


def test_generators():
  for number_index, random_number in enumerate(lottery()):
    if number_index < 3:
      assert 0 <= random_number <= 10
    else:
      assert 10 <= random_number <= 20

test_generators()