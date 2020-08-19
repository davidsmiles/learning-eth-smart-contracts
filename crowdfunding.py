import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))
w3.eth.defaultAccount = w3.eth.accounts[7]


address = '0xE74D856349fc9cE4Dd48947AC450a4A813FEB64b'
abi = json.loads('[{"outputs": [], "inputs": [{"type": "address", "name": "_beneficiary"}, {"type": "uint256", "name": "_goal"}, {"type": "uint256", "name": "_timelimit"}], "stateMutability": "nonpayable", "type": "constructor"}, {"name": "participate", "outputs": [], "inputs": [], "stateMutability": "payable", "type": "function", "gas": 108194}, {"name": "refundAll", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 3488253}, {"name": "finalize", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 63993}, {"name": "beneficiary", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1241}, {"name": "goal", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1271}, {"name": "timelimit", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1301}, {"name": "deadline", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1331}, {"name": "ended", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1361}, {"name": "funders", "outputs": [{"type": "address", "name": "sender"}, {"type": "uint256", "name": "amount"}], "inputs": [{"type": "uint256", "name": "arg0"}], "stateMutability": "view", "type": "function", "gas": 2798}, {"name": "fundersCount", "outputs": [{"type": "int128", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1421}, {"name": "refundIndex", "outputs": [{"type": "int128", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1451}]')
contract = w3.eth.contract(address=address, abi=abi)


# Participate
tx = {
    'nonce': w3.eth.getTransactionCount(w3.eth.accounts[7]),
    'value': w3.toWei('99', 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}
#contract.functions.participate().transact(tx)

# Finalize
# contract.functions.finalize().transact()

# RefundAll
contract.functions.refundAll().transact()


print(f"Crowdfunding balance: {w3.fromWei(w3.eth.getBalance(address), 'Ether')}")
