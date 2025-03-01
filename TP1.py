from collections import deque

def path_exists(graph, start, end):
    if start == end:
        return True
    
    queue = deque([start])
    visited = set()
    
    while queue:
        node = queue.popleft()
        if node == end:
            return True
        visited.add(node)
        
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
    
    return False

def main():
    graph = {
        '1': ['2'],
        '2': ['1', '5'],
        '3': ['6'],
        '4': ['6', '7'],
        '5': ['2'],
        '6': ['3', '4', '7'],
        '7': ['4', '6']
    }
    
    print("Enter the start and end nodes:")
    start = input("Start node: ").strip()
    end = input("End node: ").strip()
    
    if path_exists(graph, start, end):
        print(f"=> Path exists between {start} and {end}.")
    else:
        print(f"=> No path exists between {start} and {end}.")

if __name__ == "__main__":
    main()
