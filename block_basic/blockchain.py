# Initiating our (empty) blockchain List

genesis_block = {'previous_hash': '',
                 'index': 0, 'transactions': []}  # Dictionary
blockchain = [genesis_block]  # List structure for our main blockchain datatype
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
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def hash_block(last_block):
    return '-'.join([str(last_block[key]) for key in last_block])


def mine_block():
    try:
        # You can use negative element notation to access elements from end (right side)
        last_block = blockchain[-1]
        # List Comprehension .. Kind of like spreading and templating/formatting in a the the same time
        hashed_block = hash_block(last_block)
        # lines 61-67 below were the original straightforward for-loop approach to iterating a List .. There is however List Comprehension which we use above instead
        # hashed_block = ''
        # Just like js you can (except arguably much more straightforward here in python) iterate over the keys
        # In a dictionary object. Here we iterate over the previous block's keys and values (i.e. 'previous_hash':'XYX', 'index': 3, 'transactions': [...] )
        # Then we stringify the previous block (hashed_block) to store it.
        # for keys in last_block:
        #     value = last_block[keys]
        #     hashed_block += str(value)
        block = {
            'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': open_transactions,
        }
        blockchain.append(block)
        # We still need to add validation in this method
        # Clear open transactions after write ?
        open_transactions.clear()
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
    print('h: Manipulate the cain')
    print('o: Print the current open transactions (not mined)')
    print('p: Print all participants')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        # you can 'destructure' a tuple a lot like you might in javascript by let [x, y] = someTuple
        recipient, amount = tx_data  # unpacked/destructured tuple.
        # Our add_transaction function has 3 positional arguments. we need to specify amount so that the arg isn't applied to 2nd position
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
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
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_data()         # print the apparently corrupted blockchain to user
        print('Invalid Blockchain!')
        break                           # Immediately exit

print('Done!')
