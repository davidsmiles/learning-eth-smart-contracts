import json
import os
from dotenv import load_dotenv
from web3 import Web3

load_dotenv('.env')
infura_url = os.environ.get('INFURA_URL')
ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))


# # latest block number
print(web3.eth.blockNumber)

# transaction
receiver = '0xEa4E792A1ac8C55c4d0171dB28Bda0c5E92586dD'
sender = '0xc2d78Fa063B3357964442b3fc3E6F095501B6150'
sender_pk = 'd5f02c4f726619da2c32bef51e88c1eb4652b24a7d39930eb69ffcf3549d8c03'

nonce = web3.eth.getTransactionCount(sender)
tx = {
    'nonce': nonce,
    'to': receiver,
    'value': web3.toWei('2', 'ether'),
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}

# sign account
signed_tx = web3.eth.account.signTransaction(tx, sender_pk)
# get hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))
