# A set is a collection that is unordered and unindexed.
# Sets are created with curly braces and have comma-separated values. 

def test_sets():

  fruits_set = {"apple", "banana", "cherry"}
  assert isinstance(fruits_set, set)

  # set() constructor
  fruits_set_via_constructor = set(("apple", "banana", "cherry"))
  assert isinstance(fruits_set_via_constructor, set)


def test_set_methods():

  fruits_set = {"apple", "banana", "cherry"}

  # Check if an item is in a set
  assert "apple" in fruits_set
  assert "pineapple" not in fruits_set

  # Use the len() method to return the number of items
  assert len(fruits_set) == 3

  # add() adds an item to the set. 
  fruits_set.add("pineapple")
  assert "pineapple" in fruits_set

  # remove() removes an item from the set. 
  fruits_set.remove("pineapple")
  assert "pineapple" not in fruits_set
  assert len(fruits_set) == 3

  # Sets are unique
  first_char_set = set('abracadabra')
  second_char_set = set('alacazam')
  assert first_char_set == {'a', 'r', 'b', 'c', 'd'} 
  assert second_char_set == {'a', 'l', 'c', 'z', 'm'} 

  # Letters in first word but not in second. 
  assert first_char_set - second_char_set == {'r', 'b', 'd'}

  # Letters in first word or second word or both.
  assert first_char_set | second_char_set == {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

  # Letters in both words
  assert first_char_set & second_char_set == {'a', 'c'}

  # Letters in first or second word but not both.
  assert first_char_set ^ second_char_set == {'r', 'd', 'b', 'm', 'z', 'l'}

  # Set comprehensions
  word = {char for char in 'abracadabra' if char not in 'abc'}
  assert word == {'r', 'd'}

test_sets()
test_set_methods()