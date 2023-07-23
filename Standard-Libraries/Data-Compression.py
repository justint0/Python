import zlib

def test_zlib():

  string = b'witch which has which witches wrist watch'
  assert len(string) == 41 

  zlib_compressed_string = zlib.compress(string)
  assert len(zlib_compressed_string) == 37

  zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
  assert zlib_decompressed_string == b'witch which has which witches wrist watch'

  assert zlib.crc32(string) == 226805979

test_zlib()