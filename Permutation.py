n = 0
r = 0
FLAG = 0

def permutation(a,b):
    check_n = 0
    n_fact = 1
    n_minus_r_fact = 1
    while(check_n == 0):
        check_n = 1
        try:
            n = int(input("Enter the number of choices, n: "))
            r = int(input("Enter the number of elements, r: "))
            if (n < 0 or r < 0):
                print("Please enter a positve value")
                check_n = 0
            else:
                for i in range(1,n+1):
                   n_fact *= i
                   i += 1
                #print(n_fact)
                diff = (n-r)
                for i in range(1,diff+1):
                    n_minus_r_fact *= i
                    i += 1
                #print(n_minus_r_fact)

                permutation_n_r = (n_fact/n_minus_r_fact)

                #return permutation_n_r
                
        except ValueError:
            print("Please enter an integer value!!")
            check_n = 0
    print("PERMUTAION :: ", permutation_n_r)           


def combination(a,b):
    check_n = 0
    n_fact = 1
    r_fact = 1
    n_minus_r_fact = 1
    while(check_n == 0):
        check_n = 1
        try:
            n = int(input("Enter the number of choices, n: "))
            r = int(input("Enter the number of elements, r: "))
            if (n < 0 or r < 0):
                print("Please enter a positve value")
                check_n = 0
            else:
                for i in range(1,n+1):
                   n_fact *= i
                   i += 1
                #print(n_fact)
                for i in range(1,r+1):
                    r_fact *= i
                    i += 1
                    
                diff = (n-r)
                for i in range(1,diff+1):
                    n_minus_r_fact *= i
                    i += 1
                #print(n_minus_r_fact)

                combination_n_r = (n_fact/(n_minus_r_fact*r_fact))

                #return combination_n_r
                
        except ValueError:
            print("Please enter an integer value!!")
            check_n = 0
    print("COMBINATION ::",combination_n_r)


while(FLAG ==0):
    try:
        FLAG = 1
        Choice = int(input("What do you want to Calculate?\n1 Permutation\n2 Combination\n3 Both\nEnter your choice and press enter: "))
        if(Choice == 1):
            print("********************")
            print("****PERMUTATION*****")
            print("********************")
            permutation(n,r)
        elif(Choice == 2):
            print("**********************")
            print("*****COMBINATION******")
            print("**********************")
            combination(n,r)
        elif(Choice == 3):
            print("********************")
            print("****PERMUTATION*****")
            print("********************")
            permutation(n,r)
            print("**********************")
            print("*****COMBINATION******")
            print("**********************")
            combination(n,r)

        elif(Choice > 2 or Choice <=0 ):
            FLAG = 0
    except ValueError:
        print("Enter a Valid input")
        FLAG = 0
'''
TEST CASES:

n = 2
r = 3
PERMUTATION : 2.0
COMBINATION : 0.3333

n = 0
r = 0
PERMUTATION : 1.0
COMBINATION : 1.0

n = <String>
r = 6

PROMPT FOR INTEGER INPUT

n = <DECIMAL VALUE>
r = 6

PROMPT FOR INTEGER INPUT

n = <NEGATIVE VALUE>
or
r = <NEGATIVE VALUE>

PROMPT FOR INTEGER INPUT

'''
