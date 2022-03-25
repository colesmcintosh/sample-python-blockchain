from blockchain import Blockchain

block_transactions = [{"sender":"Mo Salah", "receiver": "Roberto Firmino", "amount":"50"}, {"sender": "Sadio Mane", "receiver":"Harvey Elliott", "amount":"25"}, {"sender":"Luis Diaz", "receiver":"Virgil Van Dijk", "amount":"35"}
]
fake_transaction = {"sender": "Mason Mount", "receiver":"Christian Pulisic, Kai Havertz", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

[local_blockchain.add_block(transaction) for transaction in block_transactions]
local_blockchain.print_blocks()

# Comment out the below line to produce valid blockchain. This line is intended to show what an invalid transaction would do.
local_blockchain.chain[2].transactions = fake_transaction

local_blockchain.validate_chain()