class Roarixd(obejct):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
    def new_block(self):
        # create a new block and add to chain
        pass
    
    def new_transaction(self, sender, recipient, amount):
       # creates a new transaction
       pass
    
    @staticmethod
    def hash(block):
        # hashes a block
        pass
    
    @property
    def last_block(self):
        #returns the last Block in the chain
        pass
    