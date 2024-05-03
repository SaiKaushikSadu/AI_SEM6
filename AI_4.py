# Implementation of BFS in python

#        A
#      /   \
#     B     C
#    / \   / \ 
#   D   E F   G


def bfs(node,goal,graph,visited,openlist,queue):
    queue.append(node)
    visited.append(node)
    openlist.remove(node)
    for i in graph[node]:
        openlist.append(i)
    print(f'\n{node} : ')
    print(f'Open List : {openlist}')
    print(f'Close List : {visited}')
    while queue:
        curr=queue.pop(0)
        for i in graph[curr]:
            print(f'\n{i} : ')
            if i not in visited:
                openlist.pop(0)
                for j in graph[i]:
                    openlist.append(j)
                visited.append(i)
                queue.append(i)
                print(f"Open List:{openlist}")
                print(f"Closed List:{visited}")
                if i == goal:
                    return True
    return False

graph = {
        'A':['B','C'],
        'B':['D','E'],
        'C':['F','G'],
        'D':[],
        'E':[],
        'F':[],
        'G':[]
}
start = input("Enter Start Node:")
goal = input("Enter Goal Node:")
visited=[]
openlist=[start]
queue=[]

print(f"Initial Open list : {openlist}")
print(f"Initial Close list : {visited}")

if bfs(start,goal,graph,visited,openlist,queue):
    print("Goal Node found")
else:
    print("Goal Node not found")
