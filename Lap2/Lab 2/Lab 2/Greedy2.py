from collections import deque

class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list,heuristic):
        self.adjacency_list = adjacency_list
        self.h = heuristic

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes


    def greedy_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}
        count = 1
        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node
        
        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or self.h[v] < self.h[n]:
                    n = v
            if n == None:
                print('Path does not exist!')
                return None
        
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                print('Nodes', count)
                reconst_path.append(start_node)
                reconst_path.reverse()
                
                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                    count +=1

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)
        print('Path does not exist!')
        return None
    
adj_list1 = {
    'S': [('A', 2), ('B', 1), ('F', 3)],
    'A': [('C', 2), ('D', 3)],
    'B': [('D', 2), ('E', 4)],
    'F': [('G', 6)],
    'C': [('G', 4)],
    'D': [('G', 4)],
    'E': [],
    'G': []
    }
heuristic1 = {
    'S': 6,
    'A': 4,
    'B': 5,
    'C': 2,
    'D': 2,
    'E': 8,
    'F': 4,
    'G': 0
    }
adj_list2 = {
    'S': [('F', 1), ('H', 1)],
    'F': [('S', 1), ('P', 1)],
    'H': [('S', 1), ('K', 1)],
    'P': [('F', 1), ('Q', 1)],
    'K': [('H', 1), ('C', 1)],
    'Q': [('P', 1), ('R', 1)],
    'C': [('K', 1), ('A', 1)],
    'R': [('Q', 1), ('T', 1)],
    'A': [('C', 1), ('B', 1)],
    'T': [('R', 1), ('G', 1)],
    'B': [('A', 1), ('D', 1)],
    'E': [('D', 1), ('N', 1)],
    'D': [('B', 1), ('E', 1), ('M', 1)],
    'M': [('D', 1), ('N', 1), ('G', 1)],
    'N': [('E', 1), ('M', 1)],
    'G': [('M', 1), ('T', 1)]
    }
heuristic2 = {
    'S': 4,
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 3,
    'F': 5,
    'G': 0,
    'H': 3,
    'K': 2,
    'M': 1,
    'N': 2,
    'P': 4,
    'Q': 3,
    'R': 2,
    'T': 1
    }
adj_list3 = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 1), ('D', 5)],  
    'C': [('A', 4), ('B', 1), ('D', 3)],
    'D': [('B', 5), ('C', 3), ('E', 8), ('F', 3), ('G', 9)],
    'E': [('D', 8), ('G', 2)],
    'F': [('D', 3), ('G', 5)],
    'G': [('E', 2), ('D', 9), ('F', 5)]
    }
heuristic3 = {
    'A': 9.5,
    'B': 9,
    'C': 8,
    'D': 7,
    'E': 1.5,
    'F': 4,
    'G': 0
    }
heuristic4 = {
    'A': 10,
    'B': 12,
    'C': 10,
    'D': 8,
    'E': 1,
    'F': 4.5,
    'G': 0
    }
adj_list4 = {
    'A': [('Z', 75), ('T', 118), ('S', 140)],
    'Z': [('A', 75), ('O', 71)],
    'T': [('A', 118), ('L', 111)],
    'O': [('Z', 71), ('S', 151)],
    'S': [('A', 140), ('O', 151), ('F', 99), ('R', 80)],
    'L': [('T', 111), ('M', 70)],
    'M': [('L', 70), ('D', 75)],
    'D': [('M', 75), ('C', 120)],
    'F': [('S', 99), ('B', 211)],
    'R': [('S', 80), ('P', 97), ('C', 146)],
    'C': [('D', 120), ('P', 138), ('R', 146)],
    'P': [('R', 97), ('C', 138), ('B', 101)],
    'B': [('F', 211), ('P', 101), ('G', 90), ('U', 85)],
    'G': [('B', 90)],
    'U': [('B', 85), ('H', 98), ('V', 142)],
    'H': [('U', 98), ('E', 86)],
    'E': [('H', 86)],
    'V': [('U', 142), ('I', 92)],
    'I': [('V', 92), ('N', 87)],
    'N': [('I', 87)]
    }
heuristic5 = {
    'A': 366,
    'B': 0,
    'C': 160,
    'D': 242,
    'E': 161,
    'F': 178,
    'G': 77,
    'H': 151,
    'I': 226,
    'L': 244,
    'M': 241,
    'N': 234,
    'O': 380,
    'P': 98,
    'R': 193,
    'S': 253,
    'T': 329,
    'U': 80,
    'V': 199,
    'Z': 374
    }
graph1 = Graph(adj_list1,heuristic1)
graph1.greedy_algorithm('S', 'G')

graph2 = Graph(adj_list2,heuristic2)
graph2.greedy_algorithm('S', 'G')
graph3 = Graph(adj_list3,heuristic3)
graph3.greedy_algorithm('A', 'G')
graph4 = Graph(adj_list3,heuristic4)
graph4.greedy_algorithm('A', 'G')
graph5 = Graph(adj_list4,heuristic5)
graph5.greedy_algorithm('A', 'B')
