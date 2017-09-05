from Q_routing import Q_routing

from get_all_routes import get_best_nodes
from get_all_routes import get_best_net
from get_all_routes import get_all_best_routes
from get_all_routes import get_cost
from get_all_routes import count_routes
from get_all_routes import get_route

from collections import Counter

#########
def get_result(R,Q,alpha,epsilon,n_episodes,start,end):
    Q = Q_routing(R,Q,alpha,epsilon,n_episodes,start,end)
    nodes = get_best_nodes(Q,start,end)
    graph = get_best_net(Q,nodes)
    route_len = len(get_route(Q,start,end))
    routes = get_all_best_routes(graph,start,end,route_len+1)
    result = count_routes(routes)
    ###
    ends_find = []
    for i in range(len(routes)):
        ends_find.append(routes[i][-1])
    ends_find = list(set(ends_find)) 
    ###
    cost = []
    for i in routes:
        cost.append(get_cost(R,i))
    Counter(cost) 
    return {"nodes":nodes,
            "graph":graph,
            "ends_find":ends_find,
            "cost":dict(Counter(cost)),
            "routes_number":result['routes_number'],
            "all_routes":result['all_routes']}