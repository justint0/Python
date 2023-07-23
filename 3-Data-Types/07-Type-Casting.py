# Casting specifies a type onto a variable. 

def test_type_casting_to_integer():
  assert int(1) == 1
  assert int(2.8) == 2
  assert int('3') == 3
  
def test_type_casting_to_float():
  assert float(1) == 1.0
  assert float(2.8) == 2.8
  assert float("3") == 3.0
  assert float("4.2") == 4.2

def test_type_casting_to_string():
  assert str("s1") == 's1'
  assert str(2) == '2'
  assert str(3.0) == '3.0'

test_type_casting_to_integer()
test_type_casting_to_float()
test_type_casting_to_string()