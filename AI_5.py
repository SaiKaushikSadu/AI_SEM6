# Implementation of Greedy Best first search in Python
from queue import PriorityQueue

def bfs(graph,start,goal,heuristic_values):
    pq=PriorityQueue()
    visited=[]
    pq.put((0,start))

    while not pq.empty():
        cost,node=pq.get()
        print(f"\n{node} : ")

        if node==goal:
            visited.append(node)
            print(f"Greedy Best First Search Path : {visited}")
            return True
        
        if node not in visited:
            visited.append(node)
            print(f"Closed List : {visited}")
            print(f"Open List : [ ",end='')
            for neighbour_node,neighbour_cost in graph[node].items():
                print(f"'{neighbour_node}', ",end='')
                pq.put((heuristic_values[neighbour_node],neighbour_node))
            print(f"]")
    return False

graph = {
    'A' : {'B':2,'C':5},
    'B' : {'A':2,'D':6},
    'C' : {'A':5,'D':2,'E':5},
    'D' : {'B':6,'C':2,'E':6},
    'E' : {'C':5,'D':6}
}

heuristic_values = {'A':10,'B':8,'C':5,'D':3,'E':0}
start = input("Enter the start node : ")
goal = input("Enter the goal node : ")

if bfs(graph,start,goal,heuristic_values):
    print("Goal Node found")
else:
    print("Goal Node not found")