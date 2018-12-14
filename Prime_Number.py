check_a = 0
a = 0
def prime(check,a):
    check_a = 0
    while (check_a == 0):
        try:
            check_a = 1
            a = int(input("Enter the Number from where you want to start searching: "))
            if (a <= 1):
                check_a = 0
                print("Please enter a value greater than 1, There is no Prime number before", a)
                continue
        except ValueError:
            print("Input should be a Positive Integer Value")
            check_a = 0

    for i in range(2,a):
        if(a % i) == 0:
            print(a,"is not a Prime number")
            break
    else:
        print (a,"is a Prime number")
prime(check_a,a)

'''
TEST CASE:
Sample Input : 3 || Expected Output: 2

Sample Input : 7 || Expected Output: 5

Sample Input : 15 || Expected Output: 13

Sample Input : 1000 || Expected Output: 997

Sample Input : 2100 || Expected Output: 2111

Sample Input : 10000 || Expected Output: 9973

Sample input: kj<space>sh || Expected Output : Input should be a positive value

Sample Input : 1<sapce>5 || Expected Output: Input should be a positive valu
'''
