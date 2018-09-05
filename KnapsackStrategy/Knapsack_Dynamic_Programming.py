from KnapsackStrategy import KnapsackStrategy_Base

class Knapsack_Dynamic_Programming_Strategy(KnapsackStrategy_Base.KnapsackStrategy):
    matrix = []

    ## Apply a dynamic programming approach to solve the knapsack
    def solve_knapsack(self):
        if(self.matrix == []):
            self.createMatrix()
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])

        for col in range(1, ncols):
            for row in range(1, nrows):
                itemWeight = self._knapsack.items[col-1].weight
                itemValue = self._knapsack.items[col-1].value
                actualCapacity = row

                if(itemWeight <= actualCapacity):
                    self.matrix[row][col] = max(self.matrix[row][col-1], itemValue + self.matrix[row-itemWeight][col-1])
                else:
                    self.matrix[row][col] = self.matrix[row][col-1]
        
        self.setKnapsackValue()
        self.traceBack()

    ## Set the knapsack's value
    def setKnapsackValue(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])       

        self._knapsack.value = self.matrix[nrows-1][ncols-1]

    ## Start the matrix for the Dynamic Programming algorithm
    def createMatrix(self):
        self.matrix = [0] * (self._knapsack.capacity + 1)
        for i in range(self._knapsack.capacity + 1):
            self.matrix[i] = [0] * (len(self._knapsack.items) + 1)

    ## Traceback the matrix for computing the knapsack's chosen items
    def traceBack(self):
        if(self._knapsack.chosenItems == []):
            self._knapsack.createChosenItemsArray()
        
        row = len(self.matrix) - 1
        col = len(self.matrix[0]) - 1

        for i in range(len(self.matrix[0]) - 1):
            value = self.matrix[row][col]
            prevValue = self.matrix[row][col - 1]

            if(value != prevValue):
                self._knapsack.chosenItems[col - 1] = 1
                row = row - self._knapsack.items[col - 1].weight

            col = col - 1  

    ## Print matrix in prompt
    def printMatrix(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])

        for i in range(nrows):
            for j in range(ncols):
                print(str(self.matrix[i][j]) + " ", end="")
            print()

    ## Print traceback in prompt
    def prinTraceBack(self):
        self.traceBack()

        for i in range(len(self._knapsack.chosenItems)):
            print(str(self._knapsack.chosenItems[i]) + " ", end = "")
        print()