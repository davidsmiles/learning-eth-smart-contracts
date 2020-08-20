"""
@title a Simulator for a Company Evaluation
@license TechyDavid Inc.
@author David Smiles
@notice 
    You can use this contract for only the most basic simulation
@dev 
    Smart Contract written in Vyper and mimicks a Company's Evaluation System
"""

# Initiate the variables for the company and it's own shares
company: public(address)
price: public(uint256)
totalStocks: public(uint256)

holdings: public(HashMap[address, uint256])


# Set up the company
@external
def __init__(_company: address, initial_price: uint256, _total_stocks: uint256):
    assert _total_stocks > 0
    assert initial_price > 0

    self.company = _company
    self.price = initial_price
    self.totalStocks = _total_stocks

    self.holdings[self.company] = self.totalStocks


# Find out how much stocks are available in the company
@internal
def _stockAvailable() -> uint256:
    return self.holdings[self.company]


# Public function to allow access to _stockAvailable
@external
def stockAvailable() -> uint256:
    return self._stockAvailable()


# Give some value to the company and get some stock in return
@payable
@external
def buyStock():
    # NOTE: full amount is given to the company, no fractional shares
    assert msg.value >= self.price
    buy_order: uint256 = msg.value / self.price

    # Check that there are enough shares to sell
    assert self.holdings[self.company] > buy_order

    self.holdings[self.company] -= buy_order
    self.holdings[msg.sender] += buy_order


# Find out how much stock any address (that's owned by someone) has.
@internal
def _getHolding(_stockholder: address) -> uint256:
    return self.holdings[_stockholder]

# Public function to allow access to getHolding
@external
def getHolding(_stockholder: address) -> uint256:
    return self._getHolding(_stockholder)


# Return the amount the company has on hand in cash
@external
def cash() -> uint256:
    return self.balance


# Give stock back to the company and get money back in ETH
@external
def sellStock(sell_order: uint256):
    assert sell_order > 0

    # You can only sell as much stock as you own
    assert self._getHolding(msg.sender) > sell_order
    stockvalue: uint256 = self.price * sell_order

    # Check that the company has enough money to purchase
    assert self.balance >= stockvalue

    # Sell the stock, send the proceeds to the user
    # and put the stock back on the market.
    self.holdings[msg.sender] -= sell_order
    self.holdings[self.company] += sell_order
    send(msg.sender, stockvalue)


# Transfer stock from one stockholder to another
@external
def transferStock(receiver: address, transfer_order: uint256):
    assert transfer_order > 0

    # You can only transfer as much stock as you own
    assert self._getHolding(msg.sender) > transfer_order

    # Debit the sender's stock and add to the receiver's address.
    self.holdings[msg.sender] -= transfer_order
    self.holdings[receiver] += transfer_order


# Allow the company to pay someone for services rendered.
@external
def payBill(vendor: address, amount: uint256):
    # Only the company can pay people
    assert msg.sender == self.company

    # Check that the company has enough money to pay
    assert self.balance >= amount

    send(vendor, amount)


# Return the amount in wei that a company has raised in stock offerings.
@internal
def _debt() -> uint256:
    return (self.totalStocks - self._stockAvailable()) * self.price


# Public function to allow access to _debt()
@external
def debt() -> uint256:
    return self._debt()


# Return the cash holdings minus the debt of the company
@external
def worth() -> uint256:
    return self.balance - self._debt()
