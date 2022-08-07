import hashlib
import json


def hash_string_256(string):
    return hashlib.sha256(string).hexdigest()


def hash_block(last_block):
    """
    Hashes a block and returns a string representation of it.
    Arguments:
        :last_block: The block that should be hashed
    """
    # Since moving to a class-object Block instead of just a dictionary. We now have trouble serializing to JSON.
    # To avoid this, lets use python's __dict__ (dunder-dict lol)
    hashable_block = last_block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict()
                                      for tx in hashable_block['transactions']]
    return hash_string_256(json.dumps(hashable_block, sort_keys=True).encode())
