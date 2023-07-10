import heapq

def best_first_search(source,target,graph):
    open=[(0,source)]
    visited=set()

    while open:
        (cost,currentnode)=heapq.heappop(open)
        if currentnode==target:
            return cost
        visited.add(currentnode)
        for neighbor,neighbor_cost in graph[currentnode]:
            if neighbor not in visited and neighbor not in [node[1] for node in open]:
                heapq.heappush(open,(neighbor_cost+cost,neighbor))
    return None

graph = {
    'A': [('B', 5), ('C', 6)],
    'B': [('D', 4), ('E', 7)],
    'C': [('F', 9), ('G', 8)],
    'D': [('H', 3)],
    'E': [('I', 6)],
    'F': [('J', 5)],
    'G': [('K', 7)],
    'H': [('L', 1)],
    'I': [('M', 2)],
    'J': [('N', 3)],
    'K': [('O', 4)],
    'L': [],
    'M': [],
    'N': [],
    'O': [('P', 1)],
    'P': []
}

start =input("enter starting node ")
target=input("enter target node ")

cost =best_first_search(start,target,graph)

print(f"Total cost to reach from {start}to {target} is {cost} ")