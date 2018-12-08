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
def prime(a):
    for num in range(1,a):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            print ("The prime number that comes first when we count backwards from", a,"is:" , (max(c)))
prime(a)

'''
TEST CASE:
Sample Input : 3 || Expected Output: 2

Sample Input : 7 || Expected Output: 5

Sample Input : 15 || Expected Output: 13

Sample Input : 1000 || Expected Output: 997

Sample Input : 2100 || Expected Output: 2111

Sample Input : 10000 || Expected Output: 9973
'''
