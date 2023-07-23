# A dictionary is a collection which is unordered, changeable and indexed.
# Dictionaries are created with curly braces and have key-value pairs.

def test_dictionary():

  fruits_dictionary = {
    'cherry': 'red',
    'apple': 'green',
    'banana': 'yellow',
  }
  assert isinstance(fruits_dictionary, dict)

  # Access elements by key
  assert fruits_dictionary['apple'] == 'green'

  # Check if a key is in the dictionary
  assert 'apple' in fruits_dictionary
  assert 'pineapple' not in fruits_dictionary

  # Change a key's value.
  fruits_dictionary['apple'] = 'red' 

  # Add key-value pair
  fruits_dictionary['pineapple'] = 'yellow'
  assert fruits_dictionary['pineapple'] == 'yellow'

  # list(d) returns a list of the keys in insertion order. 
  # sorted(d) returns a sorted list of the keys
  assert list(fruits_dictionary) == ['cherry', 'apple', 'banana', 'pineapple']
  assert sorted(fruits_dictionary) == ['apple', 'banana', 'cherry', 'pineapple']

  # Delete a key-value pair
  del fruits_dictionary['pineapple']
  assert list(fruits_dictionary) == ['cherry', 'apple', 'banana']

  # dict() builds dictionaries
  dictionary_via_constructor = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
  assert dictionary_via_constructor['sape'] == 4139

  dictionary_for_string_keys = dict(sape=4139, guido=4127, jack=4098)
  assert dictionary_for_string_keys['sape'] == 4139

  # Dictionary comprehensions
  dictionary_via_expression = {x: x**2 for x in (2, 4, 6)}
  assert dictionary_via_expression[2] == 4

test_dictionary()