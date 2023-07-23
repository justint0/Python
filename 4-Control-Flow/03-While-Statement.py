# The while loop executes as long as the condition is true.

def test_while_statement():
  number = 2
  power = 5
  result = 1

  while power > 0:
    result *= number
    power -= 1
    
  # 2^5 = 32
  assert result == 32

test_while_statement()