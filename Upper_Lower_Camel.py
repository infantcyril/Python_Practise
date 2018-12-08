def change_case():
check_string = 0
while(check_string == 0):
    try:
        check_string = 1
        Str = str(input("Enter a String: "))
        if all(x.isalpha() or x.isspace() for x in Str):
            print("UPPER CASE :", Str.upper())
            print("LOWER CASE :", Str.lower())
            print("CAMEL CASE :", Str.title())
        else:
            print("Enter a valid input")
            check_string = 0
    except ValueError:
        print("Please Enter a Valid Input")
        check_string = 0
change_case()
'''
TEST CASES:

Enter a String: i live in chennai
UPPER CASE : I LIVE IN CHENNAI
LOWER CASE : i live in chennai
CAMEL CASE : I Live In Chennai

Enter a String: my name is cyril
UPPER CASE : MY NAME IS CYRIL
LOWER CASE : my name is cyril
CAMEL CASE : My Name Is Cyril

Enter a String: hI HoW Are YOU
UPPER CASE : HI HOW ARE YOU
LOWER CASE : hi how are you
CAMEL CASE : Hi How Are You

Enter a String: 651265
Enter a valid input

Enter a String: %$^%$
Enter a valid input

Enter a String: jklk&^&$123
Enter a valid input
'''
s
