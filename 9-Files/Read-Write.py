def test_files_open():
  """
  open(filename, mode) returns a file object

  The mode can be
  'r' for reading (default)
  'w' for writing (existing file with the same name gets erased)
  'a' for appending to the end of a file
  'r+' for reading and writing

  Appending a 'b' to the mode opens the file in binary mode.
  """

  # Open files without 'with' statement
  file = open('multi_line_file.txt', 'r')
  assert not file.closed

  read_data = file.read() 
  assert read_data == (
    'first line\n'
    'second line\n'
    'third line'
  )

  file.close()
  assert file.closed

  # Open file using 'with' 
  with open('multi_line_file.txt', 'r') as file:
    read_data = file.read() 

    assert read_data == (
      'first line\n'
      'second line\n'
      'third line'
    )

  assert file.closed

test_files_open() 
