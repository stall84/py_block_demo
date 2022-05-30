import functools
# map() function in python has slightly different syntax than JS,
# but both do the same thing: apply a transforming function for every element in a List (or Array in JS)
# classic syntax is: map(callback_function, [List]) where 1st arg is the callback function applied to each element
# and 2nd arg is the List being operated on.

num_list = [1, 2, 3, 4, 5]

# NOTE: On average, especially at large scale input sizes, List Comprehension operations will be faster/more-efficient
#           Than map() function.

# def square(element):
#     return element * element


# squared_list = map(square, num_list)
# print('squared_list: ', squared_list)

def squarer(element):
    return element * element


# Unlike JS .. The map function will return a map object <class map> and will not automatically return a new list
squareded_map = map(squarer, num_list)
# This could be another reason to use List Comprehension over map().. Because w/ map() we must add a further step
# to convert the returned map object to a list.
listified_squareded_map = list(squareded_map)
print(f'typeof squareded_map after map function : {type(squareded_map)}')
print(
    f'typeof listified_squareded_map after list conversion : {type(listified_squareded_map)}')

# The map object returned by map() can still be iterated over the same as a list, but behavior will differ in other areas
for ele in squareded_map:
    print('# ', ele)


# Lambda Functions - Essentially same functionality as in JS but with different syntax: lambda x: x where x is the argument and 2nd x is function body

# Applying our same 'squaring' operation implemented in map() above, but with lambda (anonymous function)
# also here we wrap the map function in a list transform from the outset
lambdad_squared_list = list(map(lambda x: x * x, num_list))
print('lambdad_squared_list: ', lambdad_squared_list)
for num in lambdad_squared_list:
    print('* ', num)


# Reduce() - Requires an import of the functools package as it's not in standard python library (currently)
# definition: reduce(callbackFn, Iterable/Sequence, optional_initial_value)
reduced_result = functools.reduce(
    lambda prev, curr: prev + curr, [1, 2, 3, 4, 5])

print('reduced_result: ', reduced_result)  # 15
