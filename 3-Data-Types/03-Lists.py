# A list is a collection that is ordered, changeable and indexed.
# Lists are created with square brackets and have comma-separated values.

import pytest

def test_list_type():

  squares = [1, 4, 9, 16, 25]
  assert isinstance(squares, list)

  # Lists can be indexed and sliced. Slice operations return a new list. 
  assert squares[0] == 1 
  assert squares[:] == [1, 4, 9, 16, 25]

  # Lists support concatenation. 
  assert squares + [36, 49, 64] == [1, 4, 9, 16, 25, 36, 49, 64]

  # Lists are mutable. 
  cubes = [1, 8, 27, 65, 125]          # The cube of 4 is 64!
  cubes[3] = 64                        # Replace the wrong value
  assert cubes == [1, 8, 27, 64, 125]

  # Assignment to slices can modify the list
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  letters[2:5] = []
  assert letters == ['a', 'b', 'f', 'g']

  # len() returns the size of a list
  letters = ['a', 'b', 'c', 'd']
  assert len(letters) == 4

  # Lists can be nested.
  list_of_chars = ['a', 'b', 'c']
  list_of_numbers = [1, 2, 3]
  mixed_list = [list_of_chars, list_of_numbers]
  assert mixed_list == [['a', 'b', 'c'], [1, 2, 3]]

test_list_type()


def test_list_methods():

  fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
  
  # list.append(x) adds an item x to the end of the list.
  fruits.append('grape')
  assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'grape']

  # list.remove(x) removes the first item whose value is equal to x. 
  fruits.remove('grape')
  assert fruits == ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

  with pytest.raises(Exception):
    fruits.remove('not existing element')

  # list.insert(i, x) inserts an item x at a given position i.
  fruits.insert(0, 'grape')
  assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

  # list.index(x, start, end) returns the index of the first item whose value is equal to x. 
  assert fruits.index('grape') == 0
  assert fruits.index('banana', 5) == 7     # Find 'banana' starting at position 5
  
  # list.count(x) returns the number of times x appears in the list.
  assert fruits.count('tangerine') == 0

  # list.copy() returns a shallow copy of the list.
  fruits_copy = fruits.copy()
  assert fruits_copy == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

  # list.reverse() reverses the elements of the list.
  fruits_copy.reverse()
  assert fruits_copy == ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

  # list.sort(key=None, reverse=False) sorts the list in-place.
  fruits_copy.sort()
  assert fruits_copy == ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

  # list.pop() removes the item at the given position in the list, and returns it. Default is last element.
  assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
  assert fruits.pop() == 'banana'
  assert fruits == ['grape', 'orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

  # list.clear() removes all items from the list. 
  fruits.clear()
  assert fruits == []

test_list_methods()


def test_del_statement():

  numbers = [-1, 1, 66.25, 333, 333, 1234.5]

  del numbers[0]
  assert numbers == [1, 66.25, 333, 333, 1234.5]

  del numbers[2:4]
  assert numbers == [1, 66.25, 1234.5]

  del numbers[:]
  assert numbers == []

  # del can delete variables:
  del numbers
  with pytest.raises(Exception):
    assert numbers == []

test_del_statement()


def test_list_comprehensions():
  """
  A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses.
  """

  squares = []
  for number in range(10):
    squares.append(number ** 2)
  
  assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  # Without side effects
  squares = list(map(lambda x: x ** 2, range(10)))
  assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  squares = [x ** 2 for x in range(10)]
  assert squares == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

  # Another example
  combinations = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
  assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

  combinations = []
  for first_number in [1, 2, 3]:
    for second_number in [3, 1, 4]:
      if first_number != second_number:
        combinations.append((first_number, second_number))
  
  assert combinations == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

  # Another example - flatten a list 
  vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
  flatten_vector = [num for elem in vector for num in elem]
  assert flatten_vector == [1, 2, 3, 4, 5, 6, 7, 8, 9]

test_list_comprehensions()


def test_nested_list_comprehensions():

  matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
  ]

  # Transpose rows and columns:
  transposed_matrix = [[row[i] for row in matrix] for i in range(4)]
  assert transposed_matrix == [
      [1, 5, 9],
      [2, 6, 10],
      [3, 7, 11],
      [4, 8, 12],
  ]

# The * operator can be used in conjunction with zip() to unzip the list.
  assert list(zip(*matrix)) == [
    (1, 5, 9),
    (2, 6, 10),
    (3, 7, 11),
    (4, 8, 12),
  ]

test_nested_list_comprehensions()
