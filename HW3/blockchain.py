import json
from hashlib import sha256

from matplotlib.font_manager import json_dump

# Functions that Calculate Nonce
# Try with Hash
def miner(_block,_prefix):
    for i in range(1000000):
        block_nonce = str(_block) + str(i)
        digest = sha256(block_nonce.encode()).hexdigest()
        if digest.startswith(_prefix):
            nonce = str(i)
            return nonce

# Open & Load GenesisBlock file
genesisBlock_file = open('GenesisBlock/GenesisBlock.json')
genesisBlock_json = json.load(genesisBlock_file)

# Open & Load Ledger Number File 
# Add each ledger to ledgers's Array
ledgers = [] 
for i in range(0,15):
    temp = open('Ledgers/Ledger_Number{}.json'.format(i+2))
    ledgers_file = json.load(temp)
    ledgers.append(ledgers_file)

# Open & Load Math Problem Number File 
# Add each Math Problem to Problems's Array
problems = [] 
for i in range(0,15):
    temp = open('Math_Problems/Math_Problem_Number{}.json'.format(i+2))
    problems_file = json.load(temp)
    problems.append(problems_file)
    

# Initalization of Blockchain
# Adding Genesis Block to Blockchain
genesis_Block = {'blockNumber' : 1 ,'main' : genesisBlock_json,'Nonce' : None, 'previous_hash' : None}
blockchain = []
blockchain.append(genesis_Block)

# Store Last Hash
last_Block_Hash = sha256(str(genesis_Block).encode()).hexdigest()

listObj = []

# Loop to Builds Blocks
# Find Nonce for Blocks
# Add Nonce to Blockchain
for index in range(0,15):
    temp_block = {'main' : ledgers[index], 'Nonce' : None, 'previous_hash' : last_Block_Hash}
    temp_prefix_Block = problems[index]['mathProblem']
    
    # Calculate Nonce
    temp_nonce = miner(temp_block,temp_prefix_Block)
     
    temp_block.update({'Nonce' : temp_nonce})
    blockchain.append(temp_block)
    # print(blockchain[index])
    # print("Current Hash: " + last_Block_Hash)
    listObj.append({'Block Number' : index+1, 'Nonce' : blockchain[index]['Nonce'],
     'Current Hash' : last_Block_Hash, 'Previous Hash' : blockchain[index]['previous_hash']})
    
    with open("output.json", 'w') as json_file:
        json.dump(listObj, json_file, 
                           indent=4,  
                           separators=(',',': '))

    last_Block_Hash = sha256(str(temp_block).encode()).hexdigest()





 


