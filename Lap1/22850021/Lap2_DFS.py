graph = {
    'S' : ['D','E','P'],
    'A' : [],
    'B' : ['A'],
    'C' : ['A'],
    'D' : ['B','C','E'],
    'E' : ['H','R'],
    'F' : ['C','G'],
    'H' : ['P','Q'],
    'P' : ['Q'],
    'Q' : [],
    'R' : ['F'],
    'G' : []
}
visited = []
stack = []
def dfs(visited, graph, start, end):
    visited.append(start)
    stack.append(start)
    while stack:
        s = stack.pop()
        print(s, end = " ")
        if s == end:
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)
print("Cac dinh da duyet theo DFS: ")
dfs(visited, graph,'S','G')
print(end='\n')

def dfs( graph, start, end):
    visited = []
    stack = []
    
    stack.append([start])
    while stack:
        path = stack.pop()
        node = path[-1]
        visited.append(node)
        if node == end:
            return path
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
print("Duong di da duyet theo DFS: ")
print(dfs(graph,'S','G'))
