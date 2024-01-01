graph = {
    'S' : ['D','P','E'],
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
queue = []
def bfs(visited, graph, start, end):
    visited.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        if s == end:
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

def pathbfs( graph, start, end):
    visited = []
    queue = []
    
    queue.append([start])
    while queue:
        path = queue.pop(0)     
        node = path[-1]
        visited.append(node)
        if node == end:
            return path
        for neighbour in graph.get(node,[]):
            if neighbour not in visited:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

print("Cac dinh da duyet theo BFS: ")
bfs(visited, graph, 'S', 'G') 
print(end='\n')

print("Duong di da duyet theo BFS: ")
print(pathbfs( graph, 'S', 'G'))
