def test_break_statement():

  number_to_be_found = 42
  number_of_iterations = 0

  for number in range(100):
    if number == number_to_be_found:
      # Break here and don't continue the loop. 
      break
    else:
      number_of_iterations += 1
  
  assert number_of_iterations == 42

test_break_statement()