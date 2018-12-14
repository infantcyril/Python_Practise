check_a = 0
a = 0
def prim(check,a):
    check_a = 0
    while (check_a == 0):
        try:
            check_a = 1
            a = int(input("Enter the Number from where you want to start searching: "))
            if (a <= 2):
                check_a = 0
                print("Please enter a value greater than 2, There is no Prime number before", a)
                continue
        except ValueError:
            print("Input should be a Positive Integer Value")
            check_a = 0


    for x in range((a-1),1,-1):
        for num in range(2,x):
            if(x%num == 0):
                break
        else:
            print("The prime number that comes first when we count backwards from" ,a, "is:",x)
            break
            
prim(check_a,a)
'''
TEST CASE:
Sample Input : 3 || Expected Output: The prime number that comes first when we count backwards from 3 is:2



Sample Input : 15 || Expected Output: The prime number that comes first when we count backwards from 56 is:13



Sample Input : 2100 || Expected Output: The prime number that comes first when we count backwards from 2100 is:2111

Sample Input : 10000 || Expected Output: The prime number that comes first when we count backwards from 10000 is: 9973
 -------------------------------------------
	Input	|	Output
      -------------------------------------------
	56	|	The prime number that comes first when we count backwards from 56 is: 53
      -------------------------------------------
	asd	|	Enter a positive integer value
      -------------------------------------------
	@#$	|	Enter a positive integer value
      -------------------------------------------
	2.5	|	Enter a positive integer value
      -------------------------------------------
	-2	|	Please enter a value greater than 2, There is no Prime number before -2.
      -------------------------------------------
	 0	|	Please enter a value greater than 2, There is no Prime number before 0.
      -------------------------------------------
	
'''
