def create_graph():
    n=int(input("Enter the number of nodes in the graph : "))
    graph={}
    for i in range(n):
        a=input("Enter the parent node "+str(i+1)+" ")
        s=int(input("Enter the num of child nodes for the parent node "+a+" "))
        path_cost=[]
        for j in range(s):
            path_cost1=[]
            d1=input("Enter child node "+str(j+1)+" ")
            cost=int(input("Enter the corresponding path cost for node  "+d1+" "))
            path_cost1.append(d1)
            path_cost1.append(cost)
            path_cost.append(tuple(path_cost1))
        graph[a]=path_cost
    return graph

def tot_pathcost_calculation(path):
    path_cost=0
    for(edge,cost) in path:
        path_cost+=cost
    return path_cost


def bfs(graph,src,des):
    visited=[]
    queue=[[(src,0)]]
    while queue:
        path=queue.pop(0)
        current_node=path[-1][0]
        visited.append(current_node)
        if current_node==des:
            path_cost=tot_pathcost_calculation(path)
            print("Path found : ",path)
            print("corresponding path cost for the obtained path : ",path_cost)
        else:
            adjacent_nodes=graph.get(current_node,[])
            for (i,j) in adjacent_nodes:
                if i not in visited:
                    new_path=path.copy()
                    new_path.append((i,j))
                    queue.append(new_path)


def ucs(graph,src,des):
    def pathcost_ucs(path):
        path_cost=0
        for(edge,cost) in path:
            path_cost+=cost
        return path_cost,path[-1][0]
    visited=[]
    queue=[[(src,0)]]
    while queue:
        #print(queue)
        queue.sort(key=pathcost_ucs)
        #print(queue)
        path=queue.pop(0)
        current_node=path[-1][0]
        visited.append(current_node)
        if current_node==des:
            path_cost=tot_pathcost_calculation(path)
            print("Path found : ",path)
            print("corresponding path cost for the obtained path : ",path_cost)
        else:
            adjacent_nodes=graph.get(current_node,[])
            for (i,j) in adjacent_nodes:
                if i not in visited:
                    new_path=path.copy()
                    new_path.append((i,j))
                    queue.append(new_path)


def dfs(stack,visited,graph,src,des,cost):
    stack.append((src,cost))
    visited.append(src)
    if src==des:
        path_cost=tot_pathcost_calculation(stack)
        print("Path found : ",stack)
        print("corresponding path cost for the obtained path : ",path_cost)
    adjacent_nodes=graph.get(src,[])
    for (i,j) in adjacent_nodes:
                if i not in visited:
                    dfs(stack,visited,graph,i,des,j)
                    
            
def bidirectional_search(graph,src,des):
    forward=[]
    f_queue=[[(src,0)]]
    backward=[]
    b_queue=[[(des,0)]]
    while f_queue and b_queue:
        forward_path=f_queue.pop(0)
        current_fnode=forward_path[-1][0]
        backward_path=b_queue.pop(0)
        current_bnode=backward_path[-1][0]
        forward.append(current_fnode)
        backward.append(current_bnode)
        if current_fnode==current_bnode:
            print("Intersected at node "+str(current_bnode)+" ")
            backward_path.reverse()
            #print(backward_path)
            backward_path1=backward_path[1:]
            res_path=list(forward_path+backward_path1)
            path_cost=tot_pathcost_calculation(res_path)
            print("Path found : ",res_path)
            print("corresponding path cost for the obtained path : ",path_cost)
        else:
            adjacent_nodes_f=graph.get(current_fnode,[])
            for (i,j) in adjacent_nodes_f:
                if i not in forward:
                    new_path=forward_path.copy()
                    new_path.append((i,j))
                    f_queue.append(new_path)
            adjacent_nodes_b=graph.get(current_bnode,[])
            for (i,j) in adjacent_nodes_b:
                if i not in backward:
                    new_path=backward_path.copy()
                    new_path.append((i,j))
                    b_queue.append(new_path)

def dls(graph,stack,src,des,depth_limit,cost):
    stack.append((src,cost))
    if src==des:
        path_cost=tot_pathcost_calculation(stack)
        print("Path found : ",stack)
        print("corresponding path cost for the obtained path : ",path_cost)
        return True
    if depth_limit<=0:
        return False
    adjacent_nodes=graph.get(src,[])
    for (i,j) in adjacent_nodes:
        if dls(graph,stack,i,des,depth_limit-1,j):
            return True
        else:
            stack.pop()
    return False
                
def ids(graph,src,des,depth_limit,cost):
    for i in range(depth_limit):
        stack=[]
        if dls(graph,stack,src,des,i,cost):
            return True
    return False

""" input_graph = {
    'A': [('B',2),('C',3),('D',5)],
    'B': [('E',4),('F',5)],
    'C': [('G',1),('H',2)],
    'D': [('H',5)],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}       """    
input_graph=create_graph()
choice='yes'
print("Blind search techniques")
print("1)BFS\n2)DFS\n3)UCS\n4)DLS\n5)IDS\n6)BDS\n")
while(choice=='yes'):
    c=int(input("search technique to be implemented : "))
    if c==1:
        print("Breadth first search\n")
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        bfs(input_graph,source,goal)
    elif c==2:
        print("Depth First search\n")
        stack=[]
        visited=[]
        cost=0
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        dfs(stack,visited,input_graph,source,goal,cost)
    elif c==3:
        print("Uniform cost search\n")
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        ucs(input_graph,source,goal)
    elif c==4:
        print("Depth limit search\n")
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        limit=int(input("Enter the maximum depth limit : "))
        stack=[]
        cost=0
        check=dls(input_graph,stack,source,goal,limit,cost)
        if check==False:
            print("Goal cannot be reached within the specified depth limit :( ")
    elif c==5:
        print("Iterative Deepening search\n")
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        limit=int(input("Enter the maximum depth limit : "))
        cost=0
        check=ids(input_graph,source,goal,limit,cost)
        if check==False:
            print("Goal cannot be reached within the specified depth limit :( ")
    else:
        print("Bidirectional search\n")
        source=input("Enter the start node : ")
        goal=input("Enter the goal node : ")
        bidirectional_search(input_graph,source,goal)
    print()
    choice=input("Do you want to continue?? (yes/no)")
    
        
