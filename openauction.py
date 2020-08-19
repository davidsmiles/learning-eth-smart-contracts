import json
from web3 import Web3

ganache_url = 'http://127.0.0.1:7545'
w3 = Web3(Web3.HTTPProvider(ganache_url))

# set up default account
w3.eth.defaultAccount = w3.eth.accounts[0]


address = '0xcF7dCB50434b316d6C64A46bb8C2D2e9D312326c'
abi = json.loads('[{"outputs": [], "inputs": [{"type": "address", "name": "_beneficiary"}, {"type": "uint256", "name": "biddingtime"}], "stateMutability": "nonpayable", "type": "constructor"}, {"name": "bid", "outputs": [], "inputs": [], "stateMutability": "payable", "type": "function", "gas": 109861}, {"name": "withdraw", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 56184}, {"name": "endAuction", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 73631}, {"name": "beneficiary", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1241}, {"name": "auctionStart", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1271}, {"name": "auctionEnd", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1301}, {"name": "highestBidder", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1331}, {"name": "highestBid", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1361}, {"name": "ended", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1391}, {"name": "pendingReturns", "outputs": [{"type": "uint256", "name": ""}], "inputs": [{"type": "address", "name": "arg0"}], "stateMutability": "view", "type": "function", "gas": 1575}]')

contract = w3.eth.contract(address=address, abi=abi)

nonce = w3.eth.getTransactionCount(w3.eth.defaultAccount)
tx = {
    'nonce': nonce,
    'to': address,
    'value': w3.toWei('22', 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei')
}

# Bid
# contract.functions.bid().transact(tx)

# Withdraw
# contract.functions.withdraw().transact()

# End Auction
contract.functions.endAuction().transact()


# Get Balance
print(f'Current contract balance: {w3.fromWei(w3.eth.getBalance(address), "ether")}ETH')

