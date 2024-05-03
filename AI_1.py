# Implementation of DFS in python

#        A
#      /   \
#     B     C
#    / \   / \ 
#   D   E F   G

def dfs(node,goal,graph,openlist,visited):
    if node not in visited:
        visited.append(node)
        if goal==node:
            print("\nGoal Node Found")
            print(f"The DFS path is {visited}")
            return True
        else:
            if node in graph:
                openlist.remove(node)
                for i in range(-1,-len(graph[node])-1,-1):
                    openlist.insert(-len(openlist),graph[node][i])
                print(f"\n{node} : ")
                print(f"Open list is {openlist}")
                print(f"Closed list is {visited}")
                for neighbour in graph[node]:
                    if dfs(neighbour,goal,graph,openlist,visited):
                        return True
    return False

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

start=input("Enter the start node : ")
goal=input("Enter the goal node : ")

visited=[]
openlist=[start]

print(f"Initial open list is {openlist}")
print(f"Initial closed list is {visited}")

if not dfs(start,goal,graph,openlist,visited):
    print("Goal node not found")
