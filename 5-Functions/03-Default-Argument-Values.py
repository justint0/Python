def power_of(number, power=2):
  return number ** power


def test_default_function_arguments():
  assert power_of(3) == 9
  assert power_of(3, 3) == 27

test_default_function_arguments()