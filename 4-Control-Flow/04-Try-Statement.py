# The try statement is used in exception handling.

# The try block lets you test a block of code for errors.
# The except block lets you handle the error. 
# The else block executes if no errors were raised. 
# The finally block always executes.

def test_try():

  exception_has_been_caught = False

  try: 
    print(not_existing_variable)
  except NameError:
    exception_has_been_caught = True

  assert exception_has_been_caught


  # Else block 
  message = ''
  try:
    message += 'Success.'
  except NameError:
    message += 'Something went wrong.'
  else:
    message += 'Nothing went wrong.'
  
  assert message == 'Success.Nothing went wrong.'

  # Finally block
  message = ''
  try:
    print(not_existing_variable)
  except NameError:
    message += 'Something went wrong.'
  finally:
    message += 'The "try except" is finished.'
  
  assert message == 'Something went wrong.The "try except" is finished.'

test_try()