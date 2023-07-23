# The glob module provides a function for making file lists from directory wildcard searches. 

import glob

def test_glob():

  assert sorted(glob.glob('glob_files/*.txt')) == sorted([
    'glob_files/first_file.txt',
    'glob_files/second_file.txt'
  ])

test_glob()