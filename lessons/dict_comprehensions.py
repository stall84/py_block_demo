# Dictionary comprehension is a method for transforming one dictionary
# (or list / tuples.. probably any object) into another dictionary.
# During this transformation, items within the original dictionary can be conditionally
# included in the new dictionary and each item can be transformed as needed.

stats = [('age', 29), ('weight', 72), ('height', 178)]

# Using the unpacking/python-destructuring for the tuples in the list above
dict_stats = {key: value for (key, value) in stats}
