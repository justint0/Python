# Functions can be called with an arbitrary number of arguments. 

def test_function_arbitrary_arguments():

  # *args is a tuple
  def concat(*args, sep='/'):
    return sep.join(args)
  
  assert concat('earth', 'mars', 'venus') == 'earth/mars/venus'
  assert concat('earth', 'mars', 'venus', sep=' ') == 'earth mars venus'

test_function_arbitrary_arguments()