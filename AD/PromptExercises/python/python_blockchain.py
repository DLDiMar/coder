import hashlib
import json
import csv

class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.genesis_block()

    def genesis_block(self):
        transactions = []  # No transactions in the genesis block
        genesis_block = Block(transactions, "0")
        self.chain.append(genesis_block)

    def new_block(self):
        previous_hash = self.last_block.hash
        block = Block(self.current_transactions, previous_hash)
        self.chain.append(block)
        # Clear the current transactions for the next block
        self.current_transactions = []

    @property
    def last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)

 
# Let's load the sample data in JSON format    
with open("90s_cartoon_data.json", 'r') as data_file: 
    data = json.load(data_file) 
  
# Now, let's use the blockchain class         
bc = Blockchain()
  
# Add each cartoon in the JSON as a transaction 
for cartoon in data:
    bc.add_transaction(cartoon)  
    bc.new_block()  # Mine the block with each transaction
 
 # Output as CSV files  
block_data = [('Block Hash', 'Previous Hash', 'Transaction ID', 'Show Name', 'Number of Minutes', 'Producing Company', 'Lead Writer', 'Release Date')]

for block in bc.chain:
    for index, tx in enumerate(block.transactions):
        block_data.append((
            block.hash, 
            block.previous_hash, 
            index,        
            tx['show_name'],             
            tx['number_minutes_all_shows'],            
            tx['producing_company'],             
            tx['lead_writer'],            
            tx['release_date']
        ))

with open('blockchain_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(block_data)
 
print("Blockchain data saved to 'blockchain_data.csv'.")