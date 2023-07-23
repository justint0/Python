# The re module provides regular expression tools for advanced string processing. 

import re 

def test_re():

  assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
    'foot',
    'fell',
    'fastest'
  ]

  # Use string methods if possible
  assert 'tea for too'.replace('too', 'two') == 'tea for two'

test_re()
