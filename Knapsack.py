from collections import namedtuple
KnapsackItem = namedtuple("KnapsackItem", ['index', 'value', 'weight'])

class Knapsack:
    items = []
    capacity = 0
    itemsCount = 0
    matrix = []
    chosenItems = []
    value = 0

    def __init__(self):
        self.items = []
        self.capacity = 0
        self.itemsCount = 0
        self.matrix = []
        self.chosenItems = []
        self.value = 0

    def createChosenItemsArray(self):
        self.chosenItems = [0] * self.itemsCount



    ##DONE
    def createMatrix(self):
        self.matrix = [0] * (self.capacity + 1)
        for i in range(self.capacity + 1):
            self.matrix[i] = [0] * (len(self.items) + 1)

    
    ##DONE
    def solveKnapsack(self):
        if(self.matrix == []):
            self.createMatrix()
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])

        for col in range(1, ncols):
            for row in range(1, nrows):
                itemWeight = self.items[col-1].weight
                itemValue = self.items[col-1].value
                actualCapacity = row

                if(itemWeight <= actualCapacity):
                    self.matrix[row][col] = max(self.matrix[row][col-1], itemValue + self.matrix[row-itemWeight][col-1])
                else:
                    self.matrix[row][col] = self.matrix[row][col-1]
        
        self.setValue()

    def setValue(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])       

        self.value = self.matrix[nrows-1][ncols-1]

    def getValue(self):
        return self.value

        #nrows = len(self.matrix)
        #ncols = len(self.matrix[0])       

        #return self.matrix[nrows-1][ncols-1]

    ##DONE
    def printMatrix(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])

        for i in range(nrows):
            for j in range(ncols):
                print(str(self.matrix[i][j]) + " ", end="")
            print()

    ##DONE
    def traceBack(self):
        if(self.chosenItems == []):
            self.createChosenItemsArray()
        
        row = len(self.matrix) - 1
        col = len(self.matrix[0]) - 1

        for i in range(len(self.matrix[0]) - 1):
            value = self.matrix[row][col]
            prevValue = self.matrix[row][col - 1]

            if(value != prevValue):
                self.chosenItems[col - 1] = 1
                row = row - self.items[col - 1].weight

            col = col - 1    

    ##DONE
    def prinTraceBack(self):
        self.traceBack()

        for i in range(len(self.chosenItems)):
            print(str(self.chosenItems[i]) + " ", end = "")
        print()