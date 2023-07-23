def test_arithmetic_operators():

  # Addition
  assert 5 + 3 == 8

  # Subtraction
  assert 5 - 3 == 2

  # Multiplication
  assert 5 * 3 == 15
  assert isinstance(5 * 3, int)

  # Division (returns float)
  assert 8 / 4 == 2
  assert isinstance(8 / 4, float)

  # Modulus
  assert 5 % 3 == 2

  # Exponentiation (returns int)
  assert 5 ** 3 == 125
  assert isinstance(5 ** 3, int)

  # Floor division (returns int)
  assert 5 // 3 == 1
  assert isinstance(5 // 3, int)

test_arithmetic_operators()