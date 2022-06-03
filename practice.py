import hashlib
import json
import string

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

# copied_names = names
# print(copied_names)

# copied_names.pop()
# print(names)
# GENESIS_BLOCK = {'previous_hash': '', 'index': 0, 'transactions': []}
# block = {'previous_hash': "-0-[]-1-[{'sender': 'MINING', 'recipient': 'Michael', 'amount': 10}]-2-[{'sender': 'Michael', 'recipient': 'flerple@derple.com', 'amount': 10.0}, {'sender': 'MINING', 'recipient': 'Michael', 'amount': 10}]",
#          'index': 3, 'transactions': [{'sender': 'Michael', 'recipient': 'nerpnerd420@yahoo.com', 'amount': 4.2}, {'sender': 'MINING', 'recipient': 'Michael', 'amount': 10}]}


# def hash_test(block):
#     print('BEGINNING HASHING...')
#     print('-'*50)
#     print('INPUT OBJECT: ', block)
#     print('-'*50)
#     return hashlib.sha256(json.dumps(block).encode()).hexdigest()


# hash_out = hash_test(GENESIS_BLOCK)
# print('HASHED OUTPUT: ', hash_out)
# print('type(hash_out): ', type(hash_out))
# # print(hash_out.__str__())
# print(hash_out.digest())
# print(hash_out.__repr__())
# print(hash_out.name)
# print(hash_out.hexdigest())
# print(hash_out.__hash__())
# print(hash_out.__doc__)
# print(hash_out.__format__(''))
# print('hash_out.__dir__(): ', hash_out.__dir__())

# Palindrome (take in 2 strings, compare and return a boolean whether they are anagrams)
# For simplicity sake in this problem we will confine the input strings to consecutive all lower-case characters (no spaces).
# Will try to implement recursive solution
def anagram(str1: str, str2: str) -> bool:
    # If both inputs given as empty strings, consider that an anagram, return true
    if (len(str1) and len(str2) == 0):
        return True
    if (len(str1) != len(str2)):
        return False
    sort_str1 = list(str1)
    sort_str2 = list(str2)
    sort_str1.sort()
    sort_str2.sort()
    print('sort_str1: ', sort_str1)
    print('sort_str2: ', sort_str2)
    if (sort_str1 == sort_str2):
        return True
    else:
        return False


# print(anagram('fried', 'fired'))
# print(anagram('race', 'care'))
# print(anagram('flerp', 'plert'))

# 2nd version of anagram


def isAnagram(s: str, t: str) -> bool:
    if (len(s) != len(t)):
        return False
    else:
        s_dict = {}
        t_dict = {}

        for char in s:
            if (char in s_dict):
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if (char in t_dict):
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        if s_dict == t_dict:
            return True
        # for key in s_dict:
        #     if (key in t_dict.keys()):
        #         print('current s key: ', key)
        #         print('current t key: ', t_dict[key])
        #         if (s_dict[key] == t_dict[key]):
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False

    return False


print(isAnagram('fried', 'fired'))
print(isAnagram('flerp', 'aplert'))
print(isAnagram('racecar', 'racecar'))
print(isAnagram('racecar', 'racedar'))
print(isAnagram('a heart', 'a earth'))
print(isAnagram('rat', 'car'))
