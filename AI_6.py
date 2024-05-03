# Implementation of A * Algorithm in Python
import heapq

def astar(node,goal,graph,heuristic):
    visited=set()
    priority_queue=[(heuristic[node],0,node)]
    path={node:None}
    path_cost={node:0}

    while priority_queue:
        print(f"Open List : {priority_queue}")
        h,cost,curr_node=heapq.heappop(priority_queue)

        if goal==curr_node:
            return construct_path(node,goal,path)
        
        visited.add(curr_node)
        for neighbour,edge_cost in graph[curr_node].items():
            total_cost=edge_cost+path_cost[curr_node]
            if neighbour not in visited or total_cost<path_cost[neighbour]:
                path_cost[neighbour]=total_cost
                path[neighbour]=curr_node
                heapq.heappush(priority_queue,(heuristic[neighbour]+total_cost,total_cost,neighbour))
    return None

def construct_path(start,goal,path):
    curr_node=goal
    path_seq=[]
    while curr_node:
        path_seq.insert(0,curr_node)
        curr_node=path[curr_node]
    return path_seq

graph = {
    'A': {'B': 2, 'E': 3},
    'B': {'C': 1, 'G': 9},
    'C': {},
    'D': {'G':1},
    'E': {'D':6},
    'G': {}
}

heuristic = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
}

start = input("Enter the start node : ")
goal = input("Enter the goal node : ")

astar_path = astar(start,goal,graph,heuristic)

if astar_path:
    print(f"Goal {goal} reached using A*.")
    print(f"Path:{astar_path}")
else:
    print(f"Goal {goal} cannot be reached using A*.")