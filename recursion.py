#!/usr/env/bin python
#! -*- coding: utf-8 -*-
"""IS211 Assignment 14"""

def fibonnaci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a, b):
    # Used Khan Academy to understand the logic processing
    # khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, (a % b))

def compareTo(s1, s2):
    # this function recursively compares string length
    # but does not compare character values
    if not s1 and not s2:
        return 0
    elif not s2:
        return len(s1)
    elif not s1:
        return (0 - len(s2))
    else:
        return compareTo(s1[1:], s2[1:])