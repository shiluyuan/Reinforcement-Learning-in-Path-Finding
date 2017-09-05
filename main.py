from get_dict import get_dict
from get_R_Q import initial_R
from get_R_Q import initial_Q
from get_result import get_result

import pandas as pd
import time

data = pd.read_csv("graph.csv")
graph = get_dict(data)

A = graph["A"]
Z = graph["Z"]
weight = graph["weight"]
A_Z_dict = graph["A_Z_dict"]

##
start = 1
end = [9]

R = initial_R(A,Z,weight,A_Z_dict)
Q = initial_Q(R)

alpha = 0.7 # learning rate
epsilon = 0.1 #greedy policy
n_episodes = 1000

time0 = time.time()
result = get_result(R,Q,alpha,epsilon,n_episodes,start,end)
print("time is:",time.time() - time0)

print(result["ends_find"])
print(result["cost"])
print(result["routes_number"])



