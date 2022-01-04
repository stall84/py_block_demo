blockchain = []
counter = 0


def get_user_input():
    return float(input("Please enter transaction amount: "))


def get_last_blockchain_value():
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    global counter
    counter += 1
    blockchain.append([last_transaction, transaction_amount])
    print(counter)
    print(blockchain)


tx_amount = get_user_input()
add_value(tx_amount)
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
tx_amount = get_user_input()
add_value(tx_amount, get_last_blockchain_value())
