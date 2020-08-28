# O/1 Knapsack Problem #

bag_limit = 7
val = [2,2,4,5,3]
weight = [3,1,3,4,2]

knapsack = [[0 for x in range(bag_limit+1)] for x in range(len(val)+1)]

for row in range(len(val) + 1):
    for col in range(bag_limit + 1):
        if row == 0 or col == 0:
            knapsack[row][col] = 0
        elif weight[row-1] <= col: # has to be row-1 because of first row thats all zeros, else you'd get out of range
            knapsack[row][col] = max(knapsack[row-1][col], val[row-1] + knapsack[row-1][col-weight[row-1]])
        else:
            knapsack[row][col] = knapsack[row-1][col]


# Set-Cover Problem #

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])

stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set() # keep track of what states are covered
    for station, states_for_station in stations.items():

        covered = states_needed & states_for_station
        if len(covered) > len(states_covered): # which station left covers the most states
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
