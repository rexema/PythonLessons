from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calc(self):
        pass


class Coat(Clothes):
    @property
    def calc(self):
        return round((self.param / 6.5) + 0.5)


class Suit(Clothes):
    @property
    def calc(self):
        return round((2 * self.param) + 0.3)


coat = Coat(42)
print(coat.calc)
suit = Suit(160)
print(suit.calc)
