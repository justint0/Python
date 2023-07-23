# See Package.png for the structure of a package
# Every top-level package and subpackage has a __init__.py file 

# Importing packages conventions
# import sound_package.effects.echo 
# from sound_package.effects import echo
from sound_package.effects.echo import echo_function

def test_packages():
  assert echo_function() == 'Do echo effect'

test_packages()