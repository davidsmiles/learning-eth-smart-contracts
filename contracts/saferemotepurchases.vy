# Safe Remote Purchase Contract

value: public(uint256)
seller: public(address)
buyer: public(address)

unlocked: public(bool)
ended: public(bool)


# The seller initializes the contract by posting a safety deposit
# of 2*value of the item up for sale
@payable
@external
def __init__():
    assert msg.value % 2 == 0
    self.value = msg.value / 2
    self.seller = msg.sender

    self.unlocked = True


# Only a seller can refund his deposit before any buyer  makes
# a purchase
@external
def abort():
    assert self.unlocked, 'buyer already made purchase'
    assert msg.sender == self.seller, 'only seller can abort'
    selfdestruct(self.seller)


# Is the item still open? Buyer calls this function to make a
# purchase for item and deposits twice the item's value
@payable
@external
def purchase():
    assert msg.sender != self.seller
    assert self.unlocked, 'item is still up for sale!'
    assert msg.value == self.value * 2

    self.buyer = msg.sender
    self.unlocked = False


# Buyer confirms receiving the item, buyer's deposit is returned (value)
# Seller's deposit (2 * value) + item's value is returned.
@external
def received():
    # Conditions
    assert not self.unlocked
    assert msg.sender == self.buyer

    self.ended = True
    
    send(self.buyer, self.value)
    selfdestruct(self.seller)

