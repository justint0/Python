# A namespace is a collection of names (built-in namespace, global namespace, local namespace). 
# A scope is the portion of a program where a namespace can be accessed directly. 

test_variable = 'initial global value'

def test_function_scopes():

  test_variable = 'initial value inside test function'

  def do_local():
    # Create variable that is only accessible inside do_local
    test_variable = 'local value'
    return test_variable
  
  def do_nonlocal():
    # Address the variable from outer scope and try to change it.
    nonlocal test_variable
    test_variable = 'nonlocal value'
    return test_variable
  
  def do_global():
    # Address the variable from global scope and try to change it.
    global test_variable
    test_variable = 'global value'
    return test_variable

  assert test_variable == 'initial value inside test function'

  # Doesn't change global variable or nonlocal variable
  do_local()
  assert test_variable == 'initial value inside test function'

  # Doesn't change global variable but it does change nonlocal variable
  do_nonlocal()
  assert test_variable == 'nonlocal value'

  # Changes global variable but doesn't change nonlocal variable
  assert test_variable == 'nonlocal value'

test_function_scopes()


# Accessing global and non local scope is considered bad practice. 
def test_global_variable_access():

  global test_variable
  assert test_variable == 'global value'

test_global_variable_access()