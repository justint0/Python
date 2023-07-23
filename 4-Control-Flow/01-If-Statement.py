# If statements execute code if a condition is true.

def test_if_statement():
  
  number = 15
  conclusion = ''

  if number < 0:
    conclusion = 'Number is less than zero'
  elif number == 0:
    conclusion = 'Number equals to zero'
  elif number < 1:
    conclusion = 'Number is greater than zero but less than one'
  else:
    conclusion = 'Number bigger than or equal to one'
  
  assert conclusion == 'Number bigger than or equal to one'

test_if_statement()