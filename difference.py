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
[0,    50, 100, 150, 200, 250]
[50,    5,  50, 100, 150, 200]
[100,  55,  18,  58, 108, 158]
[150, 104,  64,  32,  61, 111]
[200, 154, 114,  71,  50,  71]
[250, 204, 164, 121,  93,  64]
[300, 254, 214, 169, 137, 101]
[350, 304, 264, 219, 187, 149]
    '''
    print r, u
    M = initialize_matrix(u,r,R)
    M = construct_weight_new(u,r,M,R)

    print("printing Matrix")
    for row in M:
        for val in row:
            print'{:3}'.format(val),
        print

    return M[-1][-1]

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

    M = initialize_matrix(u,r,R)

    M = construct_weight_new(u,r,M,R)

    print("printing Matrix")
    for row in M:
        for val in row:
            print'{:2}'.format(val),
        print

    return insert_dashes2(u,r,R,M)

def insert_dashes2(u, r, R, M):
    do_print = True
    print "---------------------------------------------------------"
    x = len(r)+1
    y = len(u)+1

    u_dashed = ""
    r_dashed = ""
    while x > 1 or y > 1:
        if (do_print): print "\nlooking at", M[0][x], M[y][0]
        print u_dashed, r_dashed

        if(x == 1):
            if (do_print): print "REACHED LEFT"
            if (do_print): print "adding dash to:", u
            y = y-1
            r_dashed = "-" + r_dashed
            u_dashed = u[-1] + u_dashed
            u = u[:-1]

        elif (y == 1):
            if (do_print): print "REACHED TOP"
            if (do_print): print "adding dash to:", r
            x = x-1
            u_dashed = "-" + u_dashed
            r_dashed = r[-1] + r_dashed
            r = r[:-1]

         #'--polyn-om-ial'
         #'exp-o-ne-ntial'
        else:
            above = R['-'][u[-1]]
            left = R[r[-1]]['-']
            current = R[r[-1]][u[-1]]

            if (do_print):
                print "above:", above, "left:", left, "Curr:", current

            cheapest = min(above, left, current)
            if cheapest == left:
                if (do_print): print "adding dash to:", u
                x -= 1
                u_dashed = "-" + u_dashed
                r_dashed = r[-1] + r_dashed
                r = r[:-1]
            elif cheapest == above:
                if (do_print): print "adding dash to:", r
                y -= 1
                r_dashed = "-" + r_dashed
                u_dashed = u[-1] + u_dashed
                u = u[:-1]
            else:
                if (do_print): print "adding letters to dashed:", u[-1], r[-1]
                u_dashed = u[-1] + u_dashed
                u = u[:-1]
                r_dashed = r[-1] + r_dashed
                r = r[:-1]
                x -= 1
                y -= 1

    if (do_print):
        print "TEST", R['e']['a'], R['e']['w'], R['j']['w']
        print "new strings:"
        print u_dashed
        print r_dashed
    result = 0
    for i in range(len(u_dashed)):
        result += R[u_dashed[i]][r_dashed[i]]
        if (do_print): print "R[", u_dashed[i], "][", r_dashed[i], "] = ", R[u_dashed[i]][r_dashed[i]]

    if (do_print): print "REULTAT", result
    return result, u_dashed, r_dashed

def insert_dashes(u, r, R, M):
    do_print = True
    print "---------------------------------------------------------"
    x = len(r)+1
    y = len(u)+1

    u_dashed = ""
    r_dashed = ""
    while x > 1 or y > 1:
        if (do_print): print "\nlooking at", M[0][x], M[y][0]
        print u_dashed, r_dashed
        '''
        current = M[y][x]
        above = M[y-1][x]
        left = M[y][x-1]
        diagonal = M[y-1][x-1]
        '''

        current = R[M[0][x]][M[y][0]]
        above = R[M[y-1][0]]['-']
        left = R[M[0][x-1]]['-']
        diagonal = R[M[0][x-1]][M[y-1][0]]

        if(x == 1):
            if (do_print): print "REACHED LEFT"
            if (do_print): print "adding dash to:", u
            y = y-1
            r_dashed = "-" + r_dashed
            u_dashed = u[-1] + u_dashed
            u = u[:-1]

        elif (y == 1):
            if (do_print): print "REACHED TOP"
            if (do_print): print "adding dash to:", r
            x = x-1
            u_dashed = "-" + u_dashed
            r_dashed = r[-1] + r_dashed
            r = r[:-1]

        else:
            
            if (do_print):
                if (diagonal < above and diagonal < left): print "diagonal < left/above"
                if (diagonal <= current and left >= diagonal and above >= diagonal): print "diagonal <= current, left/above >= diagonal"
                if (M[0][x] == M[y][0]): print M[0][x], "==", M[y][0
]
            if (diagonal < above and diagonal < left)\
            or (diagonal <= current and left >= diagonal and above >= diagonal)\
            or (M[0][x] == M[y][0]):
                if (do_print): print "adding letters to dashed:", u[-1], r[-1]
                u_dashed = u[-1] + u_dashed
                u = u[:-1]
                r_dashed = r[-1] + r_dashed
                r = r[:-1]
                x -= 1
                y -= 1

            else:
                if left > above:
                    if (do_print): print "adding dash to:", r
                    y -= 1
                    r_dashed = "-" + r_dashed
                    u_dashed = u[-1] + u_dashed
                    u = u[:-1]
                else:
                    if (do_print): print "adding dash to:", u
                    x -= 1
                    u_dashed = "-" + u_dashed
                    r_dashed = r[-1] + r_dashed
                    r = r[:-1]

    if (do_print):
        print "TEST", R['e']['a'], R['e']['w'], R['j']['w']
        print "new strings:"
        print u_dashed
        print r_dashed
    result = 0
    for i in range(len(u_dashed)):
        result += R[u_dashed[i]][r_dashed[i]]
        if (do_print): print "R[", u_dashed[i], "][", r_dashed[i], "] = ", R[u_dashed[i]][r_dashed[i]]
        #result += R[r_dashed[i]][u_dashed[i]]
        #if (do_print): print "R[", r_dashed[i], "][", u_dashed[i], "] = ", R[r_dashed[i]][u_dashed[i]]
    if (do_print): print "REULTAT", result
    return result, u_dashed, r_dashed

def initialize_matrix(u,r,R):
    M = [[None for i in range (len(r)+2)] for j in range (len(u)+2)]

    for y in range(len(u)+2):
        for x in range(len(r)+2):
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

def construct_weight_new(u,r,M,R):
    for y in range(len(u)+2):
        for x in range(len(r)+2):
            if y < 2 or x < 2: # Ignore first 2 rows and columns
                continue
            M[y][x] = min(M[y-1][x] + R[u[y-2]]['-'], M[y][x-1] + R['-'][r[x-2]], M[y-1][x-1] + R[u[y-2]][r[x-2]])
    return M

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
    '''  '''
    ''' '''
    def test_diff_pow(self):
        R = ({'-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1, 'm': 2, 'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2, 'y': 2, 'x': 3, 'z': 3}, 'a': {'-': 1, 'a': 0, 'c': 3, 'b': 5, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 7, 'l': 8, 'o': 9, 'n': 6, 'q': 1, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 4, 'y': 6, 'x': 2, 'z': 1}, 'c': {'-': 2, 'a': 3, 'c': 0, 'b': 2, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 4, 'l': 7, 'o': 8, 'n': 3, 'q': 4, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 3, 'v': 1, 'y': 5, 'x': 1, 'z': 2}, 'b': {'-': 2, 'a': 5, 'c': 2, 'b': 0, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 2, 'l': 5, 'o': 6, 'n': 1, 'q': 6, 'p': 7, 's': 4, 'r': 3, 'u': 4, 't': 2, 'w': 5, 'v': 1, 'y': 3, 'x': 3, 'z': 4}, 'e': {'-': 2, 'a': 3, 'c': 2, 'b': 4, 'e': 0, 'd': 1, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 6, 'j': 5, 'm': 6, 'l': 7, 'o': 6, 'n': 5, 'q': 2, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 1, 'v': 3, 'y': 3, 'x': 3, 'z': 4}, 'd': {'-': 3, 'a': 2, 'c': 1, 'b': 3, 'e': 1, 'd': 0, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 5, 'l': 6, 'o': 7, 'n': 4, 'q': 3, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 2, 'v': 2, 'y': 4, 'x': 2, 'z': 3}, 'g': {'-': 3, 'a': 4, 'c': 3, 'b': 1, 'e': 3, 'd': 2, 'g': 0, 'f': 1, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 3, 'l': 4, 'o': 5, 'n': 2, 'q': 5, 'p': 6, 's': 3, 'r': 2, 'u': 3, 't': 1, 'w': 4, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'f': {'-': 3, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 0, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 4, 'l': 5, 'o': 6, 'n': 3, 'q': 4, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 3, 'v': 1, 'y': 3, 'x': 3, 'z': 4}, 'i': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 5, 'd': 6, 'g': 4, 'f': 5, 'i': 0, 'h': 3, 'k': 1, 'j': 2, 'm': 3, 'l': 2, 'o': 1, 'n': 4, 'q': 7, 'p': 2, 's': 7, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 6, 'y': 2, 'x': 8, 'z': 9}, 'h': {'-': 3, 'a': 5, 'c': 4, 'b': 2, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 0, 'k': 2, 'j': 1, 'm': 2, 'l': 3, 'o': 4, 'n': 1, 'q': 6, 'p': 5, 's': 4, 'r': 3, 'u': 2, 't': 2, 'w': 5, 'v': 3, 'y': 1, 'x': 5, 'z': 6}, 'k': {'-': 3, 'a': 7, 'c': 6, 'b': 4, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 0, 'j': 1, 'm': 2, 'l': 1, 'o': 2, 'n': 3, 'q': 8, 'p': 3, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 5, 'y': 3, 'x': 7, 'z': 8}, 'j': {'-': 3, 'a': 6, 'c': 5, 'b': 3, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 1, 'j': 0, 'm': 1, 'l': 2, 'o': 3, 'n': 2, 'q': 7, 'p': 4, 's': 5, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 4, 'y': 2, 'x': 6, 'z': 7}, 'm': {'-': 2, 'a': 7, 'c': 4, 'b': 2, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 3, 'h': 2, 'k': 2, 'j': 1, 'm': 0, 'l': 3, 'o': 4, 'n': 1, 'q': 8, 'p': 5, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 3, 'y': 3, 'x': 5, 'z': 6}, 'l': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 7, 'd': 6, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 1, 'j': 2, 'm': 3, 'l': 0, 'o': 1, 'n': 4, 'q': 9, 'p': 2, 's': 7, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 6, 'y': 4, 'x': 8, 'z': 9}, 'o': {'-': 1, 'a': 9, 'c': 8, 'b': 6, 'e': 6, 'd': 7, 'g': 5, 'f': 6, 'i': 1, 'h': 4, 'k': 2, 'j': 3, 'm': 4, 'l': 1, 'o': 0, 'n': 5, 'q': 8, 'p': 1, 's': 8, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 7, 'y': 3, 'x': 9, 'z': 10}, 'n': {'-': 2, 'a': 6, 'c': 3, 'b': 1, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 1, 'l': 4, 'o': 5, 'n': 0, 'q': 7, 'p': 6, 's': 5, 'r': 4, 'u': 3, 't': 3, 'w': 6, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'q': {'-': 1, 'a': 1, 'c': 4, 'b': 6, 'e': 2, 'd': 3, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 8, 'j': 7, 'm': 8, 'l': 9, 'o': 8, 'n': 7, 'q': 0, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 5, 'y': 5, 'x': 3, 'z': 2}, 'p': {'-': 1, 'a': 10, 'c': 9, 'b': 7, 'e': 7, 'd': 8, 'g': 6, 'f': 7, 'i': 2, 'h': 5, 'k': 3, 'j': 4, 'm': 5, 'l': 2, 'o': 1, 'n': 6, 'q': 9, 'p': 0, 's': 9, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 8, 'y': 4, 'x': 10, 'z': 11}, 's': {'-': 2, 'a': 1, 'c': 2, 'b': 4, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 6, 'l': 7, 'o': 8, 'n': 5, 'q': 2, 'p': 9, 's': 0, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 3, 'y': 5, 'x': 1, 'z': 2}, 'r': {'-': 2, 'a': 4, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 5, 'j': 4, 'm': 5, 'l': 6, 'o': 5, 'n': 4, 'q': 3, 'p': 6, 's': 3, 'r': 0, 'u': 3, 't': 1, 'w': 2, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'u': {'-': 2, 'a': 7, 'c': 6, 'b': 4, 'e': 4, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 2, 'j': 1, 'm': 2, 'l': 3, 'o': 2, 'n': 3, 'q': 6, 'p': 3, 's': 6, 'r': 3, 'u': 0, 't': 2, 'w': 5, 'v': 5, 'y': 1, 'x': 7, 'z': 8}, 't': {'-': 2, 'a': 5, 'c': 4, 'b': 2, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 2, 'k': 4, 'j': 3, 'm': 4, 'l': 5, 'o': 4, 'n': 3, 'q': 4, 'p': 5, 's': 4, 'r': 1, 'u': 2, 't': 0, 'w': 3, 'v': 3, 'y': 1, 'x': 5, 'z': 6}, 'w': {'-': 1, 'a': 2, 'c': 3, 'b': 5, 'e': 1, 'd': 2, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 7, 'j': 6, 'm': 7, 'l': 8, 'o': 7, 'n': 6, 'q': 1, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 0, 'v': 4, 'y': 4, 'x': 2, 'z': 3}, 'v': {'-': 2, 'a': 4, 'c': 1, 'b': 1, 'e': 3, 'd': 2, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 3, 'l': 6, 'o': 7, 'n': 2, 'q': 5, 'p': 8, 's': 3, 'r': 2, 'u': 5, 't': 3, 'w': 4, 'v': 0, 'y': 4, 'x': 2, 'z': 3}, 'y': {'-': 2, 'a': 6, 'c': 5, 'b': 3, 'e': 3, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 3, 'j': 2, 'm': 3, 'l': 4, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 5, 'r': 2, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 0, 'x': 6, 'z': 7}, 'x': {'-': 1, 'a': 2, 'c': 1, 'b': 3, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 5, 'l': 8, 'o': 9, 'n': 4, 'q': 3, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 2, 'y': 6, 'x': 0, 'z': 1}, 'z': {'-': 1, 'a': 1, 'c': 2, 'b': 4, 'e': 4, 'd': 3, 'g': 5, 'f': 4, 'i': 9, 'h': 6, 'k': 8, 'j': 7, 'm': 6, 'l': 9, 'o': 10, 'n': 5, 'q': 2, 'p': 11, 's': 2, 'r': 5, 'u': 8, 't': 6, 'w': 3, 'v': 3, 'y': 7, 'x': 1, 'z': 0}})
        self.assertEqual(min_difference('pow', 'ltigdwh', R), 8)
    
    def test_diff_gad(self):
        R = ({'-': {'-': 0, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 1, 'i': 2, 'h': 1, 'k': 1, 'j': 1, 'm': 2, 'l': 2, 'o': 3, 'n': 2, 'q': 3, 'p': 3, 's': 2, 'r': 2, 'u': 2, 't': 2, 'w': 3, 'v': 2, 'y': 2, 'x': 3, 'z': 3}, 'a': {'-': 1, 'a': 0, 'c': 3, 'b': 5, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 7, 'l': 8, 'o': 9, 'n': 6, 'q': 1, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 4, 'y': 6, 'x': 2, 'z': 1}, 'c': {'-': 2, 'a': 3, 'c': 0, 'b': 2, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 4, 'l': 7, 'o': 8, 'n': 3, 'q': 4, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 3, 'v': 1, 'y': 5, 'x': 1, 'z': 2}, 'b': {'-': 2, 'a': 5, 'c': 2, 'b': 0, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 2, 'l': 5, 'o': 6, 'n': 1, 'q': 6, 'p': 7, 's': 4, 'r': 3, 'u': 4, 't': 2, 'w': 5, 'v': 1, 'y': 3, 'x': 3, 'z': 4}, 'e': {'-': 2, 'a': 3, 'c': 2, 'b': 4, 'e': 0, 'd': 1, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 6, 'j': 5, 'm': 6, 'l': 7, 'o': 6, 'n': 5, 'q': 2, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 1, 'v': 3, 'y': 3, 'x': 3, 'z': 4}, 'd': {'-': 3, 'a': 2, 'c': 1, 'b': 3, 'e': 1, 'd': 0, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 5, 'l': 6, 'o': 7, 'n': 4, 'q': 3, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 2, 'v': 2, 'y': 4, 'x': 2, 'z': 3}, 'g': {'-': 3, 'a': 4, 'c': 3, 'b': 1, 'e': 3, 'd': 2, 'g': 0, 'f': 1, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 3, 'l': 4, 'o': 5, 'n': 2, 'q': 5, 'p': 6, 's': 3, 'r': 2, 'u': 3, 't': 1, 'w': 4, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'f': {'-': 3, 'a': 3, 'c': 2, 'b': 2, 'e': 2, 'd': 1, 'g': 1, 'f': 0, 'i': 5, 'h': 2, 'k': 4, 'j': 3, 'm': 4, 'l': 5, 'o': 6, 'n': 3, 'q': 4, 'p': 7, 's': 2, 'r': 1, 'u': 4, 't': 2, 'w': 3, 'v': 1, 'y': 3, 'x': 3, 'z': 4}, 'i': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 5, 'd': 6, 'g': 4, 'f': 5, 'i': 0, 'h': 3, 'k': 1, 'j': 2, 'm': 3, 'l': 2, 'o': 1, 'n': 4, 'q': 7, 'p': 2, 's': 7, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 6, 'y': 2, 'x': 8, 'z': 9}, 'h': {'-': 3, 'a': 5, 'c': 4, 'b': 2, 'e': 4, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 0, 'k': 2, 'j': 1, 'm': 2, 'l': 3, 'o': 4, 'n': 1, 'q': 6, 'p': 5, 's': 4, 'r': 3, 'u': 2, 't': 2, 'w': 5, 'v': 3, 'y': 1, 'x': 5, 'z': 6}, 'k': {'-': 3, 'a': 7, 'c': 6, 'b': 4, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 0, 'j': 1, 'm': 2, 'l': 1, 'o': 2, 'n': 3, 'q': 8, 'p': 3, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 5, 'y': 3, 'x': 7, 'z': 8}, 'j': {'-': 3, 'a': 6, 'c': 5, 'b': 3, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 1, 'j': 0, 'm': 1, 'l': 2, 'o': 3, 'n': 2, 'q': 7, 'p': 4, 's': 5, 'r': 4, 'u': 1, 't': 3, 'w': 6, 'v': 4, 'y': 2, 'x': 6, 'z': 7}, 'm': {'-': 2, 'a': 7, 'c': 4, 'b': 2, 'e': 6, 'd': 5, 'g': 3, 'f': 4, 'i': 3, 'h': 2, 'k': 2, 'j': 1, 'm': 0, 'l': 3, 'o': 4, 'n': 1, 'q': 8, 'p': 5, 's': 6, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 3, 'y': 3, 'x': 5, 'z': 6}, 'l': {'-': 2, 'a': 8, 'c': 7, 'b': 5, 'e': 7, 'd': 6, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 1, 'j': 2, 'm': 3, 'l': 0, 'o': 1, 'n': 4, 'q': 9, 'p': 2, 's': 7, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 6, 'y': 4, 'x': 8, 'z': 9}, 'o': {'-': 1, 'a': 9, 'c': 8, 'b': 6, 'e': 6, 'd': 7, 'g': 5, 'f': 6, 'i': 1, 'h': 4, 'k': 2, 'j': 3, 'm': 4, 'l': 1, 'o': 0, 'n': 5, 'q': 8, 'p': 1, 's': 8, 'r': 5, 'u': 2, 't': 4, 'w': 7, 'v': 7, 'y': 3, 'x': 9, 'z': 10}, 'n': {'-': 2, 'a': 6, 'c': 3, 'b': 1, 'e': 5, 'd': 4, 'g': 2, 'f': 3, 'i': 4, 'h': 1, 'k': 3, 'j': 2, 'm': 1, 'l': 4, 'o': 5, 'n': 0, 'q': 7, 'p': 6, 's': 5, 'r': 4, 'u': 3, 't': 3, 'w': 6, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'q': {'-': 1, 'a': 1, 'c': 4, 'b': 6, 'e': 2, 'd': 3, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 8, 'j': 7, 'm': 8, 'l': 9, 'o': 8, 'n': 7, 'q': 0, 'p': 9, 's': 2, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 5, 'y': 5, 'x': 3, 'z': 2}, 'p': {'-': 1, 'a': 10, 'c': 9, 'b': 7, 'e': 7, 'd': 8, 'g': 6, 'f': 7, 'i': 2, 'h': 5, 'k': 3, 'j': 4, 'm': 5, 'l': 2, 'o': 1, 'n': 6, 'q': 9, 'p': 0, 's': 9, 'r': 6, 'u': 3, 't': 5, 'w': 8, 'v': 8, 'y': 4, 'x': 10, 'z': 11}, 's': {'-': 2, 'a': 1, 'c': 2, 'b': 4, 'e': 2, 'd': 1, 'g': 3, 'f': 2, 'i': 7, 'h': 4, 'k': 6, 'j': 5, 'm': 6, 'l': 7, 'o': 8, 'n': 5, 'q': 2, 'p': 9, 's': 0, 'r': 3, 'u': 6, 't': 4, 'w': 1, 'v': 3, 'y': 5, 'x': 1, 'z': 2}, 'r': {'-': 2, 'a': 4, 'c': 3, 'b': 3, 'e': 1, 'd': 2, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 5, 'j': 4, 'm': 5, 'l': 6, 'o': 5, 'n': 4, 'q': 3, 'p': 6, 's': 3, 'r': 0, 'u': 3, 't': 1, 'w': 2, 'v': 2, 'y': 2, 'x': 4, 'z': 5}, 'u': {'-': 2, 'a': 7, 'c': 6, 'b': 4, 'e': 4, 'd': 5, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 2, 'j': 1, 'm': 2, 'l': 3, 'o': 2, 'n': 3, 'q': 6, 'p': 3, 's': 6, 'r': 3, 'u': 0, 't': 2, 'w': 5, 'v': 5, 'y': 1, 'x': 7, 'z': 8}, 't': {'-': 2, 'a': 5, 'c': 4, 'b': 2, 'e': 2, 'd': 3, 'g': 1, 'f': 2, 'i': 3, 'h': 2, 'k': 4, 'j': 3, 'm': 4, 'l': 5, 'o': 4, 'n': 3, 'q': 4, 'p': 5, 's': 4, 'r': 1, 'u': 2, 't': 0, 'w': 3, 'v': 3, 'y': 1, 'x': 5, 'z': 6}, 'w': {'-': 1, 'a': 2, 'c': 3, 'b': 5, 'e': 1, 'd': 2, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 7, 'j': 6, 'm': 7, 'l': 8, 'o': 7, 'n': 6, 'q': 1, 'p': 8, 's': 1, 'r': 2, 'u': 5, 't': 3, 'w': 0, 'v': 4, 'y': 4, 'x': 2, 'z': 3}, 'v': {'-': 2, 'a': 4, 'c': 1, 'b': 1, 'e': 3, 'd': 2, 'g': 2, 'f': 1, 'i': 6, 'h': 3, 'k': 5, 'j': 4, 'm': 3, 'l': 6, 'o': 7, 'n': 2, 'q': 5, 'p': 8, 's': 3, 'r': 2, 'u': 5, 't': 3, 'w': 4, 'v': 0, 'y': 4, 'x': 2, 'z': 3}, 'y': {'-': 2, 'a': 6, 'c': 5, 'b': 3, 'e': 3, 'd': 4, 'g': 2, 'f': 3, 'i': 2, 'h': 1, 'k': 3, 'j': 2, 'm': 3, 'l': 4, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 5, 'r': 2, 'u': 1, 't': 1, 'w': 4, 'v': 4, 'y': 0, 'x': 6, 'z': 7}, 'x': {'-': 1, 'a': 2, 'c': 1, 'b': 3, 'e': 3, 'd': 2, 'g': 4, 'f': 3, 'i': 8, 'h': 5, 'k': 7, 'j': 6, 'm': 5, 'l': 8, 'o': 9, 'n': 4, 'q': 3, 'p': 10, 's': 1, 'r': 4, 'u': 7, 't': 5, 'w': 2, 'v': 2, 'y': 6, 'x': 0, 'z': 1}, 'z': {'-': 1, 'a': 1, 'c': 2, 'b': 4, 'e': 4, 'd': 3, 'g': 5, 'f': 4, 'i': 9, 'h': 6, 'k': 8, 'j': 7, 'm': 6, 'l': 9, 'o': 10, 'n': 5, 'q': 2, 'p': 11, 's': 2, 'r': 5, 'u': 8, 't': 6, 'w': 3, 'v': 3, 'y': 7, 'x': 1, 'z': 0}})

        self.assertEqual(min_difference('nbqdfc', 'gad', R), 9)
    '''
    """ALIGNMENT TESTs --------------------"""
    ''''''
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
    '''
    def test_align_zh(self):
        R = {'-': {'-': 0, 'a': 50, 'c': 50, 'b': 50, 'e': 50, 'd': 50, 'g': 50, 'f': 50, 'i': 50, 'h': 50, 'k': 50, 'j': 50, 'm': 50, 'l': 50, 'o': 50, 'n': 50, 'q': 50, 'p': 50, 's': 50, 'r': 50, 'u': 50, 't': 50, 'w': 50, 'v': 50, 'y': 50, 'x': 50, 'z': 50}, 'a': {'-': 50, 'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25}, 'c': {'-': 50, 'a': 2, 'c': 0, 'b': 1, 'e': 2, 'd': 1, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 8, 'j': 7, 'm': 10, 'l': 9, 'o': 12, 'n': 11, 'q': 14, 'p': 13, 's': 16, 'r': 15, 'u': 18, 't': 17, 'w': 20, 'v': 19, 'y': 22, 'x': 21, 'z': 23}, 'b': {'-': 50, 'a': 1, 'c': 1, 'b': 0, 'e': 3, 'd': 2, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 9, 'j': 8, 'm': 11, 'l': 10, 'o': 13, 'n': 12, 'q': 15, 'p': 14, 's': 17, 'r': 16, 'u': 19, 't': 18, 'w': 21, 'v': 20, 'y': 23, 'x': 22, 'z': 24}, 'e': {'-': 50, 'a': 4, 'c': 2, 'b': 3, 'e': 0, 'd': 1, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 6, 'j': 5, 'm': 8, 'l': 7, 'o': 10, 'n': 9, 'q': 12, 'p': 11, 's': 14, 'r': 13, 'u': 16, 't': 15, 'w': 18, 'v': 17, 'y': 20, 'x': 19, 'z': 21}, 'd': {'-': 50, 'a': 3, 'c': 1, 'b': 2, 'e': 1, 'd': 0, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 7, 'j': 6, 'm': 9, 'l': 8, 'o': 11, 'n': 10, 'q': 13, 'p': 12, 's': 15, 'r': 14, 'u': 17, 't': 16, 'w': 19, 'v': 18, 'y': 21, 'x': 20, 'z': 22}, 'g': {'-': 50, 'a': 6, 'c': 4, 'b': 5, 'e': 2, 'd': 3, 'g': 0, 'f': 1, 'i': 2, 'h': 1, 'k': 4, 'j': 3, 'm': 6, 'l': 5, 'o': 8, 'n': 7, 'q': 10, 'p': 9, 's': 12, 'r': 11, 'u': 14, 't': 13, 'w': 16, 'v': 15, 'y': 18, 'x': 17, 'z': 19}, 'f': {'-': 50, 'a': 5, 'c': 3, 'b': 4, 'e': 1, 'd': 2, 'g': 1, 'f': 0, 'i': 3, 'h': 2, 'k': 5, 'j': 4, 'm': 7, 'l': 6, 'o': 9, 'n': 8, 'q': 11, 'p': 10, 's': 13, 'r': 12, 'u': 15, 't': 14, 'w': 17, 'v': 16, 'y': 19, 'x': 18, 'z': 20}, 'i': {'-': 50, 'a': 8, 'c': 6, 'b': 7, 'e': 4, 'd': 5, 'g': 2, 'f': 3, 'i': 0, 'h': 1, 'k': 2, 'j': 1, 'm': 4, 'l': 3, 'o': 6, 'n': 5, 'q': 8, 'p': 7, 's': 10, 'r': 9, 'u': 12, 't': 11, 'w': 14, 'v': 13, 'y': 16, 'x': 15, 'z': 17}, 'h': {'-': 50, 'a': 7, 'c': 5, 'b': 6, 'e': 3, 'd': 4, 'g': 1, 'f': 2, 'i': 1, 'h': 0, 'k': 3, 'j': 2, 'm': 5, 'l': 4, 'o': 7, 'n': 6, 'q': 9, 'p': 8, 's': 11, 'r': 10, 'u': 13, 't': 12, 'w': 15, 'v': 14, 'y': 17, 'x': 16, 'z': 18}, 'k': {'-': 50, 'a': 10, 'c': 8, 'b': 9, 'e': 6, 'd': 7, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 0, 'j': 1, 'm': 2, 'l': 1, 'o': 4, 'n': 3, 'q': 6, 'p': 5, 's': 8, 'r': 7, 'u': 10, 't': 9, 'w': 12, 'v': 11, 'y': 14, 'x': 13, 'z': 15}, 'j': {'-': 50, 'a': 9, 'c': 7, 'b': 8, 'e': 5, 'd': 6, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 1, 'j': 0, 'm': 3, 'l': 2, 'o': 5, 'n': 4, 'q': 7, 'p': 6, 's': 9, 'r': 8, 'u': 11, 't': 10, 'w': 13, 'v': 12, 'y': 15, 'x': 14, 'z': 16}, 'm': {'-': 50, 'a': 12, 'c': 10, 'b': 11, 'e': 8, 'd': 9, 'g': 6, 'f': 7, 'i': 4, 'h': 5, 'k': 2, 'j': 3, 'm': 0, 'l': 1, 'o': 2, 'n': 1, 'q': 4, 'p': 3, 's': 6, 'r': 5, 'u': 8, 't': 7, 'w': 10, 'v': 9, 'y': 12, 'x': 11, 'z': 13}, 'l': {'-': 50, 'a': 11, 'c': 9, 'b': 10, 'e': 7, 'd': 8, 'g': 5, 'f': 6, 'i': 3, 'h': 4, 'k': 1, 'j': 2, 'm': 1, 'l': 0, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 7, 'r': 6, 'u': 9, 't': 8, 'w': 11, 'v': 10, 'y': 13, 'x': 12, 'z': 14}, 'o': {'-': 50, 'a': 14, 'c': 12, 'b': 13, 'e': 10, 'd': 11, 'g': 8, 'f': 9, 'i': 6, 'h': 7, 'k': 4, 'j': 5, 'm': 2, 'l': 3, 'o': 0, 'n': 1, 'q': 2, 'p': 1, 's': 4, 'r': 3, 'u': 6, 't': 5, 'w': 8, 'v': 7, 'y': 10, 'x': 9, 'z': 11}, 'n': {'-': 50, 'a': 13, 'c': 11, 'b': 12, 'e': 9, 'd': 10, 'g': 7, 'f': 8, 'i': 5, 'h': 6, 'k': 3, 'j': 4, 'm': 1, 'l': 2, 'o': 1, 'n': 0, 'q': 3, 'p': 2, 's': 5, 'r': 4, 'u': 7, 't': 6, 'w': 9, 'v': 8, 'y': 11, 'x': 10, 'z': 12}, 'q': {'-': 50, 'a': 16, 'c': 14, 'b': 15, 'e': 12, 'd': 13, 'g': 10, 'f': 11, 'i': 8, 'h': 9, 'k': 6, 'j': 7, 'm': 4, 'l': 5, 'o': 2, 'n': 3, 'q': 0, 'p': 1, 's': 2, 'r': 1, 'u': 4, 't': 3, 'w': 6, 'v': 5, 'y': 8, 'x': 7, 'z': 9}, 'p': {'-': 50, 'a': 15, 'c': 13, 'b': 14, 'e': 11, 'd': 12, 'g': 9, 'f': 10, 'i': 7, 'h': 8, 'k': 5, 'j': 6, 'm': 3, 'l': 4, 'o': 1, 'n': 2, 'q': 1, 'p': 0, 's': 3, 'r': 2, 'u': 5, 't': 4, 'w': 7, 'v': 6, 'y': 9, 'x': 8, 'z': 10}, 's': {'-': 50, 'a': 18, 'c': 16, 'b': 17, 'e': 14, 'd': 15, 'g': 12, 'f': 13, 'i': 10, 'h': 11, 'k': 8, 'j': 9, 'm': 6, 'l': 7, 'o': 4, 'n': 5, 'q': 2, 'p': 3, 's': 0, 'r': 1, 'u': 2, 't': 1, 'w': 4, 'v': 3, 'y': 6, 'x': 5, 'z': 7}, 'r': {'-': 50, 'a': 17, 'c': 15, 'b': 16, 'e': 13, 'd': 14, 'g': 11, 'f': 12, 'i': 9, 'h': 10, 'k': 7, 'j': 8, 'm': 5, 'l': 6, 'o': 3, 'n': 4, 'q': 1, 'p': 2, 's': 1, 'r': 0, 'u': 3, 't': 2, 'w': 5, 'v': 4, 'y': 7, 'x': 6, 'z': 8}, 'u': {'-': 50, 'a': 20, 'c': 18, 'b': 19, 'e': 16, 'd': 17, 'g': 14, 'f': 15, 'i': 12, 'h': 13, 'k': 10, 'j': 11, 'm': 8, 'l': 9, 'o': 6, 'n': 7, 'q': 4, 'p': 5, 's': 2, 'r': 3, 'u': 0, 't': 1, 'w': 2, 'v': 1, 'y': 4, 'x': 3, 'z': 5}, 't': {'-': 50, 'a': 19, 'c': 17, 'b': 18, 'e': 15, 'd': 16, 'g': 13, 'f': 14, 'i': 11, 'h': 12, 'k': 9, 'j': 10, 'm': 7, 'l': 8, 'o': 5, 'n': 6, 'q': 3, 'p': 4, 's': 1, 'r': 2, 'u': 1, 't': 0, 'w': 3, 'v': 2, 'y': 5, 'x': 4, 'z': 6}, 'w': {'-': 50, 'a': 22, 'c': 20, 'b': 21, 'e': 18, 'd': 19, 'g': 16, 'f': 17, 'i': 14, 'h': 15, 'k': 12, 'j': 13, 'm': 10, 'l': 11, 'o': 8, 'n': 9, 'q': 6, 'p': 7, 's': 4, 'r': 5, 'u': 2, 't': 3, 'w': 0, 'v': 1, 'y': 2, 'x': 1, 'z': 3}, 'v': {'-': 50, 'a': 21, 'c': 19, 'b': 20, 'e': 17, 'd': 18, 'g': 15, 'f': 16, 'i': 13, 'h': 14, 'k': 11, 'j': 12, 'm': 9, 'l': 10, 'o': 7, 'n': 8, 'q': 5, 'p': 6, 's': 3, 'r': 4, 'u': 1, 't': 2, 'w': 1, 'v': 0, 'y': 3, 'x': 2, 'z': 4}, 'y': {'-': 50, 'a': 24, 'c': 22, 'b': 23, 'e': 20, 'd': 21, 'g': 18, 'f': 19, 'i': 16, 'h': 17, 'k': 14, 'j': 15, 'm': 12, 'l': 13, 'o': 10, 'n': 11, 'q': 8, 'p': 9, 's': 6, 'r': 7, 'u': 4, 't': 5, 'w': 2, 'v': 3, 'y': 0, 'x': 1, 'z': 1}, 'x': {'-': 50, 'a': 23, 'c': 21, 'b': 22, 'e': 19, 'd': 20, 'g': 17, 'f': 18, 'i': 15, 'h': 16, 'k': 13, 'j': 14, 'm': 11, 'l': 12, 'o': 9, 'n': 10, 'q': 7, 'p': 8, 's': 5, 'r': 6, 'u': 3, 't': 4, 'w': 1, 'v': 2, 'y': 1, 'x': 0, 'z': 2}, 'z': {'-': 50, 'a': 25, 'c': 23, 'b': 24, 'e': 21, 'd': 22, 'g': 19, 'f': 20, 'i': 17, 'h': 18, 'k': 15, 'j': 16, 'm': 13, 'l': 14, 'o': 11, 'n': 12, 'q': 9, 'p': 10, 's': 7, 'r': 8, 'u': 5, 't': 6, 'w': 3, 'v': 4, 'y': 1, 'x': 2, 'z': 0}}
        diff, u, r = min_difference_align('jkzehqogcistrx', 'xmsiokdcbt', R)
        self.assertEqual(diff, 240)
        self.assertEqual(u, 'jkzehqogcistrx')
        self.assertEqual(r, 'xms-iokdcb-t--')

    

    def test_align_ejodl(self):
        R = {'-': {'-': 0, 'a': 50, 'c': 50, 'b': 50, 'e': 50, 'd': 50, 'g': 50, 'f': 50, 'i': 50, 'h': 50, 'k': 50, 'j': 50, 'm': 50, 'l': 50, 'o': 50, 'n': 50, 'q': 50, 'p': 50, 's': 50, 'r': 50, 'u': 50, 't': 50, 'w': 50, 'v': 50, 'y': 50, 'x': 50, 'z': 50}, 'a': {'-': 50, 'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8, 'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16, 'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24, 'x': 23, 'z': 25}, 'c': {'-': 50, 'a': 2, 'c': 0, 'b': 1, 'e': 2, 'd': 1, 'g': 4, 'f': 3, 'i': 6, 'h': 5, 'k': 8, 'j': 7, 'm': 10, 'l': 9, 'o': 12, 'n': 11, 'q': 14, 'p': 13, 's': 16, 'r': 15, 'u': 18, 't': 17, 'w': 20, 'v': 19, 'y': 22, 'x': 21, 'z': 23}, 'b': {'-': 50, 'a': 1, 'c': 1, 'b': 0, 'e': 3, 'd': 2, 'g': 5, 'f': 4, 'i': 7, 'h': 6, 'k': 9, 'j': 8, 'm': 11, 'l': 10, 'o': 13, 'n': 12, 'q': 15, 'p': 14, 's': 17, 'r': 16, 'u': 19, 't': 18, 'w': 21, 'v': 20, 'y': 23, 'x': 22, 'z': 24}, 'e': {'-': 50, 'a': 4, 'c': 2, 'b': 3, 'e': 0, 'd': 1, 'g': 2, 'f': 1, 'i': 4, 'h': 3, 'k': 6, 'j': 5, 'm': 8, 'l': 7, 'o': 10, 'n': 9, 'q': 12, 'p': 11, 's': 14, 'r': 13, 'u': 16, 't': 15, 'w': 18, 'v': 17, 'y': 20, 'x': 19, 'z': 21}, 'd': {'-': 50, 'a': 3, 'c': 1, 'b': 2, 'e': 1, 'd': 0, 'g': 3, 'f': 2, 'i': 5, 'h': 4, 'k': 7, 'j': 6, 'm': 9, 'l': 8, 'o': 11, 'n': 10, 'q': 13, 'p': 12, 's': 15, 'r': 14, 'u': 17, 't': 16, 'w': 19, 'v': 18, 'y': 21, 'x': 20, 'z': 22}, 'g': {'-': 50, 'a': 6, 'c': 4, 'b': 5, 'e': 2, 'd': 3, 'g': 0, 'f': 1, 'i': 2, 'h': 1, 'k': 4, 'j': 3, 'm': 6, 'l': 5, 'o': 8, 'n': 7, 'q': 10, 'p': 9, 's': 12, 'r': 11, 'u': 14, 't': 13, 'w': 16, 'v': 15, 'y': 18, 'x': 17, 'z': 19}, 'f': {'-': 50, 'a': 5, 'c': 3, 'b': 4, 'e': 1, 'd': 2, 'g': 1, 'f': 0, 'i': 3, 'h': 2, 'k': 5, 'j': 4, 'm': 7, 'l': 6, 'o': 9, 'n': 8, 'q': 11, 'p': 10, 's': 13, 'r': 12, 'u': 15, 't': 14, 'w': 17, 'v': 16, 'y': 19, 'x': 18, 'z': 20}, 'i': {'-': 50, 'a': 8, 'c': 6, 'b': 7, 'e': 4, 'd': 5, 'g': 2, 'f': 3, 'i': 0, 'h': 1, 'k': 2, 'j': 1, 'm': 4, 'l': 3, 'o': 6, 'n': 5, 'q': 8, 'p': 7, 's': 10, 'r': 9, 'u': 12, 't': 11, 'w': 14, 'v': 13, 'y': 16, 'x': 15, 'z': 17}, 'h': {'-': 50, 'a': 7, 'c': 5, 'b': 6, 'e': 3, 'd': 4, 'g': 1, 'f': 2, 'i': 1, 'h': 0, 'k': 3, 'j': 2, 'm': 5, 'l': 4, 'o': 7, 'n': 6, 'q': 9, 'p': 8, 's': 11, 'r': 10, 'u': 13, 't': 12, 'w': 15, 'v': 14, 'y': 17, 'x': 16, 'z': 18}, 'k': {'-': 50, 'a': 10, 'c': 8, 'b': 9, 'e': 6, 'd': 7, 'g': 4, 'f': 5, 'i': 2, 'h': 3, 'k': 0, 'j': 1, 'm': 2, 'l': 1, 'o': 4, 'n': 3, 'q': 6, 'p': 5, 's': 8, 'r': 7, 'u': 10, 't': 9, 'w': 12, 'v': 11, 'y': 14, 'x': 13, 'z': 15}, 'j': {'-': 50, 'a': 9, 'c': 7, 'b': 8, 'e': 5, 'd': 6, 'g': 3, 'f': 4, 'i': 1, 'h': 2, 'k': 1, 'j': 0, 'm': 3, 'l': 2, 'o': 5, 'n': 4, 'q': 7, 'p': 6, 's': 9, 'r': 8, 'u': 11, 't': 10, 'w': 13, 'v': 12, 'y': 15, 'x': 14, 'z': 16}, 'm': {'-': 50, 'a': 12, 'c': 10, 'b': 11, 'e': 8, 'd': 9, 'g': 6, 'f': 7, 'i': 4, 'h': 5, 'k': 2, 'j': 3, 'm': 0, 'l': 1, 'o': 2, 'n': 1, 'q': 4, 'p': 3, 's': 6, 'r': 5, 'u': 8, 't': 7, 'w': 10, 'v': 9, 'y': 12, 'x': 11, 'z': 13}, 'l': {'-': 50, 'a': 11, 'c': 9, 'b': 10, 'e': 7, 'd': 8, 'g': 5, 'f': 6, 'i': 3, 'h': 4, 'k': 1, 'j': 2, 'm': 1, 'l': 0, 'o': 3, 'n': 2, 'q': 5, 'p': 4, 's': 7, 'r': 6, 'u': 9, 't': 8, 'w': 11, 'v': 10, 'y': 13, 'x': 12, 'z': 14}, 'o': {'-': 50, 'a': 14, 'c': 12, 'b': 13, 'e': 10, 'd': 11, 'g': 8, 'f': 9, 'i': 6, 'h': 7, 'k': 4, 'j': 5, 'm': 2, 'l': 3, 'o': 0, 'n': 1, 'q': 2, 'p': 1, 's': 4, 'r': 3, 'u': 6, 't': 5, 'w': 8, 'v': 7, 'y': 10, 'x': 9, 'z': 11}, 'n': {'-': 50, 'a': 13, 'c': 11, 'b': 12, 'e': 9, 'd': 10, 'g': 7, 'f': 8, 'i': 5, 'h': 6, 'k': 3, 'j': 4, 'm': 1, 'l': 2, 'o': 1, 'n': 0, 'q': 3, 'p': 2, 's': 5, 'r': 4, 'u': 7, 't': 6, 'w': 9, 'v': 8, 'y': 11, 'x': 10, 'z': 12}, 'q': {'-': 50, 'a': 16, 'c': 14, 'b': 15, 'e': 12, 'd': 13, 'g': 10, 'f': 11, 'i': 8, 'h': 9, 'k': 6, 'j': 7, 'm': 4, 'l': 5, 'o': 2, 'n': 3, 'q': 0, 'p': 1, 's': 2, 'r': 1, 'u': 4, 't': 3, 'w': 6, 'v': 5, 'y': 8, 'x': 7, 'z': 9}, 'p': {'-': 50, 'a': 15, 'c': 13, 'b': 14, 'e': 11, 'd': 12, 'g': 9, 'f': 10, 'i': 7, 'h': 8, 'k': 5, 'j': 6, 'm': 3, 'l': 4, 'o': 1, 'n': 2, 'q': 1, 'p': 0, 's': 3, 'r': 2, 'u': 5, 't': 4, 'w': 7, 'v': 6, 'y': 9, 'x': 8, 'z': 10}, 's': {'-': 50, 'a': 18, 'c': 16, 'b': 17, 'e': 14, 'd': 15, 'g': 12, 'f': 13, 'i': 10, 'h': 11, 'k': 8, 'j': 9, 'm': 6, 'l': 7, 'o': 4, 'n': 5, 'q': 2, 'p': 3, 's': 0, 'r': 1, 'u': 2, 't': 1, 'w': 4, 'v': 3, 'y': 6, 'x': 5, 'z': 7}, 'r': {'-': 50, 'a': 17, 'c': 15, 'b': 16, 'e': 13, 'd': 14, 'g': 11, 'f': 12, 'i': 9, 'h': 10, 'k': 7, 'j': 8, 'm': 5, 'l': 6, 'o': 3, 'n': 4, 'q': 1, 'p': 2, 's': 1, 'r': 0, 'u': 3, 't': 2, 'w': 5, 'v': 4, 'y': 7, 'x': 6, 'z': 8}, 'u': {'-': 50, 'a': 20, 'c': 18, 'b': 19, 'e': 16, 'd': 17, 'g': 14, 'f': 15, 'i': 12, 'h': 13, 'k': 10, 'j': 11, 'm': 8, 'l': 9, 'o': 6, 'n': 7, 'q': 4, 'p': 5, 's': 2, 'r': 3, 'u': 0, 't': 1, 'w': 2, 'v': 1, 'y': 4, 'x': 3, 'z': 5}, 't': {'-': 50, 'a': 19, 'c': 17, 'b': 18, 'e': 15, 'd': 16, 'g': 13, 'f': 14, 'i': 11, 'h': 12, 'k': 9, 'j': 10, 'm': 7, 'l': 8, 'o': 5, 'n': 6, 'q': 3, 'p': 4, 's': 1, 'r': 2, 'u': 1, 't': 0, 'w': 3, 'v': 2, 'y': 5, 'x': 4, 'z': 6}, 'w': {'-': 50, 'a': 22, 'c': 20, 'b': 21, 'e': 18, 'd': 19, 'g': 16, 'f': 17, 'i': 14, 'h': 15, 'k': 12, 'j': 13, 'm': 10, 'l': 11, 'o': 8, 'n': 9, 'q': 6, 'p': 7, 's': 4, 'r': 5, 'u': 2, 't': 3, 'w': 0, 'v': 1, 'y': 2, 'x': 1, 'z': 3}, 'v': {'-': 50, 'a': 21, 'c': 19, 'b': 20, 'e': 17, 'd': 18, 'g': 15, 'f': 16, 'i': 13, 'h': 14, 'k': 11, 'j': 12, 'm': 9, 'l': 10, 'o': 7, 'n': 8, 'q': 5, 'p': 6, 's': 3, 'r': 4, 'u': 1, 't': 2, 'w': 1, 'v': 0, 'y': 3, 'x': 2, 'z': 4}, 'y': {'-': 50, 'a': 24, 'c': 22, 'b': 23, 'e': 20, 'd': 21, 'g': 18, 'f': 19, 'i': 16, 'h': 17, 'k': 14, 'j': 15, 'm': 12, 'l': 13, 'o': 10, 'n': 11, 'q': 8, 'p': 9, 's': 6, 'r': 7, 'u': 4, 't': 5, 'w': 2, 'v': 3, 'y': 0, 'x': 1, 'z': 1}, 'x': {'-': 50, 'a': 23, 'c': 21, 'b': 22, 'e': 19, 'd': 20, 'g': 17, 'f': 18, 'i': 15, 'h': 16, 'k': 13, 'j': 14, 'm': 11, 'l': 12, 'o': 9, 'n': 10, 'q': 7, 'p': 8, 's': 5, 'r': 6, 'u': 3, 't': 4, 'w': 1, 'v': 2, 'y': 1, 'x': 0, 'z': 2}, 'z': {'-': 50, 'a': 25, 'c': 23, 'b': 24, 'e': 21, 'd': 22, 'g': 19, 'f': 20, 'i': 17, 'h': 18, 'k': 15, 'j': 16, 'm': 13, 'l': 14, 'o': 11, 'n': 12, 'q': 9, 'p': 10, 's': 7, 'r': 8, 'u': 5, 't': 6, 'w': 3, 'v': 4, 'y': 1, 'x': 2, 'z': 0}}

        diff, u, r = min_difference_align("ejodl", "jwavztx", R)
        self.assertEqual(diff, 149)
        self.assertEqual(u, 'e-jo-dl')
        self.assertEqual(u, 'jwavztx')
    '''
if __name__ == '__main__':
    unittest.main()
