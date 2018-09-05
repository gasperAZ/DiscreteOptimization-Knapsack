from abc import ABC, abstractmethod
from Knapsack import Knapsack, KnapsackItem

class KnapsackStrategy(ABC):

    def __init__(self, _knapsack):
        self._knapsack = _knapsack
        super().__init__()

    @abstractmethod
    def solve_knapsack(self):
        """Required Method"""

