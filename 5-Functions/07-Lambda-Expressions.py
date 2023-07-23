# A lambda function is a special type of function without the function name. 

def test_lambda_expressions():

  def make_increment_function(delta):
    return lambda number: number + delta
  
  increment_function = make_increment_function(42)
  assert increment_function(1) == 43

  # Another use of lambda is to pass a function as an argument.
  pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
  pairs.sort(key=lambda pair: pair[1])

  # The words are ordered alphabetically
  assert pairs == [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

test_lambda_expressions()