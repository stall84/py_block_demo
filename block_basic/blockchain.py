# Initiating our (empty) blockchain List
blockchain = []
open_transactions = []
# Owner of this instance of the blockchain. Will be a hash in production
owner = "Michael"
counter = 0


def get_user_choice():
    # Prompts user for their choice and returns it
    user_input = input("Your choice : ")
    return user_input if user_input else None


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    # Using negative index to return the last-in element
    return blockchain[-1]


def print_blockchain_data():
    # Output all blocks of the blockchain to the console
    for block in blockchain:
        print("Block : ", block)
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


def mine_block():
    pass


def get_transaction_value():
    """ Returns the input of the user ( a new transaction amount ) as a float """
    # Get user input, transform it from a string to a float and store it
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Enter your transaction amount: "))
    return (tx_recipient, tx_amount)    # Return a Tuple


def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:

            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid
    # return False


waiting_for_input = True

while waiting_for_input:
    print("Please choose: ")
    print("1: Add a new transaction amount ")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the cain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        # you can 'destructure' a tuple a lot like you might in javascript by let [x, y] = someTuple
        recipient, amount = tx_data     # unpacked/destructured tuple.
        # Our add_transaction function has 3 positional arguments. we need to specify amount so that the arg isn't applied to 2nd position
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == "2":
        print_blockchain_data()
    elif user_choice == "h":
        if len(blockchain):
            blockchain[0] = [2]
    elif user_choice == "q":
        waiting_for_input = False
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print("Invalid Blockchain!")
        break

print("Done!")
