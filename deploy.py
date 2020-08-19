import json
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]


def deploycontract(w3, _abi, _bytecode, tx = None, *args):
    contract = w3.eth.contract(abi=_abi, bytecode=_bytecode)
    txhash = contract.constructor(*args).transact(tx)
    return w3.eth.getTransactionReceipt(txhash)


abi = json.loads('[{"outputs": [], "inputs": [], "stateMutability": "payable", "type": "constructor"}, {"name": "abort", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 28014}, {"name": "purchase", "outputs": [], "inputs": [], "stateMutability": "payable", "type": "function", "gas": 58217}, {"name": "received", "outputs": [], "inputs": [], "stateMutability": "nonpayable", "type": "function", "gas": 99365}, {"name": "value", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1241}, {"name": "seller", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1271}, {"name": "buyer", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1301}, {"name": "unlocked", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1331}, {"name": "ended", "outputs": [{"type": "bool", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1361}]')
bytecode = "0x740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a052346002808061009b57600080fd5b820690509050156100ab57600080fd5b34600280806100b957600080fd5b8204905090506000553360015560016003556103eb56600436101561000d57610315565b600035601c52740100000000000000000000000000000000000000006020526f7fffffffffffffffffffffffffffffff6040527fffffffffffffffffffffffffffffffff8000000000000000000000000000000060605274012a05f1fffffffffffffffffffffffffdabf41c006080527ffffffffffffffffffffffffed5fa0e000000000000000000000000000000000060a0526335a063b4600051141561015a5734156100ba57600080fd5b6308c379a061014052602061016052601b610180527f627579657220616c7265616479206d61646520707572636861736500000000006101a0526101805060035461010657606461015cfd5b6308c379a06101e0526020610200526015610220527f6f6e6c792073656c6c65722063616e2061626f72740000000000000000000000610240526102205060015433146101545760646101fcfd5b600154ff005b6364edfbf060005114156101f857600154331861017657600080fd5b6308c379a061014052602061016052601a610180527f6974656d206973207374696c6c20757020666f722073616c65210000000000006101a052610180506003546101c257606461015cfd5b600054600280820282158284830414176101db57600080fd5b8090509050905034146101ed57600080fd5b336002556000600355005b6383a6deb5600051141561025157341561021157600080fd5b6003541561021e57600080fd5b600254331461022c57600080fd5b600160045560006000600060006000546002546000f161024b57600080fd5b600154ff005b633fa4f245600051141561027857341561026a57600080fd5b60005460005260206000f350005b6308551a53600051141561029f57341561029157600080fd5b60015460005260206000f350005b637150d8ae60005114156102c65734156102b857600080fd5b60025460005260206000f350005b636a5e265060005114156102ed5734156102df57600080fd5b60035460005260206000f350005b6312fa6feb600051141561031457341561030657600080fd5b60045460005260206000f350005b5b60006000fd5b6100d06103eb036100d06000396100d06103eb036000f3"

tx = {
    'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount),
    'value': web3.toWei('40', 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
receipt = deploycontract(web3, abi, bytecode, tx)
print(f'Deployed successfully on {receipt.contractAddress}')


