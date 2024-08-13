'''
Instructions
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE


Using the code above, implement the relevant methods and dunder methods which will output the results below.
Hint : When adding 2 currencies which don’t share the same label you should raise an error.
>>> c1 = Currency('dollar', 5)
>>> c2 = Currency('dollar', 10)
>>> c3 = Currency('shekel', 1)
>>> c4 = Currency('shekel', 10)

>>> str(c1)
'5 dollars'

>>> int(c1)
5

>>> repr(c1)
'5 dollars'

>>> c1 + 5
10

>>> c1 + c2
15

>>> c1 
5 dollars

>>> c1 += 5
>>> c1
10 dollars

>>> c1 += c2
>>> c1
20 dollars

>>> c1 + c3
TypeError: Cannot add between Currency type <dollar> and <shekel>
'''

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        currency_label = self.currency if self.amount == 1 else self.currency + 's' # just a way to add "s" at the end of the currency name
        return f'{self.amount} {currency_label}'

    def __repr__(self):
        return self.__str__() # we want this to return the same thing as __str__

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency): # if we add 2 instances of Currency
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
        elif isinstance(other, (int, float)): # if we add int or float to instance of Currency
            return self.amount + other
        else:
            raise TypeError('Unsupported type for addition')

    def __iadd__(self, other): # handling +=
        if isinstance(other, Currency):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f'Cannot add between Currency type <{self.currency}> and <{other.currency}>')
        elif isinstance(other, (int, float)):
            self.amount += other
            return self
        else:
            raise TypeError('Unsupported type for in-place addition')

# Example usage
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollars'
print(int(c1))  # 5
print(repr(c1))  # '5 dollars'

print(c1 + 5)  # 10
print(c1 + c2)  # 15

print(c1)  # 5 dollars

c1 += 5
print(c1)  # 10 dollars

c1 += c2
print(c1)  # 20 dollars

# The following will raise a TypeError
try:
    print(c1 + c3)
except TypeError as e:
    print(e)  # Cannot add between Currency type <dollar> and <shekel>