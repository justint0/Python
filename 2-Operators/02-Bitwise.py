# Binary numbers: https://www.youtube.com/watch?v=g8ACeN9QMdY
# Bitwise operators: https://www.youtube.com/watch?v=igIjGxF2J-w

def test_bitwise_operators():

  # AND operator
  # 5 = 0b0101
  # 3 = 0b0011
  # 1 = 0b0001
  assert 5 & 3 == 1  

  # OR operator
  # 5 = 0b0101
  # 3 = 0b0011
  # 7 = 0b0111
  assert 5 | 3 == 7 

  # NOT operator inverts all the bits
  # 5 = 0000 0101
  #     1111 1010
  # -128 + 64 + 32 + 16 + 8 + 2 = -6
  assert ~5 == -6

  # XOR (exclusive or) operator
  # 5 = 0b0101
  # 3 = 0b0011
  # 6 = 0b0110      
  assert 5 ^ 3 == 6 

  # Signed right shift pushes copies of the leftmost bit in from the left
  # 5 = 0b0101
  assert 5 >> 1 == 2  # 0b0010

  # Zero fill left shift pushes zeros in from the right
  # 5 = 0b0101
  assert 5 << 1 == 10  # 0b1010

test_bitwise_operators()




