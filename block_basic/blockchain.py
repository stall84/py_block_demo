# Imports
import functools
import hashlib
import json
from collections import OrderedDict
import pickle  # pickle package / 'pickling' can convert python data to binary, store it as such, and serialiaze/deserialize on that. Somewhat in contrast with json

# Custom Imports
from hash_util import hash_string_256, hash_block
from block import Block
from transaction import Transaction
from verification import Verification

# Global constants and variables
MINING_REWARD = 10
counter = 0


class Blockchain:

    def __init__(self, hosting_node_id) -> None:
        self.hosting_node = hosting_node_id
        GENESIS_BLOCK = Block(0, "", [], 100, 0)
        # List structure for our main blockchain datatype
        # Initialized to an empty list and named 'chain' to differentiate
        # from the Blockchain class/object
        self.chain = [GENESIS_BLOCK]
        self.__open_transactions = []
        # Immediately Call to load-in most recent saved copy of the blockchain/open_transactions
        self.load_data()

    @property
    def chain(self):
        # Return a copy of the chain. This adds a layer of protection against outside modification since this is a reference object.
        return self.__chain[:]
        # (If we had just returned self.__chain.. that would have given access to the object itself)

    @chain.setter
    def chain(self, val):
        self.__chain = val

    def get_open_transactions(self):
        # Return a copy of the chain. This adds a layer of protection against outside modification since this is a reference object.
        return self.__open_transactions[:]
        # (If we had just returned self.__open_transactions.. that would have given access to the object itself)

    def load_data(self):
        # We want to guard (error-handle) against the possibility the blockchain.txt/p file may not exist. Use a try/catch block
        # To access our blockchain and open_transactions global variables
        # from inside this function scope use 'global' keyword
        # UPDATE: However since we've moved all of these to a dedicated Blockchain class, we no longer need to set global scoped variables..
        try:
            # Using an alternate pickle data serialization process.. change mode from 'r' for original text/json implementation to 'rb' for read-binary for binary/pickle
            with open("blockchain.txt", mode="r") as curr_file:
                # To get all lines read-in in a list format. use readlines()
                file_content = curr_file.readlines()

                # Our output list has the blockchain on the first line. Open transactions on 2nd
                # We select the range everything (:) up to and excluding the last character (which is the newline)
                blockchain = json.loads(file_content[0][:-1])
                updated_blockchain = []
                # # Currently very confused over what we're doing here, but understand it's to deserialize the json loaded data into the OrderedDict format we're using when saving.
                for block in blockchain:
                    converted_trans = [Transaction(
                        tx['sender'], tx['recipient'], tx['amount']) for tx in block['transactions']]

                    updated_block = Block(
                        block["index"],
                        block["previous_hash"],
                        converted_trans,
                        block["proof"],
                        block["timestamp"],
                    )

                    updated_blockchain.append(updated_block)
                self.chain = updated_blockchain
                # # No newline at end of open_transactions so no range need selected
                open_transactions = json.loads(file_content[1])
                updated_transactions = []
                for tx in open_transactions:
                    updated_transaction = Transaction(
                        tx['sender'], tx['recipient'], tx['amount'])
                    updated_transactions.append(updated_transaction)
                self.__open_transactions = updated_transactions

                # Pickling removes the need for the previous ~ 25 lines because being a binary serialization, it keeps the OrderedDict 'metadata' and we don't
                # have to perform the complex transformation we did with the json/text serialization. However we will switch to the longer
                # json serialization in order to manipulate the text file and check our security. Long Term pickle prob should be used

        # NOTE: Important to handle each exception explicitly, as we do the IOError (after the except keyword) below
        #       In the exception clause below we initially tried without specifiying an exception type.. this worked, but is an anti-pattern and will obfuscate errors..
        #       Instead always follow except with the exception type to be handled.. you can string together multiple except clauses. Or alternatively can include more than 1 in parenthesis
        #       While you can use a 'catch-all' except statement with NO specified exception.. this must be used with care because it will hide important information about errors/bugs
        except (IOError, IndexError):
            print("Handled either IOError or IndexError exceptions...")

        finally:
            # Just like in javascript the finally block works exactly the same, will always be executed regardless of a successful try or an exception
            print("Cleanup..")

    def save_data(self):
        try:
            # We'll always want a fresh/new snapshot of the blocks. so use 'w' and not 'a' as mode
            # Utilize with-as block to have python manage memory for file operations
            # for write mode.. default is 'wt' or just 'w' which is TEXT.. When implementing pickle-binary we change to 'wb' WRITE-BINARY (also change file extension to .p for pickle)
            with open(
                "blockchain.txt", mode="w"
            ) as curr_file:  # Lazy var naming. 'f' for 'file'
                # We need to standardize the serialization/deserialization of our blockchain/open_transactions write/saves
                # So we will use the JSON library for that
                # After switching to class-object form of block.. we need to make the blockchain serializable for the json function again
                saveable_chain = [
                    block.__dict__ for block in [Block(block_el.index, block_el.previous_hash, [tx.__dict__ for tx in block_el.transactions], block_el.proof, block_el.timestamp) for block_el in self.__chain]
                ]  # After moving to class-objcet Block.. This list comprehension will create a json-able list of block dicts
                curr_file.write(json.dumps(saveable_chain))
                curr_file.write("\n")
                saveable_trans = [
                    tx.__dict__ for tx in self.__open_transactions]
                curr_file.write(json.dumps(saveable_trans))

        except IOError:
            print("Error saving blockchain file...")

    def proof_of_work(self):
        last_block = self.__chain[-1]
        last_hash = hash_block(last_block)
        proof = 0
        # Continue working (looping) until valid_proof returns True, at which point our Proof has
        # correctly 'solved' the proof of work 'puzzle'
        while not Verification.valid_proof(self.__open_transactions, last_hash, proof):
            proof += 1
        return proof

    def get_balance(self):
        participant = self.hosting_node
        # We're going to use a nested list comprehension here.. I'm not a huge fan of these so far.. but the idea is
        # we want to pull out each transaction's amount made by a particular participant iterating through each block in the blockchain
        # Changes below represent our move from a Dictionary 'literal' to our custom Transaction object (access pros via dot notation)
        tx_sender = [
            [tx.amount for tx in block.transactions if tx.sender == participant]
            for block in self.__chain
        ]
        open_tx_sender = [
            tx.amount for tx in self.__open_transactions if tx.sender == participant
        ]
        tx_sender.append(open_tx_sender)  # More balance verification
        # Remember tx_sender is a list of lists.. so access the 0th element for the value itself in amount_sent calc below
        # We use a ternary expression in the reduce lambda below. Slightly different arrangement than in JS
        # where: (Value If True) if (Condition to test) else (Value If False)
        amount_sent = functools.reduce(
            lambda tx_sum, tx_amt: tx_sum +
            sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
            tx_sender,
            0,
        )
        tx_recipient = [
            [tx.amount
                for tx in block.transactions if tx.recipient == participant]
            for block in self.__chain
        ]
        amount_received = functools.reduce(
            lambda tx_sum, tx_amt: tx_sum +
            sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
            tx_recipient,
            0,
        )
        return amount_received - amount_sent

    def get_last_blockchain_value(self):
        if len(self.__chain) < 1:
            return None
        # Using negative index to return the last-in element
        return self.__chain[-1]

    def add_transaction(self, recipient, sender, amount=1.0):
        """
        Arguments:
                :recipient: The recipient of the coins (required)
                :sender: The sender of the coins, placed after recipient because of the optional deault
                        (optional args must go after required ones)
                :amount: The amount of coins sent with transaction, (optional default = 1)
        """
        # Form a dictionary-literal from our inputs. Append this new dict to the transactions list
        transaction = Transaction(sender, recipient, amount)

        if Verification.verify_transaction(transaction, self.get_balance):
            self.__open_transactions.append(transaction)
            # participants.add(sender)
            # participants.add(recipient)
            self.save_data()
            # Lets return a boolean (something) so that we can handle/communicate errors
            return True
        return False

    def mine_block(self):
        try:
            # You can use negative element notation to access elements from end (right side)
            last_block = self.__chain[-1]
            # List Comprehension .. Kind of like spreading and templating/formatting in a the the same time
            hashed_block = hash_block(last_block)
            # Call our proof-of-work function for mining process
            proof = self.proof_of_work()
            # After creating our Node class.. the old 'owner' is now going to be the node..
            # the local instantiation of the blockchain on the user's computer..
            # i.e. the 'owner'
            reward_transaction = Transaction(
                'MINING', self.hosting_node, MINING_REWARD)
            # Apend the miner's payout before combining and applying them to blockchain
            # We want to use a copy of open_transactions to limit errors at scale..
            # To do so, use the [:] list operation to 'spread in' all of the elements (copy them)
            copied_transactions = self.__open_transactions[:]
            copied_transactions.append(reward_transaction)
            block = Block(
                len(self.__chain),
                hashed_block,
                copied_transactions,
                proof,
            )
            self.__chain.append(block)
            # Clear/Reset the open transactions after mining the block
            self.__open_transactions = (
                []
            )
            self.save_data()
            return True
        except:
            print("ERROR MINING BLOCK - ABORTED")


