from KnapsackStrategy import KnapsackStrategy_Base, Knapsack_Dynamic_Programming, Knapsack_greedy_algorithm

class KnapsackSolver:
    _knapsack = 0

    def __init__(self, _knapsack):
        self._knapsack = _knapsack

    def Solve(self):
        strategy = 0
        itemsCount = self._knapsack.itemsCount
        capacity = self._knapsack.capacity

        maxMatrixSize = 536870912 ##for 32 bits systems 2^32 / 8 = max array size
        ## 1073741824 for 64 bits systems

        estimatedMatrixSize = itemsCount * capacity

        if(itemsCount <= 1000 and estimatedMatrixSize < maxMatrixSize):
            strategy = Knapsack_Dynamic_Programming.Knapsack_Dynamic_Programming_Strategy(self._knapsack)
        # elif (itemsCount > 1000):
        else:
            strategy = Knapsack_greedy_algorithm.Knapsack_Greedy_Algorithm_Strategy(self._knapsack)
        
        strategy.solve_knapsack()

        return "Knapsack has been solved!!!"