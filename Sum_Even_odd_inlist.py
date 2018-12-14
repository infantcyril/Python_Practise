create_lis = []
def sum_even_odd(lis):
    even = []
    odd = []
    
    check_list = 0
    check_value = 0
    while(check_list == 0):
        check_list = 1
        try:
            lis_len = int(input("Enter the max lenth of list"))
        except ValueError:
            print("Enter a valid input")
            check_list = 0
    while(check_value == 0):
        check_value = 1
        try:
            while(lis_len != 0):
                value_list = int(input("Enter the integer value to be present in your list"))
                create_lis.append(value_list)
                lis_len -= 1
            for i in create_lis:
                if (i%2 == 0):
                    even_num = i
                    even.append(even_num)
                else:
                    odd_num = i
                    odd.append(odd_num)
        except ValueError:
            print("Please Enter Valid Inputs in the list, This list will contain only integer values")
            check_value = 0
    print("Even numbers in the given list",even, "Odd numbers in the given list",odd)
    sum_even = 0
    sum_odd = 0
    for i in even:
        sum_even = sum_even+i
    print ("The Sum of Even numbers in the list:", sum_even)
    for i in odd:
        sum_odd = sum_odd + i
    print ("The Sum of Odd numbers in the list :", sum_odd)
sum_even_odd (create_lis)

'''

TEST CASES:


'''
