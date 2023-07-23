# One required argument and three default arguments
def parrot(voltage, state='a stiff', action='voom', parrot_type='Norwegian Blue'):

  message = 'This parrot wouldn\'t ' + action + ' '
  message += 'if you put ' + str(voltage) + ' volts through it. '
  message += 'Lovely plumage, the ' + parrot_type + '. '
  message += 'It\'s ' + state + '!'
  return message


def test_function_keyword_arguments():

  message = (
    "This parrot wouldn't VOOM if you put 1000 volts through it. "
    "Lovely plumage, the Rose-ringed parakeet. "
    "It's a stiff!"
  )

  # Keyword arguments can be supplied in any order, but must come after positional arguments. 
  assert parrot(1000, parrot_type="Rose-ringed parakeet", action="VOOM") == message

# *args is used to pass a non-keyworded, variable-length argument list
# **kwargs is used to pass a keyworded, variable-length argument list.

def test_function(first_param, *args, **kwargs):
  assert first_param == 1
  assert args == (2, 3)
  assert kwargs == {
      'fourth_param': 4,
      'fifth_param': 5
    }

test_function(1, 2, 3, fourth_param=4, fifth_param=5)
