create_lis = []
def max_inlist(create_lis):
    
    new_lis = []
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
            while lis_len!=0:
                value_list = int(input("Enter the integer value to be present in your list"))
                create_lis.append(value_list)
                lis_len -=1
        except ValueError:
            print("Enter a valid input")
            check_value = 0
    print(create_lis)
    maximum = create_lis[0]
    for i in create_lis:
        if i > maximum:
            maximum = i
    return maximum

                
result = max_inlist(create_lis)
print ("The maximum number in the given list is: ",result)

'''
Test Cases:
Input: [22,33,44,10,2,45,98,0]
Output : 98

Input: [22,33,44,10,2,45,20,-1]
Output: 45

###Doesnot accept Strin as a value in list or length of list.

'''

'''
Test Cases for Length of String:


Enter the max lenth of list a
Enter a valid input
Enter the max lenth of list <space>
Enter a valid input
Enter the max lenth of list q321
Enter a valid input
Enter the max lenth of list 3sa
Enter a valid input
Enter the max lenth of list6
get input
'''



