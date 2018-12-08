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
c = []
def Prime3(a,c):
    for num in range(1,a):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            c.append(num)
            
    print ("The prime number that comes first when we count backwards from", a,"is:" , (max(c)))
Prime3(a,c)

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
