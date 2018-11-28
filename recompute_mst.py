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
    Sig: graph G(V,E), graph T(V, E), edge e, int ==>
    Pre:
    Post:
    Example: TestCase 2
    """
    (u, v) = e
    assert(e in G.edges() and e not in T.edges() and w < G[u][v]['weight'])
    
    print "EDGES ----------------"
    vertices = list(T)
    #print vertices

    print T.edges()

    g_util = {}
    for i in range(len(vertices)):
        edges = []
        tmp = list(T.edges(vertices[i]))
        for j in range(len(T.edges(vertices[i]))):
            (node, neighbour) = tmp[j]
            edges.append(neighbour)
        g_util[vertices[i]] = edges

    #print g_util

    cycle = []

    cycle = get_cycle(g_util, u, v, cycle)
    print cycle

    T.add_edge(u, v, weight = w)

    new_cycle = [None for i in range(len(cycle))]
    for i in range(len(cycle)-1):
        new_cycle[i] = (cycle[i], cycle[i+1])

    new_cycle[-1] = (cycle[-1], cycle[0])

    to_remove = new_cycle[0]
    for edge in new_cycle:
        if edge == new_cycle[0]:
            prev = edge
        elif T[prev[0]][prev[1]]['weight'] < T[edge[0]][edge[1]]['weight']:
            to_remove = edge
            prev = edge

    x, y = to_remove[0], to_remove[1]

    print new_cycle

    '''
    if T[cycle[0]][cycle[-1]]['weight'] > T[cycle[0]][cycle[1]]['weight']:
        print cycle[0], cycle[-1], ":", T[cycle[0]][cycle[-1]]['weight']
        print cycle[0], cycle[1], ":", T[cycle[0]][cycle[1]]['weight']
        x, y = cycle[0], cycle[-1]

    for i in range(len(cycle)-2):
        if T[cycle[i]][cycle[i+1]]['weight'] > T[cycle[i+1]][cycle[i+2]]['weight']:
            print cycle[i], cycle[i+1], ":", T[cycle[0]][cycle[-1]]['weight']
            print cycle[i+1], cycle[i+2], ":", T[cycle[0]][cycle[-1]]['weight']
            x, y = cycle[i], cycle[i+1]

    if T[cycle[-2]][cycle[-1]]['weight'] > T[cycle[-1]][cycle[0]]['weight']:
        print cycle[-2], cycle[-1], ":", T[cycle[0]][cycle[-1]]['weight']
        print cycle[-1], cycle[0], ":", T[cycle[0]][cycle[-1]]['weight']
        x, y = cycle[-2], cycle[-1]
    '''
    print x, y
    T.remove_edge(x, y)

    return T

def get_cycle(G, start_node, end_node, cycle):
    do_print = False
    cycle = cycle + [start_node]
    if do_print: print "Top:", start_node, cycle
    if do_print: print "end_node:", end_node
    if start_node == end_node:
        if do_print: print "start node == end node"
        return cycle

    for vertex in G[start_node]:
        if vertex not in cycle:
            if do_print: print "vertex:", vertex
            new_cycle = get_cycle(G, vertex, end_node, cycle)
            if new_cycle:
                return new_cycle

    return None


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

        print MST.edges()

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
