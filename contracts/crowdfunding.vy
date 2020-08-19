# Crowd Funding Contract

struct Funders:
    sender: address
    amount: uint256


beneficiary: public(address)
goal: public(uint256)
timelimit: public(uint256)
deadline: public(uint256)
ended: public(bool)

funders: public(Funders[100])
fundersCount: public(int128)
refundIndex: public(int128)


@external
def __init__(_beneficiary: address, _goal: uint256, _timelimit: uint256):
    self.beneficiary = _beneficiary
    self.goal = _goal
    self.deadline = block.timestamp + _timelimit


@payable
@external
def participate():
    assert block.timestamp < self.deadline, 'deadline reached'
    index: int128 = self.fundersCount
    self.funders[index] = Funders({
        sender: msg.sender, amount: msg.value
    })
    self.fundersCount += 1


@external
def refundAll():
    assert block.timestamp >= self.deadline and self.balance < self.goal, 'goal not acheived'

    assert not self.ended
    self.ended = True

    ind: int128 = self.refundIndex
    for i in range(ind, ind + 30):
        if i >= self.fundersCount:
            self.refundIndex = self.fundersCount
            return
        send(self.funders[i].sender, self.funders[i].amount)
        self.funders[i] = empty(Funders)
    
    self.refundIndex = ind + 30


@external
def finalize():
    assert block.timestamp >= self.deadline, 'deadline has not been met (yet)'
    assert self.balance >= self.goal, 'invalid balance'

    assert not self.ended
    self.ended = True

    selfdestruct(self.beneficiary)
