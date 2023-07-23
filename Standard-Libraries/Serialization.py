# Python provides libraries to encode and decode JSON. 

import json 

def test_json():

  person_dictionary = {'first_name': 'John', 'last_name': 'Smith', 'age': 42}
  json_string = '{"first_name": "John", "last_name": "Smith", "age": 42}'

  # To load JSON back to a data structure, use the loads method.
  person_parsed_dictionary = json.loads(json_string) 
  assert person_parsed_dictionary == person_dictionary

  # To encode a data structure to JSON, use the dumps method.
  encoded_person_string = json.dumps(person_dictionary)
  assert encoded_person_string == json_string

test_json()