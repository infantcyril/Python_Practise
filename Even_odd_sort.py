create_lis = []
def even_odd_sort(lis):
    even = []
    odd = []
    even1 = []
    odd1 = []
    final_lis = []
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
            for x in range(1,(lis_len + 1)):
                value_list = int(input("Enter the integer values to be present in your list"))
                create_lis.append(value_list)
            for i in create_lis:
                if (i%2 == 0):
                    even_num = i
                    even.append(even_num)
                else:
                    odd_num = i
                    odd.append(odd_num)
            while even:
                mini = even[0]
                for j in even:
                    if j < mini:
                        mini = j
                even1.append(mini)
                even.remove(mini)    
            while odd:
                mini = odd[0]
                for j in odd:
                    if j < mini:
                        mini = j
                odd1.append(mini)
                odd.remove(mini)
            final_lis = [*odd1,*even1]
            print(final_lis)
        except ValueError:
            print("Please Enter Valid Inputs in the list, This list will contain only integer values")
            check_value = 0
even_odd_sort(create_lis)
'''
Test Cases:
Input : Create List :
[1,2,3,4,5,6,7,8,9]
Output: New_lis :
[1,3,5,7,9,2,4,6,8]

Input (REPEATED NUMBERS): Create List:
[1,6,3,2,5,6,9,4,8]
Output : New_lis :
[1,3,5,9,2,4,6,6,8]

Input : Create List :
[1,a,2,56]

*****Value Error****

Input (DECIMAL VALUE)
[1,2,3.5,6.2]

*****Value Error****

'''

