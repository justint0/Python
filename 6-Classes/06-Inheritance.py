# Inheritance allows us to create a new class from an existing class.
# The new class is known as the subclass and the existing class is known as the superclass.

class Person:
  def __init__(self, name):
    self.name = name
  
  def get_name(self):
    return self.name

# Derived classes may override methods of their base classes. 
class Employee(Person):
  def __init__(self, name, staff_id):
    Person.__init__(self, name)
    # super().__init__(name)
    self.staff_id = staff_id
  
  def get_full_id(self):
    return self.get_name() + ', ' + self.staff_id


def test_inheritance():

  person = Person('Bill') 
  employee = Employee('John', 'A23')

  assert person.get_name() == 'Bill'
  assert employee.get_name() == 'John'
  assert employee.get_full_id() == 'John, A23'

  # isinstance() and issubclass()
  assert isinstance(person, Person)
  assert isinstance(employee, Person)

  assert issubclass(Employee, Person)
  assert not issubclass(Person, Employee)

test_inheritance()



