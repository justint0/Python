import math
import random
import statistics 

def test_math():
  assert math.cos(math.pi / 4) == 0.70710678118654757
  assert math.log(1024, 2) == 10.0


def test_random(): 

  # Select random option
  random_options = ['apple', 'pear', 'banana']
  random_choice = random.choice(random_options) 
  assert random_choice in random_options

  # Sampling without replacement
  random_sample = random.sample(range(100), 10)
  for sample in random_sample:
    assert 0 <= sample <= 100
  
  # Choose random float between 0 and 1
  random_float = random.random()
  assert 0 <= random_float <= 1

  # Choose random integer between 0 and 6
  random_integer = random.randrange(6)
  assert 0 <= random_integer <= 6


def test_statistics():

  data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

  assert statistics.mean(data) == 1.6071428571428572
  assert statistics.median(data) == 1.25
  assert statistics.variance(data) == 1.3720238095238095

test_math()
test_random()
test_statistics()
