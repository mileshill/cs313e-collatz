__author__ = 'miles'

'''
The Collatz Conjecture

'''

# if even, n / 2
# if odd, n * 3 + 1
# stop when n = 1.
# fail for 2 ** n

def collatz_solve():

    from datetime import datetime
    startTime = datetime.now()

    f = input()
    read_list = f.split()
    a,b = [int(v) for v in read_list]
    rangeMin,rangeMax= read_list[0],read_list[1]

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
    print(rangeMin + " " + rangeMax + " " + str(value_list[0]))
    print(datetime.now()-startTime)
def main():

    collatz_solve()
    collatz_solve()
    collatz_solve()
    collatz_solve()

main()
