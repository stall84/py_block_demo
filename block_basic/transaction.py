from collections import OrderedDict


class Transaction:
    def __init__(self, sender, recipient, amount) -> None:
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_ordered_dict(self):
        # Pass a list of tuples to the OrderedDict function
        return OrderedDict([('sender', self.sender), ('recipient', self.recipient), ('amount', self.amount)])

    def __repr__(self) -> str:
        return f'Sender: {self.sender}, Recipient: {self.recipient}, Amount: {self.amount}'