# blockchain = []  # List structure for our main blockchain datatype
# open_transactions = []
# Owner of this instance of the blockchain. Will be a hash in production
owner = "Michael"
participants = {"Michael"}  # set literal


# def get_user_choice():
#     # Prompts user for their choice and returns it
#     user_input = input("Your choice : ")
#     # Python ternary operator / operands
#     return user_input if user_input else None


# def print_open_transactions():
#     if len(open_transactions) > 0:
#         for tx in range(len(open_transactions)):
#             print(f"Idx/No. {tx+1} Open Transaction: ", open_transactions[tx])
#     else:
#         print("No outstanding/open transactions...")

# def print_blockchain_data():
#     # Output all blocks of the blockchain to the console
#     for block in blockchain:
#         print("Block : ", block)
#     else:
#         print("_" * 20)

# def verify_transaction(transaction):
#     sender_balance = get_balance(transaction.sender)
#     return sender_balance >= transaction.amount


# def verify_transactions():
#     # Verify all open transactions
#     return all([verify_transaction(tx) for tx in open_transactions])


# def valid_proof(transactions, last_hash, proof):
#     # We'll initially guess by taking our block and adding to it this separate 'proof'.. Create a string and hash it
#     # guess = (str(transactions) + str(last_hash) + str(proof)).encode()
#     guess = (str([tx.to_ordered_dict() for tx in transactions]) +
#              str(last_hash) + str(proof)).encode()
#     print("DEBUG - guess: ", guess)
#     guess_hash = hash_string_256(guess)
#     print("guess_hash: ", guess_hash)
#     # The leading 2 0's below is merely an arbitrary condition picked to validate the hash..
#     # Essentially this is determining if the input proof does indeed lead to this hash
#     return guess_hash[0:2] == "00"  # Return True when this condition is met


# def get_transaction_value():
#     """Returns the input of the user ( a new transaction amount ) as a float"""
#     # Get user input, transform it from a string to a float and store it
#     tx_recipient = input("Enter the recipient of the transaction: ")
#     tx_amount = float(input("Enter your transaction amount: "))
#     return (tx_recipient, tx_amount)  # Return a Tuple


# Just FYI there is no formal iterator variable in Python for looping.
# i.e. in most langs you'll hav e for (let i = 0; i < whatever.length i++) {}
# In Python you have to make use of the range function to set increment/decrement, etc.


# def verify_chain():
#     # Using enumerate function to return a tuple where 1st element is index of element, and 2nd is the value
#     for (index, block) in enumerate(blockchain):
#         if index == 0:
#             continue
#         if block.previous_hash != hash_block(blockchain[index - 1]):
#             return False
#         # Check the proof as well
#         if not valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
#             print("Proof of Work is Invalid ...")
#             return False
#     return True
