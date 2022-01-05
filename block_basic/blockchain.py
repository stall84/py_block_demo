blockchain = []
counter = 0


def get_transaction_value():
    user_input = float(input("Please enter a value:  "))
    return user_input if user_input else None


def get_user_choice():
    user_input = int(input("Please choose: "))
    return user_input if user_input else None


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[0]):
    global counter
    counter += 1
    blockchain.append([last_transaction, transaction_amount])
    # print(counter)
    print(f"BlockChain Iteration {counter}: ", blockchain)


tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print("1: Add a new transaction amount ")
    print("2: Output the blockchain blocks")

    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_value()
        add_value(tx_amount, get_last_blockchain_value())
        continue
    elif user_choice == 2:
        for block in blockchain:
            print("Block : ", block)
        break
