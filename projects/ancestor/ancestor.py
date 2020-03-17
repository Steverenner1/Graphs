import sys
import os

sys.path.append('../graph')
from graph import Graph
from util import Stack

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_vertex(8)
    graph.add_vertex(9)
    graph.add_vertex(10)
    graph.add_vertex(11)
    
    for a in ancestors:
        graph.add_edge(a[1], a[0])


    s = Stack()
    s.push(starting_node)
    visited = []

    while s.size() > 0:
        remove = s.pop()
        for i in sorted(graph.vertices[remove]):
            s.push(i)
        if remove not in visited and remove != starting_node:
            visited.append(remove)
    if len(visited) < 1:
        return -1
    elif len(visited) == 1:
        for v in visited:
            return v
    return visited[len(visited) -1]
    print(ancestors)
    # test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
    


    

