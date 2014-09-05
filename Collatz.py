__author__ = 'miles'

'''
The Collatz Conjecture

'''

# if even, n / 2
# if odd, n * 3 + 1
# stop when n = 1.
# fail for 2 ** n

def main(a,b):

    #a = input("Enter in lower range boundary: ")
    #b = input("Enter in upper range boundary: ")


    try:
        a = int(a)
    except:
        print("\n 'a' and 'b' must be integers")

        #user decision to continue
        user_input_error = input("Press C to continue or any key to quit: ")
        if(user_input_error == 'c' or user_input_error == "C"):
            main()
        else:
            print("Good bye")
            quit()

    try:
        b = int(b)
    except:
        print("\n 'a' and 'b' must be integers")

        #user decision to continue
        user_input_error = input("Press C to continue or any key to quit: ")
        if(user_input_error == 'c' or user_input_error == "C"):
            main()
        else:
            print("Good bye")
            quit()

    #length = 1
    max_length = 1
    max_seq = []

    # each of the below assertions are handled in the try/except block below.
    #assert a > 0 and type(a)== int     # positive integer
    #assert b > 0 and type(b)== int     # positive integer
    #assert a <= b                      # range must be of the form range(min,max)


    try:
        assert a > 0  and type(a) == int and b > 0 and type(b) == int and a <= b
    except:
        print("\n ==> 'a' and 'b' must be positive integers ")
        print(" ==> 'a' must be less than or equal to 'b': a <= b \n")


        #user decision to continue
        user_input_error = input("Press C to continue or any key to quit: ")
        if(user_input_error == 'c' or user_input_error == "C"):
            main()
        else:
            print("Good bye")
            quit()


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


    print( list(cycle_dict.items()))
    print(value_list)
    print(a,b,value_list[0])








main(1,10)
main(100,200)