def test_continue_statement():

  even_numbers = [] 
  rest_of_the_numbers = []

  for number in range(0, 10):
    if number % 2 == 0:
      even_numbers.append(number)
      # Stop current loop iteration and go to the next one.
      continue
    
    rest_of_the_numbers.append(number)

  assert even_numbers == [0, 2, 4, 6, 8]
  assert rest_of_the_numbers == [1, 3, 5, 7, 9]

test_continue_statement()