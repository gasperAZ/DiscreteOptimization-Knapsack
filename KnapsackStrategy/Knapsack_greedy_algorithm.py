from KnapsackStrategy import KnapsackStrategy_Base

class Knapsack_Greedy_Algorithm_Strategy(KnapsackStrategy_Base.KnapsackStrategy):
    
    ## Apply a dynamic programming approach to solve the knapsack
    def solve_knapsack(self):
        if(self._knapsack.chosenItems == []):
            self._knapsack.createChosenItemsArray()
        
        value = 0
        weight = 0

        for item in self._knapsack.items:
            if weight + item.weight <= self._knapsack.capacity:
                self._knapsack.chosenItems[item.index] = 1
                value += item.value
                weight += item.weight
        
        ## Set the knapsack's final value
        self._knapsack.value = value