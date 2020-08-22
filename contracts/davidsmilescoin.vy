"""
@title DavidSmilesCoin
@author David Smiles
@license No License
@notice 
    A Cryptocurrency with the name 'DavidSmilesCoin' and a currency symbol of 'DSC'
@dev
    Smart Contract written in Vyper to set up the functions for the DSC cryptocurrency
"""


event Transfer:
    sender: indexed(address)
    receiver: indexed(address)
    value: uint256


event Approval:
    owner: indexed(address)
    spender: indexed(address)
    value: uint256


owner: public(address)
name: public(String[100])
symbol: public(String[5])
decimals: public(uint256)
totalSupply: public(uint256)

balanceOf: public(HashMap[address, uint256])
allowance: public(HashMap[address, HashMap[address, uint256]])


# Initializes contract with initial supply tokens to the creator of the contract
@external
def __init__(_owner: address, _name: String[100], _symbol: String[5], _decimals: uint256, _initial_supply: uint256):
    self.owner = _owner
    self.name = _name
    self.symbol = _symbol
    self.balanceOf[msg.sender] = _initial_supply
    self.decimals = _decimals
    self.totalSupply = _initial_supply


# Send '_value' tokens to 'receiver` from your account
@internal
def _transfer(sender: address, receiver: address, _value: uint256):
    # You can only send as much as you have
    assert self.balanceOf[sender] >= _value

    self.balanceOf[sender] -= _value
    self.balanceOf[receiver] += _value

    log Transfer(sender, receiver, _value)


# Public function to allow access to '_transfer'
@external
def transfer(receiver: address, _value: uint256) -> bool:
    self._transfer(msg.sender, receiver, _value)
    return True


# Allows '_spender' to spend no more than `_value` tokens in your behalf
@external
def approve(spender: address, _value: uint256) -> bool:
    self.allowance[msg.sender][spender] = _value

    log Approval(msg.sender, spender, _value)
    return True


# Transfer tokens from other address
@external
def transferFrom(_from: address, _to: address, _value: uint256) -> bool:
    assert _value < self.allowance[_from][msg.sender]
    self.allowance[_from][msg.sender] -= _value
    self._transfer(_from, _to, _value)

    return True
