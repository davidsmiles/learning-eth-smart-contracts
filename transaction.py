import json
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv('.env')
infura_url = os.environ.get('INFURA_URL')
ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))


# transaction
receiver = '0x60738cAD8b84814BDbE9940733B2F2325eAab215'
sender = '0x5D3921Ca070d488DdC952173b1df560A61aEd547'
sender_pk = '2ed13170c727e8cc080e2eccdc3dfeba276715b96030307bf6108a26ac4f8884'

web3.eth.defaultAccount = web3.eth.defaultAccount
nonce = web3.eth.getTransactionCount(web3.eth.accounts[0])
tx = {
    'nonce': nonce,
    'to': receiver,
    'value': web3.toWei('2', 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# # sign account if default account is not set
# signed_tx = web3.eth.account.signTransaction(tx, sender_pk)
# web3.eth.sendRawTransaction(signed_tx.rawTransaction)

# if default account is set
web3.eth.defaultAccount = web3.eth.accounts[0]
web3.eth.sendTransaction(tx)
