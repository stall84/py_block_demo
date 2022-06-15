# Imports
import functools
import hashlib
import json
from collections import OrderedDict
# Global constants and variables
MINING_REWARD = 10
GENESIS_BLOCK = {'previous_hash': '',
                 'index': 0,
                 'transactions': [],
                 'proof': 100}  # Dictionary
blockchain = [GENESIS_BLOCK]  # List structure for our main blockchain datatype
open_transactions = []
# Owner of this instance of the blockchain. Will be a hash in production
owner = 'Michael'
participants = {'Michael'}  # set literal
counter = 0


def get_user_choice():
    # Prompts user for their choice and returns it
    user_input = input('Your choice : ')
    # Python ternary operator / operands
    return user_input if user_input else None


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    # Using negative index to return the last-in element
    return blockchain[-1]


def print_open_transactions():
    if len(open_transactions) > 0:
        for tx in range(len(open_transactions)):
            print(f'Idx/No. {tx+1} Open Transaction: ', open_transactions[tx])
    else:
        print('No outstanding/open transactions...')


def print_blockchain_data():
    # Output all blocks of the blockchain to the console
    for block in blockchain:
        print('Block : ', block)
    else:
        print('_' * 20)
    # print(f"BlockChain Iteration {counter}: ", blockchain)    # Here an example of template-literal use in python (note the 'f' preceding quotes)


def add_transaction(recipient, sender=owner, amount=1.0):
    """
    Arguments:
            :recipient: The recipient of the coins (required)
            :sender: The sender of the coins, placed after recipient because of the optional deault
                     (optional args must go after required ones)
            :amount: The amount of coins sent with transaction, (optional default = 1)
    """
    # Form a dictionary-literal from our inputs. Append this new dict to the transactions list
    # transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    transaction = OrderedDict(
        [('sender', sender), ('recipient', recipient), ('amount', amount)])
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        # Lets return a boolean (something) so that we can handle/communicate errors
        return True
    return False


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


def hash_block(last_block):
    # return '-'.join([str(last_block[key]) for key in last_block])
    return hashlib.sha256(json.dumps(last_block, sort_keys=True).encode()).hexdigest()


'''
    Need to review the proof-validating function below and the concept/mechanism as a whole. -- 6-22
'''


def valid_proof(transactions, last_hash, proof):
    # We'll initially guess by taking our block and adding to it this separate 'proof'.. Create a string and hash it
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    print('guess_hash: ', guess_hash)
    # The leading 2 0's below is merely an arbitrary condition picked to validate the hash..
    # Essentially this is determining if the input proof does indeed lead to this hash
    return guess_hash[0:2] == '00'  # Return True when this condition is met


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    # Continue working (looping) until valid_proof returns True, at which point our Proof has
    # correctly 'solved' the proof of work 'puzzle'
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof


def get_balance(participant):
    # We're going to use a nested list comprehension here.. I'm not a huge fan of these so far.. but the idea is
    # we want to pull out each transaction's amount made by a particular participant iterating through each block in the blockchain
    tx_sender = [[tx['amount'] for tx in block['transactions']
                  if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount']
                      for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)    # More balance verification
    # Remember tx_sender is a list of lists.. so access the 0th element for the value itself in amount_sent calc below
    # We use a ternary expression in the reduce lambda below. Slightly different arrangement than in JS
    # where: (Value If True) if (Condition to test) else (Value If False)
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    # amount_sent = 0
    # for tx in tx_sender:
    #     if len(tx) > 0:
    #         # Remember tx_sender is a list of lists.. so access the 0th element for the value itself
    #         amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions']
                     if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx) > 0:
    #         # Remember tx_recipient is a list of lists.. so access the 0th element for the value itself
    #         amount_received += tx[0]
    # We could return a tuple here i.e. (amount_sent, amount_received). But also could go ahead and
    # Do a balance calculation to return the remaining balance (positive or negative) to the participant
    return amount_received - amount_sent


def mine_block():
    try:
        # You can use negative element notation to access elements from end (right side)
        last_block = blockchain[-1]
        # List Comprehension .. Kind of like spreading and templating/formatting in a the the same time
        hashed_block = hash_block(last_block)
        # Call our proof-of-work function for mining process
        proof = proof_of_work()
        # Carry out the reward assignment to the miner of record (owner)
        # reward_transaction = {
        #     'sender': 'MINING',
        #     'recipient': owner,
        #     'amount': MINING_REWARD
        # }
        # Using the OrderedDict imported object to preclude any key-value order-mismatch
        reward_transaction = OrderedDict(
            [('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
        # Apend the miner's payout before combining and applying them to blockchain
        # We want to use a copy of open_transactions to limit errors at scale..
        # To do so, use the [:] list operation to 'spread in' all of the elements (copy them)
        copied_transactions = open_transactions[:]
        copied_transactions.append(reward_transaction)
        block = {
            'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': copied_transactions,
            'proof': proof,
        }
        blockchain.append(block)
        # We still need to add validation in this method
        # Clear open transactions after write ?
        # open_transactions.clear()
        return True
    except:
        print('ERROR MINING BLOCK - ABORTED')


def get_transaction_value():
    """Returns the input of the user ( a new transaction amount ) as a float"""
    # Get user input, transform it from a string to a float and store it
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Enter your transaction amount: '))
    return (tx_recipient, tx_amount)  # Return a Tuple

# Just FYI there is no formal iterator variable in Python for looping.
# i.e. in most langs you'll hav e for (let i = 0; i < whatever.length i++) {}
# In Python you have to make use of the range function to set increment/decrement, etc.


def verify_chain():
    # Using enumerate function to return a tuple where 1st element is index of element, and 2nd is the value
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
        # Check the proof as well
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of Work is Invalid ...')
            return False
    return True
    # # block_index = 0
    # is_valid = True
    # for block_index in range(len(blockchain)):
    #     if block_index == 0:

    #         continue
    #     elif blockchain[block_index][0] == blockchain[block_index - 1]:
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    # return is_valid
    # # return False


waiting_for_input = True

while waiting_for_input:
    print('Please choose: ')
    print('1: Add a new transaction amount ')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('o: Print the current open transactions (not mined)')
    print('p: Print all participants')
    print('v: Check validity of all transactions')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # you can 'destructure' a tuple a lot like you might in javascript by let [x, y] = someTuple
        recipient, amount = tx_data  # unpacked/destructured tuple.
        # Ourf add_transaction function has 3 positional arguments. we need to specify amount so that the arg isn't applied to 2nd position
        if add_transaction(recipient, amount=amount):
            print('Added Transaction!')
        else:
            print('Transaction Failed..')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []  # If minining successfull - clear the open transactions list

    elif user_choice == '3':
        print_blockchain_data()
    elif user_choice == 'h':
        # Make sure that you don't try to "hack" the blockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
            }
    elif user_choice == 'o':
        print_open_transactions()
    elif user_choice == 'p':
        print('Participants: ')
        for participant in participants:
            print(participant)
    elif user_choice == 'v':
        if verify_transactions():
            print('All transactions are valid')
        else:
            print('There are invalid transactions')
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    # Review string formatting {}:6.2f} is calling for max 6 digits with 2 decimal places - Print balances after any transaction
    print('Balance of {}: {:6.2f}'.format('Michael', get_balance('Michael')))
    if not verify_chain():
        print_blockchain_data()         # print the apparently corrupted blockchain to user
        print('Invalid Blockchain!')
        break                           # Immediately exit

print('Done!')
