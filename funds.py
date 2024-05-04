import support
# Take the user's bets as an array so we can pass back both what the bet was and the changed funds
def takeBets(_inCash):
    _bet = [0, 0]
    while _bet[0] <= 0:
        try:
            support.print_paragraphs(f"You have: ${_inCash}", "%", 32, "box")
            _bet[0] = int(input("Enter your bet: "))
        except:
            print("Please enter a valid number.")
            _bet[0] = 0
        if _bet[0] > _inCash:
            print("You don't have enough money to bet that much.")
            _bet[0] = 0
    _bet[1] = edit(_bet[0],_inCash, "sub")
    return _bet
# Set starting cash or reset cash if needed
def set(_debug):
    if _debug == True:
        _outCash = 1000
    else:
        _outCash = 100
    return _outCash
# Edit our cash
def edit(_inCash, _userCash, _op):
    if _op == "add":
        _outCash = _inCash + _userCash
        support.print_paragraphs(f"${_inCash} was added to your funds. You have ${_userCash} now.", "%", 32, "box")
    if _op == "sub":
        _outCash = _userCash - _inCash
        support.print_paragraphs(f"${_inCash} was deducted from your funds. You have ${_userCash} now.", "%", 32, "box")
    return _outCash