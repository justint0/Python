def test_integer_numbers():

  positive_integer = 1
  negative_integer = -3255522
  big_integer = 35656222554887711

  assert isinstance(positive_integer, int)
  assert isinstance(negative_integer, int)
  assert isinstance(big_integer, int)


def test_booleans():
  """
  The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1.
  """

  true_boolean = True
  false_boolean = False

  assert true_boolean
  assert not false_boolean

  assert isinstance(true_boolean, bool)
  assert isinstance(false_boolean, bool)

  assert str(true_boolean) == "True"
  assert str(false_boolean) == "False"


def test_float_numbers():

  float_number = 7.0

  # float() 
  float_number_via_function = float(7)
  float_negative = -35.59

  assert float_number == float_number_via_function
  assert isinstance(float_number, float)
  assert isinstance(float_number_via_function, float)
  assert isinstance(float_negative, float)

  # Float can also be scientific numbers with an "e" to indicate the power of 10.
  float_with_small_e = 35e3
  assert float_with_small_e == 35000


def test_complex_numbers():

  complex_number_1 = 5 + 6j
  complex_number_2 = 3 - 2j

  assert isinstance(complex_number_1, complex)
  assert isinstance(complex_number_2, complex)

test_integer_numbers()
test_booleans()
test_float_numbers()
test_complex_numbers()