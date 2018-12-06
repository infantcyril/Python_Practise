check_a = 0
check_b = 0
while (check_a == 0):
    try:
        check_a = 1
        a = int(input("Enter the value of the Number from where you want to start searching: "))
        if (a < 0):
            check_b = 0
            print("Please enter a Positive Value")
            continue
    except ValueError:
        print("Input should be a Positive Value")
        check_a = 0
while(check_b == 0):
    try:
        check_b = 1
        b = int(input("Enter the index value: "))
        if (b <= 0):
            check_b = 0
            print("Enter a positive integer value for b")
            continue
    except ValueError:
        print("Input should be a Positive Value")
        check_b = 0
   
c = []
while (a <= 0):
    a += 1
    break
def Prime3(a,b,c):
    for num in range(a+1,((a+50*b))):
        for i in range(2,num):
            if(num % i) == 0:
                break
        else:
            c.append(num)
    print ("The Next Prime Number Residing in The Index Value", b, "is:" , c[b-1])
Prime3(a,b,c)

'''
TEST CASE:
Sample Input :
(2,5)

Expected Output:
11
 -----------------

Sample Input :
(7,3)

Expected Output:
17
------------------

Sample Input :
(2,100)

Expected Output:
547
------------------

Sample Input :
(1000,5)

Expected Output:
1031
------------------
Sample Input :
(0,5)

Expected Output:
11

'''
