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
    M = initialize_matrix(u,r)
    M = construct_weight_1_matrix(u,r,M,R)

    print "TESTING SHIT"
    print M[0][2], M[2][0]
    print R[M[0][2]][M[2][0]]
    if R[M[0][2]][M[2][0]]:
        print "TRUE"

    print("printing Matrix")
    for row in M:
        for val in row:
            print'{:2}'.format(val),
        print

    print "result =", M[-1][-1]
    return M[-1][-1]
    # To get the resemblance between two letters, use code like this:
    # difference = R['a']['b']

def initialize_matrix(u,r):
    M = [[None for i in range (len(r)+2)]for j in range (len(u)+2)]

    # FFS!!! I = ROW! J = COLUMN!
    # OBS! Måste lägga till dash: - om len(u) != len(r)
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 and j < 2:
                M[i][j] = 0      # Set first 2x2 to 0
                continue
            elif j == 0:
                M[i][j] = r[i-2] # Set row labels
            elif i == 0:
                M[i][j] = u[j-2] # Set column labels
            elif i == 1:
                M[i][j] = j-1    # Set first column values
            elif j == 1:
                M[i][j] = i-1    # Set first row values
            else:
                M[i][j] = 0      # initialize remaining matrix

    return M


def construct_weight_1_matrix(u,r,M,R):
    for i in range(len(r)+2):
        for j in range(len(u)+2):
            if i < 2 or j < 2:                    # Ignore first 2 rows and columns
                continue
            differance = R[M[0][j]][M[i][0]]
            if i == j and not differance:         # If current row/column label match
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j], M[i][j-1], M[i-1][j-1])+1
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
