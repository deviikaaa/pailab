# A* Algorithm

def a_star(start, goal, graph):
    open_set = {start}
    closed_set = set()
    g = {start: 0}
    parents = {start: start}

    while open_set:
        current = min(open_set, key=lambda x: g[x] + heuristic(x))
        
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in graph.get(current, []):
            if neighbor in closed_set:
                continue
            tentative_g = g[current] + weight
            if neighbor not in open_set or tentative_g < g.get(neighbor, float('inf')):
                open_set.add(neighbor)
                parents[neighbor] = current
                g[neighbor] = tentative_g
                
    return None

def heuristic(n):
    H_dist = {'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
    return H_dist.get(n, float('inf'))

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'D': [('G', 1)],
    'E': [('D', 6)]
}

print("Path found:", a_star('A', 'G', graph))


# Alpha-Beta Pruning

def minimax(nodeIndex, depth, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = minimax(nodeIndex * 2 + i, depth + 1, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = minimax(nodeIndex * 2 + i, depth + 1, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [10, 9, 14, 18, 5, 4, 50, 3]
print("The optimal value is:", minimax(0, 0, True, values, float('-inf'), float('inf')))
