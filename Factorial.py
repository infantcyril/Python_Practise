check_n = 0
n = 1
def fact1(check,n):
    factorial = 1
    check_n = 0
    i = 2
    while check_n == 0:
        check_n = 1
        try:
            n = int(input("Enter the number"))
            
            if n >= 0:
                for i in range(2,n+1):
                    factorial *= i
                    i += 1
                return (factorial) 
            else:
                print("Enter a value equal to or greater than 0")
                check_n = 0
        
        except ValueError:
            print("Please give an integer input")
            check_n =0
result = fact1(check_n, n)
print (result)
