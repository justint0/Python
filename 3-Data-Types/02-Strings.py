import pytest

def test_string_type():

  # Strings created with different kind of quotes are treated the same.
  name_1 = "John"
  name_2 = 'John'
  assert name_1 == name_2

  # Use \' to escape the single quote or use double quotes instead.
  single_quote_string = 'doesn\'t'
  double_quote_string = "doesn't"
  assert single_quote_string == double_quote_string

  # Using print(), \n creates a new line.
  print('First line.\nSecond line.')

  # Strings can be indexed. 
  word = 'Python'
  assert word[0] == 'P' # First character
  assert word[-1] == 'n' # Last character

  # Strings can also be sliced. 
  assert word[0:2] == 'Py'
  assert word[2:5] == 'tho' 

  # Attempting to use an index that is too large will result in an error. 
  with pytest.raises(Exception):
    not_existing_character = word[42]
    assert not not_existing_character
  
  # However, out of range slices are handled gracefully. 
  assert word[42:] == ''

  # Python strings are immutable. 
  with pytest.raises(Exception):
    word[0] = 'J'

  # len() returns the length of a string:
  characters = 'supercalifragilisticexpialidocious'
  assert len(characters) == 34

  # String literals can span multiple lines when enclosed in triple quotes. End of lines are automatically included in the string, but it's possible to prevent this by adding a \ at the end of the line. 
  multi_line_string = '''\
      First line
      Second line
  '''

def test_string_operators():

    # Concatenation and repetition
    assert 3 * 'un' + 'ium' == 'unununium'

    # This feature is particularly useful when you want to break long strings:
    text = (
      'Put several strings within parentheses '
      'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # If you want to concatenate variables or a variable and a literal, use +:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'
  

def test_string_methods():

    hello_world_string = "Hello, World!"

    # The strip() method removes whitespace.
    string_with_whitespaces = " Hello, World! "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('t') == 4

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('welcome') == 7

    # Converts the first character of each word to upper case
    assert 'Welcome to my world'.title() == 'Welcome To My World'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('John', 'Peter', 'Vicky')
    assert ', '.join(my_tuple) == 'John, Peter, Vicky'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()

    # Returns True if all characters in the string are decimals.
    assert '1234'.isdecimal()


def test_string_formatting():

  # To use formatted string literals (f-strings), begin a string with f or F before the opening quotation mark. Inside this string, you can write a Python expression using {}. 
  year = 2018
  event = 'conference'
  assert f'Results of the {year} {event}' == 'Results of the 2018 conference'

  # The str.format() method requires more manual effort.  
  yes_votes = 42_572_654  # equivalent to 42572654
  no_votes = 43_132_495   # equivalent to 43132495
  percentage = yes_votes / (yes_votes + no_votes)
  assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

  # repr() or str() convert any value to a string. 
  greeting = 'Hello, world.'
  assert str(greeting) == 'Hello, world.'
  assert repr(greeting) == "'Hello, world.'"

  # Formatted string literal with format specifier. 
  pi_value = 3.14159
  assert f'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

  # Passing an int after ':' will cause that field to be int number of characters wide.
  table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
  table_string = ''
  for name, phone in table_data.items():
    table_string += f'{name:7}==>{phone:7d}'

  assert table_string == ('Sjoerd ==>   4127'
                          'Jack   ==>   4098'
                          'Dcab   ==>   7678')
  
  # More on formatting with str.format() 
  assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

  # Numbers or keywords can be used in the format fields
  assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'

  formatted_string = 'This {food} is {adjective}.'.format(
    food='spam',
    adjective='absolutely horrible'
  )
  assert formatted_string == 'This spam is absolutely horrible.' 

  formatted_string = 'The story of {0}, {1}, and {other}.'.format(
    'Bill',
    'Manfred',
    other='Georg'
  )
  assert formatted_string == 'The story of Bill, Manfred, and Georg.'

  # Variables are referenced by name instead of position. 
  table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
  formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)
  assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

  # ** unpacks the dictionary
  formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)
  assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'

test_string_type()
test_string_operators()
test_string_methods()
test_string_formatting()
