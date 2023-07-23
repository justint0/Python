def fibonacci_at_position(position):
  """Return fibonacci number at specified position"""
  current_position = 0
  previous_number, current_number = 0, 1

  while current_position < position:
    current_position += 1
    previous_number, current_number = current_number, previous_number + current_number

  return previous_number


def fibonacci_smaller_than(limit):
  """Return Fibonacci series up to limit"""
  result = [] 
  previous_number, current_number = 0, 1

  while previous_number < limit:
    result.append(previous_number)
    previous_number, current_number = current_number, previous_number + current_number

  return result


# Run in terminal: python3 fibonacci_module.py <arguments>
if __name__ == '__main__':
  import sys
  print(fibonacci_at_position(int(sys.argv[1])))