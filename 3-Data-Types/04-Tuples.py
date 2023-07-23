# A tuple is a collection which is ordered and unchangeable.
# Tuples are created with round brackets. 
# Tuples may have mutable elements, such as lists. 

import pytest

def test_tuple():
  fruits_tuple = ("apple", "banana", "cherry")

  assert isinstance(fruits_tuple, tuple)
  assert fruits_tuple[0] == "apple"

  # You cannot change values in a tuple.
  with pytest.raises(Exception):
    fruits_tuple[0] = "pineapple"

  # Tuple() constructor
  fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))
  assert isinstance(fruits_tuple_via_constructor, tuple)

  # len() function
  assert len(fruits_tuple_via_constructor) == 3

  # It is possible to omit brackets when initializing tuples.
  another_tuple= 12345, 54321, 'hello!'
  assert another_tuple == (12345, 54321, 'hello!')

  # Tuples may be nested
  nested_tuple = another_tuple, (1, 2, 3, 4, 5)
  assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

  # Empty tuples are constructed by an empty pair of parentheses
  empty_tuple = ()

  # A tuple with one item is constructed by a value followed by a comma.
  singleton_tuple = 'hello',
  assert singleton_tuple == ('hello',)

  # Tuple packing
  packed_tuple = 12345, 54321, 'hello!'

  # Tuple unpacking
  first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
  assert first_tuple_number == 12345
  assert second_tuple_number == 54321
  assert third_tuple_string == 'hello!'

  # Swap
  first_number = 123
  second_number = 456
  first_number, second_number = second_number, first_number
  assert first_number == 456
  assert second_number == 123

test_tuple()