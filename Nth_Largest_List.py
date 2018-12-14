
create_lis = []
def nth_largest(lis):
    
    create_lis = []
    new_lis = []
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
            while lis_len != 0:
                value_list = int(input("Enter the integer value to be present in your list"))
                create_lis.append(value_list)
                lis_len-=1
        except ValueError:
            print("Enter a valid input")
            check_value = 0
    print(create_lis)
    while create_lis:
        minimum = create_lis[0]
        for i in create_lis:
            if i < minimum:
                minimum = i    
        new_lis.append(minimum)
        create_lis.remove(minimum)

        
    for i in new_lis:
        if i not in final_lis:
            final_lis.append(i)
    size  = (len(final_lis))
    check_n = 0


    while(check_n == 0):
        check_n = 1
        try:
            n = int(input("Enter the value of n:"))
            if n > size or n <= 0:
                print("This list has only" ,size,"unique values! Please enter a value between 1 and",size)
                check_n = 0
               
        except ValueError:
            print("Enter a valid input")
            check_value = 0
    #print(new_lis)
    #print(final_lis)

    print("The" ,n ,"largest number in the list is",final_lis[size - n])
nth_largest(create_lis)
