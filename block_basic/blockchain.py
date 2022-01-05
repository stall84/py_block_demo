blockchain = []
counter = 0


def get_transaction_value():
    user_input = float(input("Please enter a value:  "))
    return user_input if user_input else None


def get_user_choice():
    user_input = input("Input : ")
    if user_input == "Q":
        return 3
    return int(user_input) if user_input else None


def get_last_blockchain_value():
    return blockchain[-1]


def print_blockchain_data():
    for block in blockchain:
        print("Block : ", block)
    print(f"BlockChain Iteration {counter}: ", blockchain)


def add_value(transaction_amount, last_transaction=[0]):
    global counter
    counter += 1
    blockchain.append([last_transaction, transaction_amount])
    # print(counter)


tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print("Please choose: ")
    print("1: Add a new transaction amount ")
    print("2: Output the blockchain blocks")
    print("Q: Quit")
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
        continue
    elif user_choice == 2:
        print_blockchain_data()
        continue
    elif user_choice == 3:
        break
    else:
        print("Input was invalid, please pick a value from the list!")
        continue

print("Done!")
