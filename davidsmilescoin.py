import json
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv('.env')
infura_url = os.environ.get('INFURA_URL')
ganache_url = "http://127.0.0.1:7545"

w3 = Web3(Web3.HTTPProvider(ganache_url))

w3.eth.defaultAccount = w3.eth.accounts[0]

address = w3.toChecksumAddress('0xE97DbCf8DF0f864Cf39d7C7a0A13d6787559882A')
abi = json.loads('[{"name": "Transfer", "inputs": [{"type": "address", "name": "sender", "indexed": true}, {"type": "address", "name": "receiver", "indexed": true}, {"type": "uint256", "name": "value", "indexed": false}], "anonymous": false, "type": "event"}, {"name": "Approval", "inputs": [{"type": "address", "name": "owner", "indexed": true}, {"type": "address", "name": "spender", "indexed": true}, {"type": "uint256", "name": "value", "indexed": false}], "anonymous": false, "type": "event"}, {"outputs": [], "inputs": [{"type": "address", "name": "_owner"}, {"type": "string", "name": "_name"}, {"type": "string", "name": "_symbol"}, {"type": "uint256", "name": "_decimals"}, {"type": "uint256", "name": "_initial_supply"}], "stateMutability": "nonpayable", "type": "constructor"}, {"name": "transfer", "outputs": [{"type": "bool", "name": ""}], "inputs": [{"type": "address", "name": "receiver"}, {"type": "uint256", "name": "_value"}], "stateMutability": "nonpayable", "type": "function", "gas": 76330}, {"name": "approve", "outputs": [{"type": "bool", "name": ""}], "inputs": [{"type": "address", "name": "spender"}, {"type": "uint256", "name": "_value"}], "stateMutability": "nonpayable", "type": "function", "gas": 37793}, {"name": "transferFrom", "outputs": [{"type": "bool", "name": ""}], "inputs": [{"type": "address", "name": "_from"}, {"type": "address", "name": "_to"}, {"type": "uint256", "name": "_value"}], "stateMutability": "nonpayable", "type": "function", "gas": 113773}, {"name": "owner", "outputs": [{"type": "address", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1271}, {"name": "name", "outputs": [{"type": "string", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 9657}, {"name": "symbol", "outputs": [{"type": "string", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 6756}, {"name": "decimals", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1361}, {"name": "totalSupply", "outputs": [{"type": "uint256", "name": ""}], "inputs": [], "stateMutability": "view", "type": "function", "gas": 1391}, {"name": "balanceOf", "outputs": [{"type": "uint256", "name": ""}], "inputs": [{"type": "address", "name": "arg0"}], "stateMutability": "view", "type": "function", "gas": 1575}, {"name": "allowance", "outputs": [{"type": "uint256", "name": ""}], "inputs": [{"type": "address", "name": "arg0"}, {"type": "address", "name": "arg1"}], "stateMutability": "view", "type": "function", "gas": 1759}]')
contract = w3.eth.contract(address=address, abi=abi)

print(contract.functions.transfer('0x5D3921Ca070d488DdC952173b1df560A61aEd547', 500).transact())

print(contract.functions.balanceOf('0x5D3921Ca070d488DdC952173b1df560A61aEd547').call())