import support
class Funds:
    def __init__(self, funds):
        self._amount = funds
    # Set starting cash or reset cash if needed
    def set(self, _int):
        self._amount = int(_int)
    # How much money do we have?
    def get(self):
        return self._amount
    # Take the user's bets as an array so we can pass back both what the bet was and the changed funds// relic code
    def bet(self):
        _bet = 0
        while _bet <= 0:
            try:
                support.print_paragraphs(f"You have: ${self._amount}", "%", 32, "box")
                _bet = int(input("Enter your bet: "))
            except:
                print("Please enter a valid number.")
                _bet = 0
            if _bet > self._amount:
                print("You don't have enough money to bet that much.")
                _bet = 0
        Funds.edit(self, _bet, "sub")
        return _bet
    # Edit our cash
    def edit(self, _inCash, _op):
        if _op == "add":
            _outCash = _inCash + self._amount
            support.print_paragraphs(f"${_inCash} was added to your funds. You have ${_outCash} now.", "%", 32, "box")
        if _op == "sub":
            _outCash = self._amount - _inCash
            support.print_paragraphs(f"${_inCash} was deducted from your funds. You have ${_outCash} now.", "%", 32, "box")
        self._amount = _outCash