class MyCounter:
  counter = 10

  def get_counter(self):
    return self.counter
  
  def increment_counter(self):
    self.counter += 1
    return self.counter


def test_method_objects(): 
  # A method is a function on an object. 
  counter = MyCounter()
  assert counter.get_counter() == 10

  get_counter = counter.get_counter
  assert get_counter() == 10 

test_method_objects()