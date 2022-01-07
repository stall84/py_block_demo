blockchain = []
counter = 0


def get_transaction_value():
    user_input = float(input("Please enter a value:  "))
    return user_input if user_input else None


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


def add_value(transaction_amount, last_transaction):
    global counter
    counter += 1
    if (
        last_transaction == None
    ):  # Handle initial case where the blockchain will be empty (no -1 to access). For now we'll start every blockchain with [1]
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


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


while True:
    print("Please choose: ")
    print("1: Add a new transaction amount ")
    print("2: Output the blockchain blocks")
    print("h: Manipulate the cain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
        print_blockchain_data()
    elif user_choice == "h":
        if len(blockchain):
            blockchain[0] = [2]
    elif user_choice == "q":
        break
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print("Invalid Blockchain!")
        break

print("Done!")

# Notes
# Remember the and/or keywords, work pretty much same as JS
