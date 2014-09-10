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
# collatz_eval
# ------------

def collatz_eval (a,b) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    m = b//2 + 1

    while m > a:
        a = m
        m = b//2  + 1



    cycle_dict = {}
    value_list = []

    # Collatz Algorithm: test all integers in the inclusive range [a,b]
    # Returns integer with longest cycle length and cycle length. >>> max_n max_cycle
    for n in range(a,b+1):

        if not(n in cycle_dict.keys()): # integer cycle length not yet calculated

            seq = []   # reset the sequence for each integer tested


            while (n!= 1):  # entry condition for algorithm
                seq.append(n)

                if( n % 2 == 0): # even operation
                    n = n // 2

                else:             # odd operation
                    n = n * 3 + 1
            seq.append(1)


            for i in range(len(seq)):
                if not(seq[i] in cycle_dict.keys()): # if the calculated seq val not in keys, add key:value
                    cycle_dict[seq[i]] = len(seq[i:])

    for i in range(a,b+1): # all k:v pairs in cycle range
        value_list.append(cycle_dict[i])

    value_list.sort(reverse=True) # move longest cycle length to position[0]
    
    return value_list[0]


# -------------
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
