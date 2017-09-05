from collections import Counter

def get_single_dict(dic):
    single_link = {}
    min_value = min(dic.values())
    for key in dic.keys():
        if dic[key] == min_value:
            single_link[key] = dic[key]
    return single_link.keys()

def get_best_nodes(Q,start,end):
    next_level = [start]
    node_use = [start]
    while list(set(next_level) & set(end)) == []:
        temp_level = []
        for i in next_level:
            temp_level += get_single_dict(Q[i])
        next_level = list(set(temp_level))
        node_use += next_level
    return list(set(node_use))

def get_best_net(Q,nodes):
    best_net = {}
    for i in nodes:
        best_net[i] = list(set( get_single_dict(Q[i]) ) & set(nodes))
    return best_net

def get_all_best_routes(graph,start,end,max_depth):
    past_path = []
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
       # print "*"
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            ## end the current loop if we already reach the point
            if adjacent in end:
                new_path.append(adjacent)
                past_path.append(new_path)
                continue
            
            if adjacent in new_path:
                continue

            new_path.append(adjacent)
            if len(new_path) >= max_depth and new_path[-1] not in end:
                break
           # print new_path
            queue.append(new_path)
            past_path.append(new_path)
    
    best_paths = []
    for l in past_path:
        if l[-1] in end:
            best_paths.append(l)
    return best_paths
    
    
def get_cost(R,route):
    cost = 0
    for i in range(len(route)-1):
        cost += R[route[i]][route[i+1]]
    return round(cost,3)

def count_routes(routes):
    ends_find = []
    all_routes = {}
    for i in range(len(routes)):
        ends_find.append(routes[i][-1])
    
    count =  dict(Counter(ends_find))
    
    ends = list(set(ends_find))
    for i in ends:
        all_routes[i] = []
    for i in routes:
        end = i[-1]
        all_routes[end].append(i)
    return {"routes_number":count,
            "all_routes":all_routes}
    
        

def get_route(Q,start,end):
    """ input is  Q-table is like:{1: {2: 0.5, 3: 3.8},
                                   2: {1: 5.9, 5: 10}} """   
    single_route = [start]
    while single_route[-1] not in end:
        next_step = min(Q[single_route[-1]],key=Q[single_route[-1]].get)
        single_route.append(next_step)
        if len(single_route) > 2 and single_route[-1] in single_route[:-1]:
            break
    return single_route




















    