import copy

def initial_R(A,Z,weight,A_Z_dict):
    #input net is
    R = {}
    net = copy.deepcopy(A_Z_dict)
    for i in net.keys():
        sub_key = net[i]
        sub_dic = {}
        for j in sub_key:
            sub_dic[j] = 0
        R[i] = sub_dic       
    for i in range(len(A)):
        R[A[i]][Z[i]] = weight[i]
    return R

def initial_Q(R):
    Q = copy.deepcopy(R)
    for i in Q.keys():
        for j in Q[i].keys():
            Q[i][j] = 100
    return Q