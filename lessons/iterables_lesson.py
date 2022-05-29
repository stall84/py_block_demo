# 3 types of iterables in Python

# List (This is a dynamic array .. borrows from Array Lists and array.array)
iterable = [
    "milk",
    "honey",
    "milk",
]  # mutable, ordered (order guaranteed), duplicates allowed

set_list = {
    "milk",
    "honey",
}  # mutable, un-ordered (order not guaranteed). Written with curly brackets. NO duplicates allowed
# Note that set's can be initialized in a few different ways. Above we have the standard literal construction
# Below we use the set constructor itself. Which must be passed an iterable.
# Be careful though because just calling set('Max'), since a string is an iteable would produce:
# {'M', 'a', 'x'} which might not be what you meant. Instead pass set(['Max']) to achieve: {'Max'}
new_set = set(['Michael', 'Max'])
print(new_set)  # {'Michael', 'Max'}

ma_tuple = (
    "Milk",
    "Honey",
)  # Imutable, ordered, duplicates OK, usually used for grouping

ma_dictionary = {
    "name": "Milk",
    "n": 2,
}  # similar to JS objects. These are maps. Unordered, Mutable, No duplicate Keys, and the key must be a string.
