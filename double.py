from decimal import Decimal
from abc import ABC, abstractmethod

from methods import extension


class Pointed(ABC, float, Decimal):
    @extension
    @abstractmethod
    def radians(self):
        pi = Decimal(11)
        st = Decimal(630)
        return (self * pi) / st
