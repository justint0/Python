# def function_name(arguments)
def fibonacci_function_example(number_limit):
  """Generate a Fibonacci series up to number_limit."""

  fibonacci_list = []
  previous_number, current_number = 0, 1

  while previous_number < number_limit:
    fibonacci_list.append(previous_number)
    previous_number, current_number = current_number, previous_number + current_number

  # The return statement returns a value from a function.
  return fibonacci_list


def test_function_definition():

  assert fibonacci_function_example(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

  # Functions can be assigned to variables. 
  fibonacci_function_clone = fibonacci_function_example
  assert fibonacci_function_clone(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

  # Functions can be defined inside other functions, functions can be passed as arguments to other functions, and functions can return other functions. 

  # Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed. See more: https://www.programiz.com/python-programming/closure

  def greet():
    # Variable defined outside the inner function
    name = "John"

    # Return a nested anonymous function 
    return lambda: "Hi " + name
  
  # Call the outer function
  message = greet()

  # Call the inner function
  print(message())

test_function_definition()