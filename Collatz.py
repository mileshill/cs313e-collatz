#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# import cache functionality
# ------------
from functools import lru_cache

# ------------
# collatz_eval
# ------------

@lru_cache(maxsize=512)
def collatz_eval(i ,j):

    b = max(i,j)
    a = min(i,j)
    m= b//2 + 1
    if m > a:
        a=m


    length = 1
    max_length = 1
    #applying the "Hailstone Algorithm" to the user defined range
    for n in range(a,b+1): # inclusive range of user defined variables

        while (n != 1):

            if (n%2):
                n = n + n//2 +1
                length += 2
            else:		  		#even procedure
                n = n//2			# n + n//2 + 1
                length += 1


        if (length > max_length): 	#test the sequence length for each loop
            max_length = length +1  	#reassigns max_length to longest sequence

        length = 0                	#resets the length value for the next loop

    return max_length# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
import sys

#from Collatz import collatz_solve

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
