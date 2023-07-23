def test_raise_exception():
  
  try:
    age = int(input('How old are you?: '))
    print(f'You are {age} years old')

    if age < 0 or age > 120:
      raise ValueError
  
  except ValueError:
    print('Age range is invalid.')
  except:
    print('Some other exception occured.')

test_raise_exception()