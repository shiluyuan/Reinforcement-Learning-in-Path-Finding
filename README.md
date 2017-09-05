
Reinforcement Learning in Path Finding
Traditional shortest path algorithm including BFS(Breadth First Search), DFS(Depth First Search) and Dijkstra's algorithm.
However, BFS and DFS is very slow and suffer exponential time increase as graph tree become deeper and deeper for large complex graph. For my experience, when I have 70k nodes and 200K edge graph, BFS and DFS would take hours to search 5 depth. So it is impossible if the shortest path is 6 depth or more.


For Dijkstra's algorithm, it is quick to give a shortest path, but it will give only one not all of the best path. For instance, if there are 100 equal best rountes in a weighted graph, Dijskra's algorithm will only return one of the best rountes.
So I develop a algorithm using reinforcemenet learning in path finding problem. In reinforcemnt learning problem, we have action, rewards and states and discount rate. To solve traditional problem, we have Q-learning. Q-learning can be used to find an optimal action-selection policy for any given (finite) Markov decision process (MDP). Similarly, to solve best-path-finding problem, we have Q-rounting. The difference between Q-Learning and Q-Rounting is that, Q-Rounting doesn't have a discount rate, and for each state, it will choose the minimun furture cost instead of maximum future reward.

I only give a example of small network. For my experience, I tried on large complex network with 70k nodes and 20k edges and Q-routing algorithm is still fast and it can find all shortest path with 10 depth within minutes.
You set your own graph in graph.csv. First column is stating node, second column is connecting node and third column is the cost between the two nodes.
Hope you have fun!! If you have any questions, please leave comments or e-mail to mathshiluyuan@gmail.com.
