#!/usr/bin/python
# -*- coding: utf-8 -*-
# from operator import attrgetter
from collections import namedtuple
KnapsackItem = namedtuple("KnapsackItem", ['index', 'value', 'weight'])

class Knapsack:
    items = []
    capacity = 0
    itemsCount = 0
    matrix = []
    chosenItems = []

    def __init__(self):
        self.items = []
        self.capacity = 0
        self.itemsCount = 0
        self.matrix = []
        self.chosenItems = []

    def createMatrix(self):
        self.matrix = [0] * (self.capacity + 1)
        for i in range(self.capacity + 1):
            self.matrix[i] = [0] * (len(self.items) + 1)

    def createChosenItemsArray(self):
        self.chosenItems = [0] * self.itemsCount

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

    def getValue(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])       

        return self.matrix[nrows-1][ncols-1]

    def printMatrix(self):
        nrows = len(self.matrix)
        ncols = len(self.matrix[0])

        for i in range(nrows):
            for j in range(ncols):
                print(str(self.matrix[i][j]) + " ", end="")
            print()

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

    def prinTraceBack(self):
        self.traceBack()

        for i in range(len(self.chosenItems)):
            print(str(self.chosenItems[i]) + " ", end = "")
        print()

def readItems(input_data, _knapsack):

    # store all the file lines
    lines = input_data.split('\n')

    # The first line contains the number of items and the knapsack capacity
    firstLine = lines[0].split()
    _knapsack.itemsCount = int(firstLine[0])
    _knapsack.capacity = int(firstLine[1])

    for i in range(1, _knapsack.itemsCount + 1):
        line = lines[i]
        # each line contains an object with the format "value" and "weight"
        knapsackObject = line.split()
        _knapsack.items.append(KnapsackItem(i-1, int(knapsackObject[0]), int(knapsackObject[1])))

    # _knapsack.items = sorted(_knapsack.items, key=attrgetter('weight'))

def solve_it(input_data):

    _knapsack = Knapsack()

    readItems(input_data, _knapsack)
    _knapsack.solveKnapsack()
    _knapsack.traceBack()

    output_data = str(_knapsack.getValue()) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, _knapsack.chosenItems))

    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

