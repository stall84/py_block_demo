import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(last_block):
    '''
    Hashes a block and returns a string representation of it.
    Arguments: 
        :last_block: The block that should be hashed
    '''
    # return '-'.join([str(last_block[key]) for key in last_block])
    return hash_string_256(json.dumps(last_block, sort_keys=True).encode())
