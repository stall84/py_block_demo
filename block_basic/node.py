from uuid import uuid4
from blockchain import Blockchain
from verification import Verification


class Node:
    # We made the decision that our Node objects should contain local copies of the blockchain.
    # Eventually this class will be used to create a Node object for every user/participant connecting over the internet
    def __init__(self) -> None:
        # self.id = str(uuid4())
        self.id = 'TEMPORARY WALLET KEY'
        self.blockchain = Blockchain(self.id)

    def get_transaction_value(self):
        """Returns the input of the user ( a new transaction amount ) as a float"""
        # Get user input, transform it from a string to a float and store it
        tx_recipient = input("Enter the recipient of the transaction: ")
        tx_amount = float(input("Enter your transaction amount: "))
        return (tx_recipient, tx_amount)  # Return a Tuple

    def print_open_transactions(self, open_transactions):
        if len(open_transactions) > 0:
            for tx in range(len(open_transactions)):
                print(f"Idx/No. {tx+1} Open Transaction: ",
                      open_transactions[tx])
        else:
            print("No outstanding/open transactions...")

    def print_blockchain_data(self):
        # Output all blocks of the blockchain to the console
        for block in self.blockchain.chain:
            print("Block : ", block)
        else:
            print("_" * 20)

    def get_user_choice(self):
        # Prompts user for their choice and returns it
        user_input = input("Your choice : ")
        # Python ternary operator / operands
        return user_input if user_input else None

    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print("Please choose: ")
            print("1: Add a new transaction amount ")
            print("2: Mine a new block")
            print("3: Output the blockchain blocks")
            print("o: Print the current open transactions (not mined)")
            print("v: Check validity of all transactions")
            print("q: Quit")
            user_choice = self.get_user_choice()
            if user_choice == "1":
                tx_data = self.get_transaction_value()
                # you can 'destructure' a tuple a lot like you might in javascript by let [x, y] = someTuple
                recipient, amount = tx_data  # unpacked/destructured tuple.
                # Ourf add_transaction function has 3 positional arguments. we need to specify amount so that the arg isn't applied to 2nd position
                if self.blockchain.add_transaction(recipient, self.id, amount=amount):
                    print("Added Transaction!")
                else:
                    print("Transaction Failed..")
                print(self.blockchain.get_open_transactions())
            elif user_choice == "2":
                self.blockchain.mine_block()
            elif user_choice == "3":
                self.print_blockchain_data()
            elif user_choice == "o":
                self.print_open_transactions(
                    self.blockchain.get_open_transactions())
            elif user_choice == "v":
                if Verification.verify_transactions(self.blockchain.get_open_transactions(), self.blockchain.get_balance):
                    print("All transactions are valid")
                else:
                    print("There are invalid transactions")
            elif user_choice == "q":
                waiting_for_input = False
            else:
                print("Input was invalid, please pick a value from the list!")
            # Review string formatting {}:6.2f} is calling for max 6 digits with 2 decimal places - Print balances after any transaction
            print("Balance of {}: {:6.2f}".format(
                self.id, self.blockchain.get_balance()))
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_data()  # print the apparently corrupted blockchain to user
                print("Invalid Blockchain!")
                break  # Immediately exit

        print("Done!")


node = Node()
node.listen_for_input()
