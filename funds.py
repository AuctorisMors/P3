import support
# Keep all money calc and value here
_amount = 0
# Set starting cash or reset cash if needed
def set(_int):
    global _amount
    _amount = int(_int)
# How much money do we have?
def get():
    global _amount
    return _amount
# Take the user's bets as an array so we can pass back both what the bet was and the changed funds// relic code
def takeBets():
    global _amount
    _bet = 0
    while _bet <= 0:
        try:
            support.print_paragraphs(f"You have: ${_amount}", "%", 32, "box")
            _bet = int(input("Enter your bet: "))
        except:
            print("Please enter a valid number.")
            _bet = 0
        if _bet > _amount:
            print("You don't have enough money to bet that much.")
            _bet = 0
    edit(_bet, "sub")
    return _bet
# Edit our cash
def edit(_inCash, _op):
    global _amount
    if _op == "add":
        _outCash = _inCash + _amount
        support.print_paragraphs(f"${_inCash} was added to your funds. You have ${_outCash} now.", "%", 32, "box")
    if _op == "sub":
        _outCash = _amount - _inCash
        support.print_paragraphs(f"${_inCash} was deducted from your funds. You have ${_outCash} now.", "%", 32, "box")
    _amount = _outCash