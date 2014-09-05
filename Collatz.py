__author__ = 'miles'

'''
The Collatz Conjecture

'''

# if even, n / 2
# if odd, n * 3 + 1
# stop when n = 1.
# fail for 2 ** n

def collatz_solve(a,b):

    from datetime import datetime
    startTime = datetime.now()

    cycle_dict = {}
    value_list = []

    # Collatz Algorithm: test all integers in the inclusive range [a,b]
    # Returns integer with longest cycle length and cycle length. >>> max_n max_cycle
    for n in range(a,b+1):

        if not(n in cycle_dict.keys()):

            seq = []   # reset the sequence for each integer tested
            length = 1 # reset the cycle count for each integer tested

            while (n!= 1):  # entry condition for algorithm
                seq.append(n)

                if( n % 2 == 0): # even operation
                    n = n // 2
                    length += 1

                else:             # odd operation
                    n = n * 3 + 1
                    length += 1
            seq.append(1)

            for i in range(len(seq)):
                if not(seq[i] in cycle_dict.keys()):
                    cycle_dict[seq[i]] = len(seq[i:])

    for i in range(a,b+1):
        value_list.append(cycle_dict[i])

    value_list.sort(reverse=True)


    print(a,b,value_list[0])
    print(datetime.now()-startTime)






def main():

    collatz_solve(1,10)
    collatz_solve(100,200)
    collatz_solve(201,210)
    collatz_solve(900,1000)

main()
