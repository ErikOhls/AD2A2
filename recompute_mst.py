#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Recomputing the minimum spanning tree

Team Number:
Student Names:
'''
import unittest
import networkx as nx
"""IMPORTANT:
We're using networkx only to provide a reliable graph
object.  Your solution may NOT rely on the networkx implementation of
any graph algorithms.  You can use the node/edge creation functions to
create test data, and you can access node lists, edge lists, adjacency
lists, etc. DO NOT turn in a solution that uses a networkx
implementation of a graph traversal algorithm, as doing so will result
in a score of 0.
"""
try:
    import matplotlib.pyplot as plt
    have_plt = True
except:
    have_plt = False

class Node:
    """
    Class containing various information about nodes

    Attributes:
       node(int): Identifier
       adj(list): List of adjacent nodes
       visited(boolean): Switch intended to turn on once node is visited
       parent(int): Identifier of parent node
    """
    node = ""
    adj = None
    edges = None
    visited = False
    parent = -1

def update_MST_1(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 1
    """
    (u, v) = e
    assert(e in G.edges() and e not in T.edges() and w > G[u][v]['weight'])


def update_MST_2(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==> graph T(V, E)
    Pre:  T is a valid MST of G
    Post: MST of G with edge e considered
    Example: TestCase 2
    """
    (u, v) = e
    assert(e in G.edges() and e not in T.edges() and w < G[u][v]['weight'])

    # List to hold all the vertices in T
    # Type: a[] where a is type of vertex identifier
    vertices = list(T)

    # Dict containing vertices and their respective neighbors
    # Type a{} where a is type of vertex identifier, label is vertex \
    # and label's list is list of neighbors
    g_util = {}
    for i in range(len(vertices)): # Fill dict with MST's vertices
    # Invariant: len(vertices)
    #   Variant: len(vertices)-1
        edges = []
        tmp = list(T.edges(vertices[i]))
        for j in range(len(T.edges(vertices[i]))):
        # Invariant: len(T.edges(vertices[i]))
        #   Variant: len(T.edges(vertices[i]))-1
            (node, neighbour) = tmp[j]
            edges.append(neighbour)
        g_util[vertices[i]] = edges

    # List containing vertices
    # Type: a[] where a is type of vertex identifier
    cycle = []

    # Find cycle in MST
    cycle = get_cycle(g_util, u, v, cycle)

    # Add new edge
    T.add_edge(u, v, weight = w)

    # List containing tuples of all edges connecting cycle
    # Type: tuple[]
    edge_cycle = [None for i in range(len(cycle))]
    for i in range(len(cycle)-1):
    # Invariant: len(cycle)-1
    #   Variant: (len(cycle)-1)-1
        edge_cycle[i] = (cycle[i], cycle[i+1])

    edge_cycle[-1] = (cycle[-1], cycle[0])

    # Find the heaviest edge
    to_remove = edge_cycle[0]
    for edge in edge_cycle:
    # Invariant: len(edge_cycle)
    #   Variant: len(edge_cycle)-1
        if edge == edge_cycle[0]:
            prev = edge
        elif T[prev[0]][prev[1]]['weight'] < T[edge[0]][edge[1]]['weight']:
            to_remove = edge
            prev = edge

    x, y = to_remove[0], to_remove[1]

    T.remove_edge(x, y)

    return T

def get_cycle(G, start_node, end_node, cycle):
    # Invariant: len(G)
    #   Variant: len(G)-start_node
    """
    Sig: dict G{V:[E..V]}, vertex start_node, vertex end_node, int[]  ==> int[]
    Pre: start_node and end_node is contained whitin graph G
    Post: List of vertices making up a cycle in G, if an edge existed \
          between start_node and end_node, or none
    Example: get_cycle(G{1: [2], 2: [3], 3:[2]}, 1, 3, []) ==>
             [1,2,3]
    """
    cycle = cycle + [start_node]
    if start_node == end_node:
        return cycle

    for vertex in G[start_node]:
    # Invariant: length(G[start_node])
    #   Variant: length(G[start_node])-1
        if vertex not in cycle:
            new_cycle = get_cycle(G, vertex, end_node, cycle)
            if new_cycle:
                return new_cycle

    return None

def update_MST_3(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 3
    """
    (u, v) = e
    assert(e in G.edges() and e in T.edges() and w < G[u][v]['weight'])

def update_MST_4(G, T, e, w):
    """
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 4
    """
    (u, v) = e
    assert(e in G.edges() and e in T.edges() and w > G[u][v]['weight'])


class RecomputeMstTest(unittest.TestCase):
    """Test Suite for minimum spanning tree problem

    Any method named "test_something" will be run when this file is 
    executed. Use the sanity check as a template for adding your own 
    test cases if you wish.
    (You may delete this class from your submitted solution.)
    """
    def create_graph(self):
        G = nx.Graph()
        G.add_edge('a', 'b', weight = 0.6)
        G.add_edge('a', 'c', weight = 0.2)
        G.add_edge('c', 'd', weight = 0.1)
        G.add_edge('c', 'e', weight = 0.7)
        G.add_edge('c', 'f', weight = 0.9)
        G.add_edge('a', 'd', weight = 0.3)
        return G

    def draw_mst(self, G, T, n):
        if not have_plt:
            return
        pos = nx.spring_layout(G) # positions for all nodes
        plt.subplot(220 + n)
        plt.title('updated MST %d' % n)
        plt.axis('off')
        # nodes
        nx.draw_networkx_nodes(G, pos, node_size = 700)
        # edges
        nx.draw_networkx_edges(G, pos, width = 6, alpha = 0.5,
                               edge_color = 'b', style = 'dashed')
        nx.draw_networkx_edges(T, pos, width = 6)
        # labels
        nx.draw_networkx_labels(G, pos, font_size = 20, font_family = 'sans-serif')

    def est_mst1(self):
        """Sanity Test

        This is a simple sanity check for your function;
        passing is not a guarantee of correctness.
        """
        # TestCase 1: e in G.edges() and not e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_1(G, T, ('a', 'd'), 0.5)
        self.draw_mst(G, T, 1)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
            )

    def est_mst2(self):
        # TestCase 2: e in G.edges() and not e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_2(G, T, ('a', 'd'), 0.1)
        self.draw_mst(G, T, 2)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
            )

    def test_mst2_fail(self):
        def helper_function_weight(T, G):
            weight = 0
            for u, v in T.edges():
                weight += G[u][v]['weight']
            return weight


        G = nx.complete_graph(5);

        G[0][1]['weight'] = 26;
        G[0][2]['weight'] = 24;
        G[0][3]['weight'] = 94;
        G[0][4]['weight'] = 97;
        G[1][2]['weight'] = 83;
        G[1][3]['weight'] = 100;
        G[1][4]['weight'] = 76;
        G[2][3]['weight'] = 10;
        G[2][4]['weight'] = 14;
        G[3][4]['weight'] = 7;


        MST = nx.minimum_spanning_tree(G);

        self.draw_mst(G, MST, 2)

        update_MST_2(G.copy(), MST, (1, 3), 31);

        G[1][3]['weight'] = 31

        print "67?", helper_function_weight(MST, G)


    def est_mst3(self):
        # TestCase 3: e in G.edges() and e in T.edges() and
        #             w < G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_3(G, T, ('a', 'c'), 0.1)
        self.draw_mst(G, T, 3)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'c'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
            )

    def est_mst4(self):
        # TestCase 4: e in G.edges() and e in T.edges() and
        #             w > G[u][v]['weight']
        G = self.create_graph()
        T = nx.minimum_spanning_tree(G)
        update_MST_4(G, T, ('a', 'c'), 0.4)
        self.draw_mst(G, T, 4)
        self.assertItemsEqual(
            T.edges(),
            [('a', 'b'), ('a', 'd'), ('c', 'd'), ('c', 'e'), ('c', 'f')]
            )

    @classmethod
    def tearDownClass(cls):
        if have_plt:
            plt.show()
if __name__ == '__main__':
    unittest.main()
