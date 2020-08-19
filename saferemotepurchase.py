import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.defaultAccount = w3.eth.accounts[1]


address = '0x6303bB8b0edd1734613339941c13ceAC955364a3'
abi = json.loads('[{"outputs": [], "inputs": [], "stateMutability": "payable", "type": "constructor"}, {"name": "abort", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 28014}, {"name": "purchase", "outputs": [], "inputs": [], "stateMutability": "payable", "type": "function", "gas": 58217}, {"name": "received", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 99365}, {"name": "value", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1241}, {"name": "seller", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1271}, {"name": "buyer", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1301}, {"name": "unlocked", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1331}, {"name": "ended", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1361}]')
contract = w3.eth.contract(address=address, abi=abi)


# Purchase
tx = {
    'nonce': w3.eth.getTransactionCount(w3.eth.accounts[1]),
    'value': w3.toWei('40', 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}
# contract.functions.purchase().transact(tx)    # item purchased


# Received
contract.functions.received().transact()