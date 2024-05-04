import support
# Keep all money calc and value here
_userCash = 0
# How much money do we have?
def get():
    return _userCash
# Set starting cash or reset cash if needed
def set(_int):
    _userCash = _int
# Take the user's bets as an array so we can pass back both what the bet was and the changed funds// relic code
def takeBets():
    _bet = 0
    while _bet <= 0:
        try:
            support.print_paragraphs(f"You have: ${_userCash}", "%", 32, "box")
            _bet = int(input("Enter your bet: "))
        except:
            print("Please enter a valid number.")
            _bet = 0
        if _bet > _userCash:
            print("You don't have enough money to bet that much.")
            _bet = 0
    edit(_bet, "sub")
    return _bet
# Edit our cash
def edit(_inCash, _op):
    if _op == "add":
        _outCash = _inCash + _userCash
        support.print_paragraphs(f"${_inCash} was added to your funds. You have ${_outCash} now.", "%", 32, "box")
    if _op == "sub":
        _outCash = _userCash - _inCash
        support.print_paragraphs(f"${_inCash} was deducted from your funds. You have ${_outCash} now.", "%", 32, "box")
    _userCash = _outCash