# 0/1 Knapsack Problem #

def knapsack(bag_limit, val, weight):

    knapsack = [[0 for x in range(bag_limit+1)] for x in range(len(val)+1)]

    for row in range(len(val) + 1):
        for col in range(bag_limit + 1):
            if row == 0 or col == 0:
                knapsack[row][col] = 0
            elif weight[row-1] <= col:
                knapsack[row][col] = max(knapsack[row-1][col], val[row-1] + knapsack[row-1][col-weight[row-1]])
            else:
                knapsack[row][col] = knapsack[row-1][col]


    total = bag_limit
    row = len(val)
    col = bag_limit
    loop = 1
    items = []

    while bag_limit > 0:
        if knapsack[row][col] != knapsack[row-1][col]:
            items.append(str(row))
            row -=1
            col = col - weight[row]
            bag_limit -= weight[row]
        else:
            row-=1

    print('You should place items ' + ', '.join(items) + ' in your knapsack for the highest value under ' + str(bag_limit) + ' lbs.' )

    return knapsack

knapsack(bag_limit = 7, val = [2,2,4,5,3], weight = [3,1,3,4,2])


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
