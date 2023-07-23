def test_file_methods():

  multi_line_file = open('multi_line_file.txt', 'r')
  binary_file = open('binary_file', 'r')

  # f.read(size)
  read_data = multi_line_file.read() 
  assert read_data == 'first line\nsecond line\nthird line'

  # f.seek(offset, from_what)
  assert binary_file.seek(0) == 0  # Go to the 0th byte in the file
  assert binary_file.seek(6) == 6  # Go to the 6th byte in the file
  assert binary_file.read(1) == '6'

  # f.readline() reads a single line from the file
  multi_line_file.seek(0)
  assert multi_line_file.readline() == 'first line\n'
  assert multi_line_file.readline() == 'second line\n'
  assert multi_line_file.readline() == 'third line'
  assert multi_line_file.readline() == ''

  multi_line_file.close()
  binary_file.close()

test_file_methods()