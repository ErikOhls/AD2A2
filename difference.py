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
    Pre:    u and r is arrays of any length. R is the resemblance matrix that \
            holds the resemblance weight for each character in the alphabet.
    Post:   returns the minimum resemblance cost between the two strings u and r.
    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference("dinamck","dynamic",R) ==> 3
    """
    M = initialize_matrix(u,r,R)
    M = construct_weights(u,r,M,R)

    #print_matrix(M)

    return M[-1][-1]

# Solution to part c:
def min_difference_align(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:    u and r is arrays of any length. R is the resemblance matrix that \
            holds the resemblance weight for each character in the alphabet.
    Post:   returns two modified strings that shows the positioning of the minimum \
            difference and the minimum resemolance cost of the string.\

    Example: Let R be the resemblance matrix where every change and skip costs 1
             min_difference_align("dinamck","dynamic",R) ==>
                                    3, "dinam-ck", "dynamic-"
    """

    M = initialize_matrix(u,r,R)
    M = construct_weights(u,r,M,R)

    #print_matrix(M)

    return insert_dashes(u,r,R,M)


def initialize_matrix(u,r,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int[0..len(u)+2][0..len(r)+2]
    Pre:    u and r is arrays of any length. R is the resemblance matrix that \
            holds the resemblance cost for each character in the alphabet. \
    Post:   returns a matrix with the first row and column with labels and \
            the first row/column initialized with the appropriate edit \
            distances.

    Example: Let R be the resemblance matrix where every change and skip costs 1
    initialize_matrix("a","a",R)  ==> [[0,0,a][0,0,0][a,0,0]]
    initialize_matrix("aa","b",R) ==> [[0,0,b][0,0,1][a,1,0][a,1,0]]
    """
    M = [[None for i in range (len(r)+2)] for j in range (len(u)+2)]

    for y in range(len(u)+2):
    # Invariant: range(len(u)+2)
    # Variant: length(u+2)-i
        for x in range(len(r)+2):
        # Invariant: range(len(r)+2)
        # Variant: length(r+2)-i
            if y < 2 and x < 2:
                M[y][x] = 0      # Set first 2x2 to 0
                continue
            elif x == 0:
                M[y][x] = u[y-2] # Set column labels
            elif y == 0:
                M[y][x] = r[x-2] # Set row labels
            elif x == 1:
                M[y][x] = M[y-1][x] + R[M[y][0]]['-']   # Set first column values
            elif y == 1:
                M[y][x] = M[y][x-1] + R['-'][M[0][x]]   # Set first row values
            else:
                M[y][x] = 0      # initialize remaining matrix

    return M


def construct_weights(u,r,M,R):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int[0..len(u)+2][0..len(r)+2]
    Pre:    u and r is arrays of any length. R is the resemblance matrix that \
            holds the resemblance cost for each character in the alphabet. \
    Post:   returns a matrix with edit distances of subsets of the strings

    Example: Let R be the resemblance matrix where every change and skip costs 1
    initialize_matrix("a","a",R)  ==> [[0,0,a][0,0,0][a,0,0]]
    initialize_matrix("aa","b",R) ==> [[0,0,b][0,0,1][a,1,1][a,1,2]]
    """
    for y in range(len(u)+2):
    # Invariant: range(len(u)+2)
    # Variant: length(u+2)-i
        for x in range(len(r)+2):
        # Invariant: range(len(r)+2)
        # Variant: length(r+2)-i
            if y < 2 or x < 2: # Ignore first 2 rows and columns
                continue
            M[y][x] = min(M[y-1][x] + R[u[y-2]]['-'], M[y][x-1] + R['-'][r[x-2]], M[y-1][x-1] + R[u[y-2]][r[x-2]])
    return M


def insert_dashes(u, r, R, M):
    """
    Sig:    string, string, int[0..|A|, 0..|A|] ==> int, string, string
    Pre:    u and r is arrays of any length. R is the resemblance matrix that \
            holds the resemblance cost for each character in the alphabet. \
            M is a valid edit distiance matrix
    Post:   returns and the minimum resemolance cost of the string and two \
    modified strings that shows the positioning of the minimum \
    difference\

    Example: Let R be the resemblance matrix where every change and skip costs 1
    min_difference_align("dinamck","dynamic",R,M) ==>
    3, "dinam-ck", "dynamic-"
    """
    x = len(r)+1
    y = len(u)+1

    u_dashed = ""
    r_dashed = ""
    while x > 1 or y > 1:
    # Invariant: 1
    # Variant: x, y

        if(x == 1):
            y = y-1
            r_dashed = "-" + r_dashed
            u_dashed = u[-1] + u_dashed
            u = u[:-1]


        elif (y == 1):
            x = x-1
            u_dashed = "-" + u_dashed
            r_dashed = r[-1] + r_dashed
            r = r[:-1]

        elif M[0][x] == M[y][0]:
            u_dashed = u[-1] + u_dashed
            u = u[:-1]
            r_dashed = r[-1] + r_dashed
            r = r[:-1]
            x -= 1
            y -= 1

        else:
            dif_above = R[u[-1]]['-']
            dif_left = R['-'][r[-1]]
            current = M[y][x]
            above = M[y-1][x]
            left = M[y][x-1]

            if current == dif_above + above:
                y -= 1
                r_dashed = "-" + r_dashed
                u_dashed = u[-1] + u_dashed
                u = u[:-1]
            elif current == dif_left + left:
                x -= 1
                u_dashed = "-" + u_dashed
                r_dashed = r[-1] + r_dashed
                r = r[:-1]
            else:
                u_dashed = u[-1] + u_dashed
                u = u[:-1]
                r_dashed = r[-1] + r_dashed
                r = r[:-1]
                x -= 1
                y -= 1

    result = 0

    for i in range(len(u_dashed)):
    # Invariant range(u_dashed)
    # Variant length(u_dashed)-i
        result += R[u_dashed[i]][r_dashed[i]]
    return result , u_dashed, r_dashed

def print_matrix(M):
    """
    Generates a easily readable matrix.
    Change i in {:i} the change cell size
    """
    print("printing Matrix")
    for row in M:
        for val in row:
            print'{:3}'.format(val),
        print

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
    ''''''
    def test_diff_one_equal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference("a","a",R),0)

    def test_diff_one_unequal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference("b","a",R),1)

    def test_diff_calle_banan(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference("calle","banan",R),4)

    def test_diff_all_unequal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference("aaaaaaaaaaaaaaa","bbbbbbbbbbbbbbb",R),15)

    def test_diff_all_equal(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference("aaaaaaaaaaaaaaa","aaaaaaaaaaaaaaa",R),0)

    def test_diff_12(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference('aa', 'b', R), 2)

    def test_diff_failed(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 1) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference('iacxoey', 'yjavik', R), 7)

    def test_diff_test(self):
        alphabet = ascii_lowercase + '-'
        R = dict( [ (
                     a,
                     dict( [ ( b, (0 if a==b else 2) ) for b in alphabet ] )
                    ) for a in alphabet ] )
        self.assertEqual(min_difference('iacxoey', 'yjavik', R), 14)

    """ALIGNMENT TESTs --------------------"""

    def test_align_sanity(self):
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
