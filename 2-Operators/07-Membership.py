def test_membership_operators():

  fruit_list = ["apple", "banana"]

  # in returns True if a sequence is present in the object
  assert "banana" in fruit_list

  # not in returns True if a sequence is not present in the object
  assert "pineapple" not in fruit_list

test_membership_operators()