check_string = 0
count = 0
while(check_string == 0):
    check_string = 1
    Str = str(input("Enter a String: "))
    if all(x.isspace() for x in Str):
        print("Please give an Input..!! You have given only spaces")
        check_string = 0
    else:
        for x in Str:
            count+=1
        print("The length of ",Str.upper(), "is: " , count)
 
'''
TEST CASES:
SAMPLE INPUT/OUTPUT

Enter a String: 2131231
The length of  2131231 is:  7

Enter a String: asda sadas
The length of  ASDA SADAS is:  10

Enter a String: hgajsd!kjhkh%^&*(
The length of  HGAJSD!KJHKH%^&*( is:  17


:::***EMPTY STRING***:::
Enter a String:
Please give an Input..!! You have given only spaces
Enter a String:
'''

