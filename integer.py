from abc import ABC, abstractmethod
from decimal import Decimal

from methods import extension


class Integer(ABC, int):
    @extension
    @abstractmethod
    def radians(self):
        pi = Decimal(11)
        st = Decimal(630)
        return (self * pi) / st
