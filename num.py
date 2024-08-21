from abc import ABC, abstractmethod

from methods import extension
from models.double import Pointed
from models.integer import Integer


class Num(ABC, Integer, Pointed):
    @extension
    @abstractmethod
    def is_eligible_age_to_vote(self) -> bool:
        return self >= 18
