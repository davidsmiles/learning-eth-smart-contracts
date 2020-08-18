# Open Auction

# Beneficiary receives money from the highest bidder
beneficiary: public(address)
auctionStart: public(uint256)
auctionEnd: public(uint256)

# Current state of auction
highestBidder: public(address)
highestBid: public(uint256)


# Set to True at the end
ended: bool

# Keeps track of refunded bids
pendingReturns: public(HashMap[address, uint256])


# Create a simple auction with 'bidding time'
# on behalf of the beneficiary address '_beneficiary'
@external
def __init__(_beneficiary: address, biddingtime: uint256):
    self.beneficiary = _beneficiary
    self.auctionStart = block.timestamp
    self.auctionEnd = self.auctionStart + biddingtime


# Bid on the auction with the value sent with the transaction
# This is money is refunded only when the bid is npot won
@payable
@external
def bid():
    # Check if bidding period is over
    assert block.timestamp < self.auctionStart, 'bidding time expired'

    # Check if bid is high enough
    assert msg.value >= self.highestBid, 'bid is lower than the current highest bid'

    # Track the refund for the previous high bidder
    self.pendingReturns[self.highestBidder] += self.highestBid

    # Track the new bid
    self.highestBidder = msg.sender
    self.highestBid = msg.value


# Withdraw a previously refunded bill
@external
def withdraw():
    pendingAmount: uint256 = self.pendingReturns[msg.sender]
    send(msg.sender, pendingAmount)
    self.pendingReturns[msg.sender] = 0


# End the Auction and send the highest bid
# to the Beneficiary
@external
def endAuction():
    # Check if auction endtime has been reached
    assert block.timestamp >= self.auctionEnd

    # Check if this function has been called already
    assert not self.ended

    self.ended = True

    # Send highest big to beneficiary
    send(msg.sender, self.highestBid)
