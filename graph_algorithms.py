# Dijkstra's Algorithm #

graph = {}
costs = {}
parents = {}

###### GRAPH ######

graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['finish'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['finish'] = 5

graph['finish'] = {}

###### COSTS ######

costs['a'] = 6
costs['b'] = 2
costs['finish'] = float("inf")

###### PARENTS ######

parents['a'] = 'start'
parents['b'] = 'start'
parents['finish'] = ''


def find_lowest_cost_node(graph):
    lowest_cost = float('inf')
    node = None
    for key in costs.keys():
        if key not in visited:
            if costs[key] < lowest_cost:
                lowest_cost = costs[key]
                node = key
    return node

visited = []

node = find_lowest_cost_node(graph)
while node is not None:
    cost = costs[node] # cost of current node
    neighbors = graph[node] # neighbors of current node
    for n in neighbors.keys():
        new_cost = cost + neighbors[n] # cost of current node + neighbor
        if new_cost < costs[n]: # if new cost is less than known neighbor cost
            costs[n] = new_cost # change value of cost in costs
            parents[n] = node

    visited.append(node)
    node = find_lowest_cost_node(graph)


# Breadth First Search #

from collections import deque

graph = {}

graph['you'] = ['bob', 'claire', 'alice']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'johnny']
graph['anuj'] = []
graph['thom'] = []
graph['peggy'] = []
graph['jonny'] = []

def person_is_seller(name):
    return name[-1] == 'm'

def bfs(start):

    search_queue = deque()
    search_queue += start
    searched = []
    while search_queue:
        person = search_queue.popleft()

        if person_is_seller(person):
            return person + ' is a mango seller'
        else:
            search_queue.extend(graph[person])
            searched.append(person)
