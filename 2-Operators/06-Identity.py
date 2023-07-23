def test_identity_operators():

  first_fruits_list = ["apple", "banana"]
  second_fruits_list = ["apple", "banana"]
  third_fruits_list = first_fruits_list

  # is returns True if both variables are the same object
  assert first_fruits_list is third_fruits_list

  # is not returns True if both variables are not the same object.
  assert first_fruits_list is not second_fruits_list

test_identity_operators()