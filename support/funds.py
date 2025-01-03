from support.text import Text

class Funds:
    def __init__(self, funds):
        self._amount = funds

    def set(self, _int):
        self._amount = int(_int)

    def get(self):
        return self._amount

    def bet(self):
        while True:
            try:
                Text.print(f"You have: ${self._amount}", "%", 32, "box")
                _bet = int(input("Enter your bet: "))
                if _bet > self._amount:
                    print("You don't have enough money to bet that much.")
                else:
                    self.edit(_bet, "sub")
                    return _bet
            except ValueError:
                print("Please enter a valid number.")

    def edit(self, _inCash, _op):
        if _op == "add":
            self._amount += _inCash
            Text.print(f"${_inCash} was added to your funds. You have ${self._amount} now.", "%", 32, "box")
        elif _op == "sub":
            self._amount -= _inCash
            Text.print(f"${_inCash} was deducted from your funds. You have ${self._amount} now.", "%", 32, "box")