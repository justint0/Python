def test_class_objects():

  class ComplexNumber:
    real = 0
    imaginary = 0 

    def get_real(self): 
      return self.real
    
    def get_imaginary(self):
      return self.imaginary
  
  assert ComplexNumber.real == 0 

  # Class instantiation
  complex_number = ComplexNumber()
  complex_number.real = 10
  assert complex_number.get_real() == 10 

  # __init__ is a special method known as the constructor.
  class ComplexNumberWithConstructor:
    def __init__(self, real_part, imaginary_part):
      self.real = real_part
      self.imaginary = imaginary_part
    
    def get_real(self):
      return self.real
    
    def get_imaginary(self):
      return self.imaginary
  
  complex_number = ComplexNumberWithConstructor(3.0, -4.5)
  assert complex_number.real, complex_number.imaginary == (3.0, -4.5)

test_class_objects()
