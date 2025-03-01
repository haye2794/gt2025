import numpy as np
import heapq

def create_graph():
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'L', 'M']
    num_nodes = len(nodes)
    node_to_index = {node: index for index, node in enumerate(nodes)}
    
    adj_matrix = [[float('inf')] * num_nodes for _ in range(num_nodes)]
    
    edges = [
        ('A', 'C', 1), ('A', 'B', 4),
        ('B', 'F', 3),
        ('C', 'D', 8), ('C', 'F', 7),
        ('D', 'H', 5),
        ('F', 'H', 1), ('F', 'E', 1),
        ('E', 'H', 2),
        ('H', 'G', 3), ('H', 'M', 7), ('H', 'L', 6),
        ('G', 'M', 4),
        ('M', 'L', 1),
        ('L', 'G', 4), ('L', 'E', 2)
    ]
    
    for x, y, weight in edges:
        i, j = node_to_index[x], node_to_index[y]
        adj_matrix[i][j] = weight
        adj_matrix[j][i] = weight
    
    return nodes, node_to_index, np.array(adj_matrix)

def print_adjacency_matrix(adj_matrix):
    print("Adjacency Matrix for Undirected and Weighted graph:")
    for row in adj_matrix:
        print([" inf" if x == float('inf') else f"{int(x):4d}" for x in row])

def dijkstra(adj_matrix, node_to_index, source, target):
    num_nodes = len(adj_matrix)
    source_idx = node_to_index[source]
    target_idx = node_to_index[target]
    
    distances = [float('inf')] * num_nodes
    distances[source_idx] = 0
    prev = [None] * num_nodes
    pq = [(0, source_idx)]
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_dist > distances[current_node]:
            continue
        
        for neighbor in range(num_nodes):
            weight = adj_matrix[current_node][neighbor]
            if weight != float('inf'):
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    prev[neighbor] = current_node
                    heapq.heappush(pq, (new_dist, neighbor))
    
    path = []
    current = target_idx
    while current is not None:
        path.append(list(node_to_index.keys())[list(node_to_index.values()).index(current)])
        current = prev[current]
    path.reverse()
    
    return path, distances[target_idx]

def main():
    nodes, node_to_index, adj_matrix = create_graph()
    print_adjacency_matrix(adj_matrix)
    
    source = input("Enter the source node (A-M): ").strip().upper()
    target = input("Enter the target node (A-M): ").strip().upper()
    
    if source in node_to_index and target in node_to_index:
        shortest_path, total_weight = dijkstra(adj_matrix, node_to_index, source, target)
        print(f"Shortest path from {source} to {target}: {' -> '.join(shortest_path)}")
        print(f"Weighted sum of the shortest path: {total_weight}")
    else:
        print("Invalid nodes. Please enter valid node labels (A-M).")

if __name__ == "__main__":
    main()
