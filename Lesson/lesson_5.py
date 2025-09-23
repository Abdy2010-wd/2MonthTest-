# Dunder methods - magic methods double underscore
class Money:
    def _init__(self, amount=0):
        self.amount = amount

def _str_(self):
    return f"экземпляр Money:{self.amount}"
def __str__(self, other):
    return Money{self. mount + other money)
def __mul__(self, other):
    pass
def _eq__(self, other):
    return self.amount == other.amount
 #gt - greater than - self > other
# ge - greatre than or equal: self > other
# lt - less than: self < other
# le - less thna or equal: self < other
    def gt (self, other):
        if self.amount > other.amount
            return True
        else:
            return False



igor_money = Money(100)
print(igor_money)
adilet_money = Money(250)
total_money = igor_money + adilet_money
print(total_money)


