
# Reinforcement Learning in Path Finding

Traditional shortest path algorithm including BFS(Breadth First Search), DFS(Depth First Search) and Dijkstra's algorithm.

However, BFS and DFS is very slow and suffer exponential time increase as graph tree become deeper and deeper for large complex graph. For my experience, when I have 70k nodes and 200K edge graph, BFS and DFS would take hours to search 5 depth. So it is impossible if the shortest path is 6 depth or more.

<img src='p1.png'>

<img src='P2.png'>

For Dijkstra's algorithm, it is quick to give a shortest path, but it will give only one not all of the best path. For instance, if there are 100 equal best rountes in a weighted graph, Dijskra's algorithm will only return one of the best rountes. 

So I develop a algorithm using reinforcemenet learning in path finding problem. In reinforcemnt learning problem, we have action, rewards and states and discount rate. To solve traditional problem, we have Q-learning. Q-learning can be used to find an optimal action-selection policy for any given (finite) Markov decision process (MDP). Similarly, to solve best-path-finding problem, we have Q-rounting. The difference between Q-Learning and Q-Rounting is that, Q-Rounting doesn't have a discount rate, and for each state, it will choose the minimun furture cost instead of maximum future reward.

<img src='p3.png'>
<img src='p4.png'>

The python code for Q-Rounting:
```python
def update_Q(T,Q,current_state, next_state, alpha):
    current_t = T[current_state][next_state]
    current_q = Q[current_state][next_state]
    new_q = current_q + alpha * (current_t + min(Q[next_state].values()) - current_q)
    Q[current_state][next_state] = new_q   
    return Q
```

Here we take a small network for instance.
<img src='p5.png'>
We use number 1 to 9  to repalce node A to I. And we want to find shortest path from 1(A) to 9(I).


```python
from get_dict import get_dict
from get_R_Q import initial_R
from get_R_Q import initial_Q
from get_result import get_result

import pandas as pd
import time

data = pd.read_csv("graph_1.csv")
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
print(result["all_routes"])
```

    loop: 0
    nodes: [0, 0, 6]
    nodes: [0, 0, 6, 4]
    nodes: [0, 0, 6, 4, 4]
    nodes: [0, 0, 6, 4, 4, 4]
    time is: 0.008524894714355469
    {9: [[1, 4, 5, 9]]}
    

We can see it find the shortest is 1-4-5-9(A-D-E-I) and the cost for this rounte is 23.
Now we change the weight from 4(D) to 9(I) to 18. Now we expect it will finde another rount 1-4-9(A-D-I), since both route have cost 23.


```python
from get_dict import get_dict
from get_R_Q import initial_R
from get_R_Q import initial_Q
from get_result import get_result

import pandas as pd
import time

data = pd.read_csv("graph_2.csv")
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
print(result["all_routes"])
```

    loop: 0
    nodes: [0, 0, 8]
    nodes: [0, 0, 8, 4]
    nodes: [0, 0, 8, 4, 4]
    nodes: [0, 0, 8, 4, 4, 4]
    time is: 0.006042003631591797
    {9: [[1, 4, 9], [1, 4, 5, 9]]}
    

Now we can see it find two routes have same smallest cost 23.

This is only a example of small network. For my experience, I tried on large complex network with 70k nodes and 20k edges and Q-routing algorithm is still fast and it can find all shortest path with 10 depth within minutes. 

You set your own graph in graph.csv. First column is stating node, second column is connecting node and third column is the cost between the two nodes.

Hope you have fun!! If you have any questions, please leave comments or e-mail to mathshiluyuan@gmail.com.
