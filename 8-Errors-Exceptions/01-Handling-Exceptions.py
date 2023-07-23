def test_handle_exceptions():

  exception_has_been_handled = False
  try:
    result = 10 * (1 / 0)  # division by zero
    assert result
  except ZeroDivisionError:
    exception_has_been_handled = True

  assert exception_has_been_handled


  # Undefined variable 
  exception_has_been_handled = False
  try:
    result = 4 + spam * 3  # spam is not defined
    assert result
  except NameError:
    exception_has_been_handled = True
  
  assert exception_has_been_handled


  # Multiple exceptions listed
  exception_has_been_handled = False
  try:
    result = 10 * (1 / 0)  # division by zero
    assert result
  except (ZeroDivisionError, NameError):
    exception_has_been_handled = True
  
  assert exception_has_been_handled


  # Multiple except statements
  exception_has_been_handled = False
  try:
    result = 10 * (1 / 0)
    assert result
  except NameError:
    exception_has_been_handled = True
  except ZeroDivisionError:
    exception_has_been_handled = True
  
  assert exception_has_been_handled


  # Else clause is executed if no exceptions are raised
  exception_has_been_handled = False
  no_exceptions_has_been_fired = False

  try:
    result = 10
    assert result
  except NameError:
    exception_has_been_handled = True
  else:
    no_exceptions_has_been_fired = True
  
  assert not exception_has_been_handled
  assert no_exceptions_has_been_fired

test_handle_exceptions()
