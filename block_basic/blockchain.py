blockchain = []
open_transactions = []
# Owner of this instance of the blockchain. Will be a hash in production
owner = "Michael"
counter = 0


def get_transaction_value():
    """ Returns the input of the user ( a new transaction amount ) as a float """
    # Get user input, transform it from a string to a float and store it
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Enter your transaction amount: "))
    return (tx_recipient, tx_amount)    # Return a Tuple


def get_user_choice():
    user_input = input("Input : ")
    return user_input if user_input else None


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def print_blockchain_data():
    for block in blockchain:
        print("Block : ", block)
    print(f"BlockChain Iteration {counter}: ", blockchain)


def add_transaction(sender, recipient, amount=1.0):
    """

Arguments:
        :sender: The sender of the coins,
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with transaction, default = 1

    """

    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transactions.append(transaction)


def mine_block():
    pass


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
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
        add_transaction(tx_amount, get_last_blockchain_value())
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
