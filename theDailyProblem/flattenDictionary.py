"""
Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
You can assume there will be no arrays, and all keys will be strings.

Here's some starter code:

def flatten_dictionary(d):
  # Fill this in.

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d))
# {'a': 1, 'b.c': 2, 'b.d.e': 3}
"""

def flatten_dictionary(d, ancestry, flat):
  for key, value in d.items():
     
    # Generate the ancestry key
    if ancestry:
      a = ancestry + "." + key
    else:
      a = key

    # Recurse or flatten dictionary
    if isinstance(d[key], dict):
      flatten_dictionary(d[key], a, flat)
    else:
      if a not in flat:
        flat[a] = value
      else:
        print("array value")
  return flat

d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}
print(flatten_dictionary(d, "", {}))
print({'a': 1, 'b.c': 2, 'b.d.e': 3})
