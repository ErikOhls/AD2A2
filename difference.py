#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'''
Assignment 2: Search String Replacement

Team Number: 44
Student Names: Erik Lövgren, Erik Ohlsson
'''
import unittest
# Sample matrix provided by us:
from string import ascii_lowercase

# Solution to part b:
def min_difference(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference("dinamck","dynamic",R) ==> 3
    """
    '''
    if len(u) != len(r):
        delta = len(u) - len(r)
        print delta
        if delta < 0:
            for i in range(abs(delta)):
                u = u + "-"
        else:
            for i in range(delta):
                r = r + "-"
    '''

    M = initialize_matrix(u,r, R)
    #M = construct_weight_new(u,r,M,R)

    print("printing Matrix")
    for row in M:
        for val in row:
            print'{:3}'.format(val),
        print

    print "result =", M[-1][-1]
    return M[-1][-1]
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']

def initialize_matrix(u,r, R):
    M = [[None for i in range (len(r)+2)]for j in range (len(u)+2)]

    # FFS!!! I = ROW! J = COLUMN!
    # OBS! Måste lägga till dash: - om len(u) != len(r)
    print r
    print len(r)+2, len(u)+2
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 and j < 2:
                M[i][j] = 0      # Set first 2x2 to 0
                continue
            elif j == 0 and i < len(u)+2:
                print i, j
                print r[i-2]
                M[i][j] = r[i-2] # Set row labels
            elif i == 0 and j < len(r)+2:
                print i, j
                M[i][j] = u[j-2] # Set column labels
            elif i == 1 and j < len(r)+2:
                M[i][j] = M[i][j-1] + R['-'][M[0][j]]   # Set first column values
            elif j == 1 and i < len(u)+2:
                M[i][j] = M[i-1][j] + R['-'][M[i][0]]   # Set first row values
            elif i < len(u)+2 and j < len(r)+2:
                M[i][j] = 0      # initialize remaining matrix

    return M


def construct_weight_new(u,r,M,R):
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 or j < 2:                    # Ignore first 2 rows and columns
                continue
            if M[0][j] == M [i][0]:
                difference = 0
            else:
                difference = R[M[0][j]][M[i][0]]
            M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1])+difference

    return M


def construct_weight_1_matrix(u,r,M,R):
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 or j < 2:                    # Ignore first 2 rows and columns
                continue
            differance = R[M[0][j]][M[i][0]]
            if not differance:         # If current row/column label match
                M[i][j] = M[i-1][j-1]
            else:
                if differance == 0:
                    differance = 1
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1])+differance
    return M

def construct_weight_2_matrix(u,r,M,R):
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 or j < 2:                 # Ignore first 2 rows and columns
                continue
            #if i == j and M[0][j] == M[i][0]:  # If current row/column label match
            elif  M[0][j] == M[i][0]:  # If current row/column label match
                M[i][j] = M[i-1][j-1]
            elif i ==j:
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1])+2
            else:
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1])+1
    return M

# Solution to part c:
def min_difference_align(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:
    Post:
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference_align("dinamck","dynamic",R) ==>
                                    3, "dinam-ck", "dynamic-"
    """

def qwerty_distance():
    """Generates a QWERTY Manhattan distance resemblance matrix

    Costs for letter pairs are based on the Manhattan distance of the
    corresponding keys on a standard QWERTY keyboard.
    Costs for skipping a character depends on its placement on the keyboard:
    adding a character has a higher cost for keys on the outer edges,
    deleting a character has a higher cost for keys near the middle.

    Usage:
        R = qwerty_distance()
        R['a']['b']  # result: 5
    """
    from collections import defaultdict
    import math
    R = defaultdict(dict)
    R['-']['-'] = 0
    zones = ["dfghjk", "ertyuislcvbnm", "qwazxpo"]
    keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for num, content in enumerate(zones):
        for char in content:
            R['-'][char] = num + 1
            R[char]['-'] = 3 - num
    for a in ascii_lowercase:
        rowA = None
        posA = None
        for num, content in enumerate(keyboard):
            if a in content:
                rowA = num
                posA = content.index(a)
        for b in ascii_lowercase:
            for rowB, contentB in enumerate(keyboard):
                if b in contentB:
                    R[a][b] = int(math.fabs(rowB - rowA) + math.fabs(posA - contentB.index(b)))
    return R

class MinDifferenceTest(unittest.TestCase):
    """Test Suite for search string replacement problem

    Any method named "test_something" will be run when this file is
    executed. Use the sanity check as a template for adding your own test
    cases if you wish.
    (You may delete this class from your submitted solution.)
    """
    '''
    def test_diff_sanity(self):
        """Difference sanity test

        Given a simple resemblance matrix, test that the reported
        difference is the expected minimum. Do NOT assume we will always
        use this resemblance matrix when testing!
        """
        alphabet = ascii_lowercase + '-'
        # The simplest (reasonable) resemblance matrix:
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("dinamck","dynamic",R),3)
    def test_diff_one_equal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("a","a",R),0)

    def test_diff_one_unequal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("b","a",R),1)

    def test_diff_calle_banan(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("calle","banan",R),4)

    def test_diff_all_unequal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("aaaaaaaaaaaaaaa","bbbbbbbbbbbbbbb",R),15)

    def test_diff_all_equal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(min_difference("aaaaaaaaaaaaaaa","aaaaaaaaaaaaaaa",R),0)

    '''
    def test_diff_failed(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference('iacxoey', 'yjavik', R), 7)
    '''
    def test_diff_failed2(self):
        R = {'-': {'-': 0, 'a': 50, 'c': 50, 'b': 50, 'e': 50, 'd': 50, 'g': 50, 'f': 50, 'i': 50, 'h': 50, 'k': 50, 'j': 50, 'm': 50, 'l': 50, 'o': 50, 'n': 50, 'q': 50, 'p': 50, 's': 50, 'r': 50, 'u': 50, 't': 50, 'w': 50, 'v': 50, 'y': 50, 'x': 50, 'z': 50}, 'a': {'-': 50, 'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25}, 'c': {'-': 50, 'a': 2, 'c': 0, 'b': 1, 'e': 2, 'd': 1, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 8, 'j': 7, 'm': 10, 'l': 9, 'o': 12, 'n': 11, 'q': 14, 'p': 13, 's': 16, 'r': 15, 'u': 18, 't': 17, 'w': 20, 'v': 19, 'y': 22, 'x': 21, 'z': 23}, 'b': {'-': 50, 'a': 1, 'c': 1, 'b': 0, 'e': 3, 'd': 2, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 9, 'j': 8, 'm': 11, 'l': 10, 'o': 13, 'n': 12, 'q': 15, 'p': 14, 's': 17, 'r': 16, 'u': 19, 't': 18, 'w': 21, 'v': 20, 'y': 23, 'x': 22, 'z': 24}, 'e': {'-': 50, 'a': 4, 'c': 2, 'b': 3, 'e': 0, 'd': 1, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 6, 'j': 5, 'm': 8, 'l': 7, 'o': 10, 'n': 9, 'q': 12, 'p': 11, 's': 14, 'r': 13, 'u': 16, 't': 15, 'w': 18, 'v': 17, 'y': 20, 'x': 19, 'z': 21}, 'd': {'-': 50, 'a': 3, 'c': 1, 'b': 2, 'e': 1, 'd': 0, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 7, 'j': 6, 'm': 9, 'l': 8, 'o': 11, 'n': 10, 'q': 13, 'p': 12, 's': 15, 'r': 14, 'u': 17, 't': 16, 'w': 19, 'v': 18, 'y': 21, 'x': 20, 'z': 22}, 'g': {'-': 50, 'a': 6, 'c': 4, 'b': 5, 'e': 2, 'd': 3, 'g': 0, 'f': 1, 'i': 2, 'h': 1, 'k': 4, 'j': 3, 'm': 6, 'l': 5, 'o': 8, 'n': 7, 'q': 10, 'p': 9, 's': 12, 'r': 11, 'u': 14, 't': 13, 'w': 16, 'v': 15, 'y': 18, 'x': 17, 'z': 19}, 'f': {'-': 50, 'a': 5, 'c': 3, 'b': 4, 'e': 1, 'd': 2, 'g': 1, 'f': 0, 'i': 3, 'h': 2, 'k': 5, 'j': 4, 'm': 7, 'l': 6, 'o': 9, 'n': 8, 'q': 11, 'p': 10, 's': 13, 'r': 12, 'u': 15, 't': 14, 'w': 17, 'v': 16, 'y': 19, 'x': 18, 'z': 20}, 'i': {'-': 50, 'a': 8, 'c': 6, 'b': 7, 'e': 4, 'd': 5, 'g': 2, 'f': 3, 'i': 0, 'h': 1, 'k': 2, 'j': 1, 'm': 4, 'l': 3, 'o': 6, 'n': 5, 'q': 8, 'p': 7, 's': 10, 'r': 9, 'u': 12, 't': 11, 'w': 14, 'v': 13, 'y': 16, 'x': 15, 'z': 17}, 'h': {'-': 50, 'a': 7, 'c': 5, 'b': 6, 'e': 3, 'd': 4, 'g': 1, 'f': 2, 'i': 1, 'h': 0, 'k': 3, 'j': 2, 'm': 5, 'l': 4, 'o': 7, 'n': 6, 'q': 9, 'p': 8, 's': 11, 'r': 10, 'u': 13, 't': 12, 'w': 15, 'v': 14, 'y': 17, 'x': 16, 'z': 18}, 'k': {'-': 50, 'a': 10, 'c': 8, 'b': 9, 'e': 6, 'd': 7, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 0, 'j': 1, 'm': 2, 'l': 1, 'o': 4, 'n': 3, 'q': 6, 'p': 5, 's': 8, 'r': 7, 'u': 10, 't': 9, 'w': 12, 'v': 11, 'y': 14, 'x': 13, 'z': 15}, 'j': {'-': 50, 'a': 9, 'c': 7, 'b': 8, 'e': 5, 'd': 6, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 1, 'j': 0, 'm': 3, 'l': 2, 'o': 5, 'n': 4, 'q': 7, 'p': 6, 's': 9, 'r': 8, 'u': 11, 't': 10, 'w': 13, 'v': 12, 'y': 15, 'x': 14, 'z': 16}, 'm': {'-': 50, 'a': 12, 'c': 10, 'b': 11, 'e': 8, 'd': 9, 'g': 6, 'f': 7, 'i': 4, 'h': 5, 'k': 2, 'j': 3, 'm': 0, 'l': 1, 'o': 2, 'n': 1, 'q': 4, 'p': 3, 's': 6, 'r': 5, 'u': 8, 't': 7, 'w': 10, 'v': 9, 'y': 12, 'x': 11, 'z': 13}, 'l': {'-': 50, 'a': 11, 'c': 9, 'b': 10, 'e': 7, 'd': 8, 'g': 5, 'f': 6, 'i': 3, 'h': 4, 'k': 1, 'j': 2, 'm': 1, 'l': 0, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 7, 'r': 6, 'u': 9, 't': 8, 'w': 11, 'v': 10, 'y': 13, 'x': 12, 'z': 14}, 'o': {'-': 50, 'a': 14, 'c': 12, 'b': 13, 'e': 10, 'd': 11, 'g': 8, 'f': 9, 'i': 6, 'h': 7, 'k': 4, 'j': 5, 'm': 2, 'l': 3, 'o': 0, 'n': 1, 'q': 2, 'p': 1, 's': 4, 'r': 3, 'u': 6, 't': 5, 'w': 8, 'v': 7, 'y': 10, 'x': 9, 'z': 11}, 'n': {'-': 50, 'a': 13, 'c': 11, 'b': 12, 'e': 9, 'd': 10, 'g': 7, 'f': 8, 'i': 5, 'h': 6, 'k': 3, 'j': 4, 'm': 1, 'l': 2, 'o': 1, 'n': 0, 'q': 3, 'p': 2, 's': 5, 'r': 4, 'u': 7, 't': 6, 'w': 9, 'v': 8, 'y': 11, 'x': 10, 'z': 12}, 'q': {'-': 50, 'a': 16, 'c': 14, 'b': 15, 'e': 12, 'd': 13, 'g': 10, 'f': 11, 'i': 8, 'h': 9, 'k': 6, 'j': 7, 'm': 4, 'l': 5, 'o': 2, 'n': 3, 'q': 0, 'p': 1, 's': 2, 'r': 1, 'u': 4, 't': 3, 'w': 6, 'v': 5, 'y': 8, 'x': 7, 'z': 9}, 'p': {'-': 50, 'a': 15, 'c': 13, 'b': 14, 'e': 11, 'd': 12, 'g': 9, 'f': 10, 'i': 7, 'h': 8, 'k': 5, 'j': 6, 'm': 3, 'l': 4, 'o': 1, 'n': 2, 'q': 1, 'p': 0, 's': 3, 'r': 2, 'u': 5, 't': 4, 'w': 7, 'v': 6, 'y': 9, 'x': 8, 'z': 10}, 's': {'-': 50, 'a': 18, 'c': 16, 'b': 17, 'e': 14, 'd': 15, 'g': 12, 'f': 13, 'i': 10, 'h': 11, 'k': 8, 'j': 9, 'm': 6, 'l': 7, 'o': 4, 'n': 5, 'q': 2, 'p': 3, 's': 0, 'r': 1, 'u': 2, 't': 1, 'w': 4, 'v': 3, 'y': 6, 'x': 5, 'z': 7}, 'r': {'-': 50, 'a': 17, 'c': 15, 'b': 16, 'e': 13, 'd': 14, 'g': 11, 'f': 12, 'i': 9, 'h': 10, 'k': 7, 'j': 8, 'm': 5, 'l': 6, 'o': 3, 'n': 4, 'q': 1, 'p': 2, 's': 1, 'r': 0, 'u': 3, 't': 2, 'w': 5, 'v': 4, 'y': 7, 'x': 6, 'z': 8}, 'u': {'-': 50, 'a': 20, 'c': 18, 'b': 19, 'e': 16, 'd': 17, 'g': 14, 'f': 15, 'i': 12, 'h': 13, 'k': 10, 'j': 11, 'm': 8, 'l': 9, 'o': 6, 'n': 7, 'q': 4, 'p': 5, 's': 2, 'r': 3, 'u': 0, 't': 1, 'w': 2, 'v': 1, 'y': 4, 'x': 3, 'z': 5}, 't': {'-': 50, 'a': 19, 'c': 17, 'b': 18, 'e': 15, 'd': 16, 'g': 13, 'f': 14, 'i': 11, 'h': 12, 'k': 9, 'j': 10, 'm': 7, 'l': 8, 'o': 5, 'n': 6, 'q': 3, 'p': 4, 's': 1, 'r': 2, 'u': 1, 't': 0, 'w': 3, 'v': 2, 'y': 5, 'x': 4, 'z': 6}, 'w': {'-': 50, 'a': 22, 'c': 20, 'b': 21, 'e': 18, 'd': 19, 'g': 16, 'f': 17, 'i': 14, 'h': 15, 'k': 12, 'j': 13, 'm': 10, 'l': 11, 'o': 8, 'n': 9, 'q': 6, 'p': 7, 's': 4, 'r': 5, 'u': 2, 't': 3, 'w': 0, 'v': 1, 'y': 2, 'x': 1, 'z': 3}, 'v': {'-': 50, 'a': 21, 'c': 19, 'b': 20, 'e': 17, 'd': 18, 'g': 15, 'f': 16, 'i': 13, 'h': 14, 'k': 11, 'j': 12, 'm': 9, 'l': 10, 'o': 7, 'n': 8, 'q': 5, 'p': 6, 's': 3, 'r': 4, 'u': 1, 't': 2, 'w': 1, 'v': 0, 'y': 3, 'x': 2, 'z': 4}, 'y': {'-': 50, 'a': 24, 'c': 22, 'b': 23, 'e': 20, 'd': 21, 'g': 18, 'f': 19, 'i': 16, 'h': 17, 'k': 14, 'j': 15, 'm': 12, 'l': 13, 'o': 10, 'n': 11, 'q': 8, 'p': 9, 's': 6, 'r': 7, 'u': 4, 't': 5, 'w': 2, 'v': 3, 'y': 0, 'x': 1, 'z': 1}, 'x': {'-': 50, 'a': 23, 'c': 21, 'b': 22, 'e': 19, 'd': 20, 'g': 17, 'f': 18, 'i': 15, 'h': 16, 'k': 13, 'j': 14, 'm': 11, 'l': 12, 'o': 9, 'n': 10, 'q': 7, 'p': 8, 's': 5, 'r': 6, 'u': 3, 't': 4, 'w': 1, 'v': 2, 'y': 1, 'x': 0, 'z': 2}, 'z': {'-': 50, 'a': 25, 'c': 23, 'b': 24, 'e': 21, 'd': 22, 'g': 19, 'f': 20, 'i': 17, 'h': 18, 'k': 15, 'j': 16, 'm': 13, 'l': 14, 'o': 11, 'n': 12, 'q': 9, 'p': 10, 's': 7, 'r': 8, 'u': 5, 't': 6, 'w': 3, 'v': 4, 'y': 1, 'x': 2, 'z': 0}}

        self.assertEqual(min_difference('visdfpl', 'sxwmkerfdzc', R), 227)

    def test_diff_failed3(self):
        R = {'-': {'-': 0, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'a': {'-': 1, 'a': 0, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'c': {'-': 1, 'a': 1, 'c': 0, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'b': {'-': 1, 'a': 1, 'c': 1, 'b': 0, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'e': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 0, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'd': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 0, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'g': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 0, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'f': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 0, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'i': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 0, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'h': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 0, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'k': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 0, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'j': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 0, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'm': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 0, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'l': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 0, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'o': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 0, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'n': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 0, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'q': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 0, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'p': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 0, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 's': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 0, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'r': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 0, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'u': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 0, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 't': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 0, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'w': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 0, 'v': 1, 'y': 1, 'x': 1, 'z': 1}, 'v': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 0, 'y': 1, 'x': 1, 'z': 1}, 'y': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 0, 'x': 1, 'z': 1}, 'x': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 0, 'z': 1}, 'z': {'-': 1, 'a': 1, 'c': 1, 'b': 1, 'e': 1, 'd': 1, 'g': 1, 'f': 1, 'i': 1, 'h': 1, 'k': 1, 'j': 1, 'm': 1, 'l': 1, 'o': 1, 'n': 1, 'q': 1, 'p': 1, 's': 1, 'r': 1, 'u': 1, 't': 1, 'w': 1, 'v': 1, 'y': 1, 'x': 1, 'z': 0}}

        self.assertEqual(min_difference('ljo', 'bwlekxcjotfqnrayu', R), 14)
    '''
    def est_align_sanity(self):
        """Simple alignment

        Passes if the returned alignment matches the expected one.
        """
        # QWERTY resemblance matrix:
        R = qwerty_distance()
        diff, u, r = min_difference_align("polynomial", "exponential", R)
        # Warning: we may (read: 'will') use another matrix!
        self.assertEqual(diff, 15)
        # Warning: there may be other optimal matchings!
        self.assertEqual(u, '--polyn-om-ial')
        self.assertEqual(r, 'exp-o-ne-ntial')

if __name__ == '__main__':
    unittest.main()
