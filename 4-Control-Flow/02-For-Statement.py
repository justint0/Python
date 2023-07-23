# Python's for statement iterates over the items of any sequence. 

def test_for_statement():

  # Measure word length
  words = ['cat', 'window', 'defenestrate']
  words_length = 0

  for word in words:
    words_length += len(word)

  assert words_length == (3 + 6 + 12)

  # If you need to modify the sequence you are iterating over while inside the loop, make a copy.
  for word in words[:]: 
    if len(word) > 6:
      words.insert(0, word)
  
  assert words == ['defenestrate', 'cat', 'window', 'defenestrate']

  # range() generates arithmetic progressions
  iterated_numbers = []

  for number in range(5):
    iterated_numbers.append(number) 

  assert iterated_numbers == [0, 1, 2, 3, 4]

  # To iterate over the indices of a sequence, combine range() and len()
  words = ['Mary', 'had', 'a', 'little', 'lamb']
  concatenated_string = ''

  for word_index in range(len(words)):
    concatenated_string += words[word_index] + ' '

  assert concatenated_string == 'Mary had a little lamb '

  # Or use enumerate().
  concatenated_string = ''

  for word_index, word in enumerate(words):
    concatenated_string += word + ' '
  
  assert concatenated_string == 'Mary had a little lamb '

  # When looping dictionaries, use items() to access key-value pairs. 
  knights_names = []
  knights_properties = []

  knights = {'gallahad': 'the pure', 'robin': 'the brave'}
  for key, value in knights.items():
    knights_names.append(key)
    knights_properties.append(value) 

  assert knights_names == ['gallahad', 'robin']
  assert knights_properties == ['the pure', 'the brave']

  # To loop two or more sequences, use the zip() function
  questions = ['name', 'quest', 'favorite color']
  answers = ['lancelot', 'the holy grail', 'blue']
  combinations = [] 

  for question, answer in zip(questions, answers):
    combinations.append('What is your {0}? It is {1}.'.format(question, answer))
  
  assert combinations == [
      'What is your name? It is lancelot.',
      'What is your quest? It is the holy grail.',
      'What is your favorite color? It is blue.',
  ]

test_for_statement()


def test_range_function():

  assert list(range(5)) == [0, 1, 2, 3, 4]
  assert list(range(0, 10, 3)) == [0, 3, 6, 9]

test_range_function()