# Path with Maximum Probability

## Problem Description

You are given a directed weighted graph represented by `n` nodes and an array of edges `edges`. Each element `edges[i]` is a pair `[u, v]` that represents a directed edge from node `u` to node `v` with a corresponding success probability `succProb[i]`.

You are also given two integers `start_node` and `end_node` representing the starting and ending nodes respectively.

Your task is to find the maximum success probability of a path from `start_node` to `end_node` using Dijkstra's algorithm.

## Approach

To solve this problem, we can use Dijkstra's algorithm to find the maximum success probability of a path from the starting node to the ending node.

1. Build the graph: Create a graph representation suitable for Dijkstra's algorithm. Each node will have a list of adjacent nodes along with their corresponding success probabilities.

2. Initialize the priority queue: Create a max heap priority queue to store the nodes with their current success probabilities. Initialize the starting node with a success probability of 1.0.

3. Initialize the probabilities: Create a vector to store the current maximum success probability for each node. Initialize all probabilities to 0.0, except for the starting node which is initialized to 1.0.

4. Perform Dijkstra's algorithm: While the priority queue is not empty, extract the node with the maximum success probability. If the extracted node is the ending node, return its success probability. Otherwise, iterate through its adjacent nodes and update their success probabilities if a higher probability is found. Push the updated nodes into the priority queue.

5. Return the maximum success probability: If the ending node is not reached, return 0.0 as there is no path from the starting node to the ending node.

## Implementation

Here is the implementation of the `maxProbability` function in C++:

```cpp
double maxProbability(int n, vector<vector<int>> &edges, vector<double> &succProb, int start_node, int end_node)
{
    // Build the graph
    vector<vector<pair<int, double>>> graph(n);
    for (int i = 0; i < edges.size(); i++)
    {
        int u = edges[i][0];
        int v = edges[i][1];
        double prob = succProb[i];
        graph[u].push_back({v, prob});
        graph[v].push_back({u, prob});
    }

    // Initialize the priority queue
    priority_queue<pair<double,int>> pq;
    pq.push({1.0,start_node});

    // Initialize the probabilities
    vector<double> probabilities(n,0.0);
    probabilities[start_node] = 1.0;

    // Perform Dijkstra's algorithm
    while(!pq.empty()){
        double curr_prob = pq.top().first;
        int topNode = pq.top().second;
        pq.pop();

        if(topNode==end_node){
            return curr_prob;
        }

        for(auto neighbour:graph[topNode]){
            int adjNode = neighbour.first;
            double probab = neighbour.second;
            double new_prob = curr_prob*probab;
            if(new_prob>probabilities[adjNode]){
                probabilities[adjNode] = new_prob;
                pq.push({probabilities[adjNode],adjNode});
            }
        }
    }

    return probabilities[end_node];
}

```

## Complexity Analysis

The time complexity of this approach is O(E log V), where E is the number of edges and V is the number of nodes in the graph. This is because we perform Dijkstra's algorithm, which has a time complexity of O((E+V) log V) in the worst case. In our case, the number of edges is E and the number of nodes is V.

The space complexity is O(V), where V is the number of nodes in the graph. This is because we need to store the graph representation and the probabilities for each node.

