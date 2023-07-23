# Logical operators are used to combine conditional statements.

def test_logical_operators():
  first_number = 5
  second_number = 10

  # and returns True if both statements are true
  assert first_number > 0 and second_number < 20

  # or returns True if one of the statements is true
  assert first_number > 5 or second_number < 20

  # not returns True if the result is false
  assert not first_number == second_number

test_logical_operators()