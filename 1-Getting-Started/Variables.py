# Python is dynamically typed. 
# Every variable in Python is an object.

# Rules for Python variables:
# A variable name must start with a letter or the underscore character.
# A variable name can only contain alpha-numeric characters and underscores.
# Variable names are case-sensitive.

def test_variables():
  
  integer_variable = 5
  string_variable = 'John'

  assert integer_variable == 5
  assert string_variable == 'John'

  variable_with_changed_type = 4
  variable_with_changed_type = 'Sally'

  assert variable_with_changed_type == 'Sally'

test_variables()
