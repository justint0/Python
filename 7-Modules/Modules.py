# A module is a file that contains code to perform a specific task. 

# Three conventions for importing modules
import fibonacci_module
# from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than
# from fibonacci_module import *


def test_modules():
  
  assert fibonacci_module.fibonacci_at_position(7) == 13
  assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

  assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]

test_modules()