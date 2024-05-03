# Implementation of DLS in python

#        A
#      /   \
#     B     C
#    / \   / \ 
#   D   E F   G
#  /     \
# H       I

def dls(node,goal,graph,openlist,visited,depth_limit,curr_limit):
    if node not in visited:
        visited.append(node)
        if goal==node:
            print(f"{goal}- Goal node found")
            print(f"DLS path : {visited}")
            return True
        else:
            if curr_limit<=depth_limit:
                print(f"\n{node} : ")
                if node in graph:
                    openlist.remove(node)
                    for i in range(-1,-len(graph[node])-1,-1):
                        openlist.insert(-len(openlist),graph[node][i])
                    print(f"Open List : {openlist}")
                    print(f"Close List : {visited}")
                    for neighbour in graph[node]:
                        if dls(neighbour,goal,graph,openlist,visited,depth_limit,curr_limit+1):
                            return True
            else:
                return False
    return False


graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':['H'],
    'E':['I'],
    'F':[],
    'G':[],
    'H':[],
    'I':[]
}

start=input("Enter the start node : ")
goal=input("Enter the goal node : ")

visited=[]
openlist=[start]
depth_limit= int(input("Enter the depth limit : "))
curr_limit=0

print(f"Initial open list : {openlist}")
print(f"Initial close list : {visited}")

if dls(start,goal,graph,openlist,visited,depth_limit,curr_limit):
    print("Goal node found within the depth")
else:
    print("Goal node not found within the depth")