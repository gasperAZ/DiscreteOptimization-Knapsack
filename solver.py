#!/usr/bin/python
# -*- coding: utf-8 -*-

from Knapsack import Knapsack, KnapsackItem
from KnapsackStrategy import KnapsackSolver

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

    # _knapsack.solveKnapsack()
    # _knapsack.traceBack()
    Solver = KnapsackSolver.KnapsackSolver(_knapsack)
    Solver.Solve()

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

