# A class is a blueprint for creating objects.

def test_class_definition():

  class GreetingClass:
    name = 'user'

    # The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
    def say_hello(self):
      return 'Hello ' + self.name
    
    def say_goodbye(self):
      return 'Goodbye ' + self.name
  
  # Class instantiation
  greeter = GreetingClass() 
  assert greeter.say_hello() == 'Hello user'
  assert greeter.say_goodbye() == 'Goodbye user'

test_class_definition()