def test_function_unpacking_arguments():

  # Unpack a list
  arguments_list = [3, 6]
  assert list(range(*arguments_list)) == [3, 4, 5]

  # Unpack a dictionary
  def myFish(guppies, zebras):
    print(f'I have {guppies} guppy fish.')
    print(f'I have {zebras} zebra fish.')

  fish = {
    'guppies': 2,
    'zebras' : 5,
  }

  myFish(**fish)

test_function_unpacking_arguments()
