
def reach_out(group,net):
    ## this reach out for points, one loop
    search_key = set(net.keys()) & set(group)
    for key in search_key:
        if key in net.keys():
            group += net[key]
            del net[key]
    return {"new_group":group,
            "new_net":net}
    
def get_group(point,net):
    group = list([point] + net[point])
    group_len = [0,1]
    while group_len[-2] != group_len[-1]:
        temp = reach_out(group,net)
        group = temp["new_group"]
        net = temp["new_net"]
        group_len.append(len(group))
    return list(set(group))

def get_sub_net(nodes,net):
    ## input is a node of a network of list
    sub_net = {}
    for i in nodes:
        sub_net[i] = net[i]
    return sub_net