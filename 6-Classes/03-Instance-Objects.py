def test_instance_objects():
  # Classes have data and methods. Data does not have to be declared in the class definition. 

  class DummyClass:
    pass

  dummy_instance = DummyClass()

  dummy_instance.temporary_attribute = 1
  assert dummy_instance.temporary_attribute == 1
  del dummy_instance.temporary_attribute

test_instance_objects()