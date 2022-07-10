# Ref:  https://realpython.com/list-comprehension-python/

# List Comprehensions are one of the most recognized key features of Python.. A powerful/expressive(debatable)
# way to essentially do maps/filters/reductions on Lists.

# EX1 - Duplicate simple_list by multiplying simple_list[i] by 2 IF those elements are also in the calc_items list. (Map in the javascript array method context)
simple_list = [1, 2, 3, 4]

calc_items = [1, 2]

dup_list = [element * 2 for element in simple_list if element in calc_items]

print('dup_list: ', dup_list)
# [2, 4]
