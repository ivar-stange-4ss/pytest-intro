import warnings

class Person:
    def __init__(self, firstname, lastname, age):
        self._firstname = firstname
        self._lastname = lastname
        self._age = age
        self._inventory = []
        self._account = 1000.0

    @property
    def fullname(self):
        return f"{self._firstname} {self._lastname}"

    def buy(self, item, price):
        if self._account < price:
            warnings.warn("Insufficient funds!")
        else:
            self._inventory.append(item)
            self._account -= price

    def sell(self, item, price):
        self._inventory.remove(item)
        self._account += price
