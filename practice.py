names = ['David', 'Paul', 'Adrienne', 'Becca', 'Alexander']

# print('names start length: ', len(names))
# for name in names:
#     if (len(name) > 5):
#         if ('n' in name.lower()):
#             print(len(name))
# while (len(names) > 0):
#     current = names.pop()
#     print('popping : ', current)
# print('names end length: ', len(names))

# for name in range(len(names)):
#     print(f'name no.{name}: ', names[name])


# def palindrome(string):
#     if (len(string) <= 1):
#         return True
#     elif string[0] == string[-1]:
#         return palindrome(string[1:-1])
#     return False


# print(palindrome('kayak'))
# print(palindrome('pasta'))
# print(palindrome('racecar'))
# print(palindrome('civic'))
# print(palindrome('gag'))
# print(palindrome('nodakon'))

copied_names = names
print(copied_names)

copied_names.pop()
print(names)
