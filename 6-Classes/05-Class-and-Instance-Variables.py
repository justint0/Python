# Class variables are shared by all instances.
# Instance variables are unique to each instance.
# Mutable objects should never be class variables. 

def test_class_and_instance_variables(): 

  class Dog:
    kind = 'canine'

    def __init__(self, name):
      self.name = name
      self.tricks = []
    
    def add_trick(self, trick):
      self.tricks.append(trick)
  
  fido = Dog('Fido')
  buddy = Dog('Buddy')

  assert fido.kind == 'canine'
  assert buddy.kind == 'canine'

  # Unique to Fido
  assert fido.name == 'Fido'

  # Unique to Buddy
  assert buddy.name == 'Buddy' 
  
test_class_and_instance_variables()
