import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))

# set up default account
w3.eth.defaultAccount = w3.eth.accounts[1]


# instantiate the contract
abi = json.loads('[{"constant":false,"inputs":[{"name":"content","type":"string"}],"name":"createTask","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"tasks","outputs":[{"name":"id","type":"uint256"},{"name":"content","type":"string"},{"name":"completed","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"taskCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
address = w3.toChecksumAddress('0x0f3111eb9fB7e5D9bDeccC3AB7E0e71a212339B0')
contract = w3.eth.contract(address=address, abi=abi)


# call some functions
for i in range(1, contract.functions.taskCount().call() + 1):
    tasks = contract.functions.tasks(i).call()
    print(f'{i} {tasks}')


# add a task
# contract.functions.createTask('Learn blockchain too').transact()
