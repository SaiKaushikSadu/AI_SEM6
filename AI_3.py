# Implementation of DFID in python

#        A
#      /   \
#     B     C
#    / \   / \ 
#   D   E F   G

def dfid(node,goal,graph,max_depth,depth_limit):
    while depth_limit<=max_depth:
        visited=[]
        print(f"Trying for level : {depth_limit}")
        result=dls(node,goal,graph,visited,0,depth_limit)
        if result:
            print(f"Goal node found at depth {depth_limit}")
            return True
        depth_limit=depth_limit+1

def dls(node,goal,graph,visited,curr_depth,max_depth):
    if node not in visited:
        visited.append(node)
        if node==goal:
            print(f"Path : {visited}")
            return True
        else:
            if curr_depth<max_depth:
                for neighbour in graph[node]:
                    if dls(neighbour,goal,graph,visited,curr_depth+1,max_depth):
                        return True
            else:
                return False
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
max_depth= int(input("Enter the depth limit : "))
depth_limit=0

result=dfid(start,goal,graph,max_depth,depth_limit)
