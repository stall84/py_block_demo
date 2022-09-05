from hash_util import hash_string_256, hash_block


class Verification:

    def valid_proof(self, transactions, last_hash, proof):
        # We'll initially guess by taking our block and adding to it this separate 'proof'.. Create a string and hash it
        # guess = (str(transactions) + str(last_hash) + str(proof)).encode()
        guess = (str([tx.to_ordered_dict() for tx in transactions]) +
                 str(last_hash) + str(proof)).encode()
        print("DEBUG - guess: ", guess)
        guess_hash = hash_string_256(guess)
        print("guess_hash: ", guess_hash)
        # The leading 2 0's below is merely an arbitrary condition picked to validate the hash..
        # Essentially this is determining if the input proof does indeed lead to this hash
        # Return True when this condition is met
        return guess_hash[0:2] == "00"

    def verify_chain(self, blockchain):
        # Using enumerate function to return a tuple where 1st element is index of element, and 2nd is the value
        for (index, block) in enumerate(blockchain):
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            # Check the proof as well
            if not self.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print("Proof of Work is Invalid ...")
                return False
        return True

    def verify_transaction(self, transaction, get_balance):
        sender_balance = get_balance()
        return sender_balance >= transaction.amount

    def verify_transactions(self, open_transactions, get_balance):
        # Verify all open transactions
        return all([self.verify_transaction(tx, get_balance) for tx in open_transactions])
