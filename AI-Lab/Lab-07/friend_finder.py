network = {
    "Ali": ["Bilal", "Sara"],
    "Bilal": ["Ali", "Zara"],
    "Sara": ["Ali", "Omar"],
    "Zara": ["Bilal", "Hira"],
    "Omar": ["Sara"],
    "Hira": ["Zara"],
}

def bfs_shortest_path(graph, start, goal):
    visited = [start]
    queue = [[start]] 
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node == goal:
            return path
            
        if node in graph:
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(path + [neighbour])
    return None

start = "Ali"
goal = "Hira"
path = bfs_shortest_path(network, start, goal)

if path:
    print("Shortest chain from start to goal:", path)
    print("Number of introductions needed:", len(path) - 1)
else:
    print("No connection found")
