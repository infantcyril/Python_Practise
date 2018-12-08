def prim(a):
    for x in range(2,a):
        if(a%x) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")


check_a = 0
while(check_a == 0):
    check_a = 1
    try:
        a = int(input("Enter a number :"))
        if a == 1:
            print("1 is a Natural Number")
            
        elif a <= 0:
            num = 0
            print("Enter a Positive Integer")
            check_a = 0
            
        elif(a>1):
            prim(a)
    except ValueError:
        print("No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1")
        check_a = 0
'''
TEST CASES:

SAMPLE INPUT/EXPECTED OUTPUT

Enter a number :3
3 is a prime number

Enter a number :12
12 is not a prime number

Enter a number :211
211 is a prime number

Enter a number :1009
1009 is a prime number

Enter a number :adsd
No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1

Enter a number :!@#@!#
No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1

Enter a number :
No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1

Enter a number :-12
Enter a Positive Integer

Enter a number :0
Enter a Positive Integer

Enter a number :3/5
No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1

Enter a number :6asda
No String/Spl Characters!!! Enter a Valid Positve Integer Value greater than 1
'''
