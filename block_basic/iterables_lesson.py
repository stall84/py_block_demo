# 3 types of iterables in Python

# List (Array)
iterable = [
    "milk",
    "honey",
    "milk",
]  # mutable, ordered (order guaranteed), duplicates allowed

set_list = {
    "milk",
    "honey",
}  # mutable, un-ordered (order not guaranteed). Written with curly brackets. NO duplicates allowed

ma_tuple = (
    "Milk",
    "Honey",
)  # Imutable, ordered, duplicates OK, usually used for grouping

ma_dictionary = {
    "name": "Milk",
    "n": 2,
}  # similar to JS objects. These are maps. Unordered, Mutable, No duplicate Keys,
