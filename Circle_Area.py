pi = 3.14
r = 0.0
def area_circle(r,pi):
    
    check_r = 0
    while (check_r == 0):
        check_r = 1

        try:
            r = float(input("Enter the radius of the circle:"))
            if(r < 0):
                print("Radius of a Circle cannot be negative!!!")
                check_r = 0
        except ValueError:
            print("Radius cannot be a string")
            check_r = 0

    Area = pi * (r*r)
    print("The Area of the Circle with radius =%.3f" % r, "is:%.3f" % Area)


def circum_circle(r,pi):
    
    check_r = 0
    while (check_r == 0):
        check_r = 1

        try:
            r = float(input("Enter the radius of the circle:"))
            if(r < 0):
                print("Radius of a Circle cannot be negative!!!")
                check_r = 0
        except ValueError:
            print("Radius cannot be a string")
            check_r = 0

    circumference = 2* pi * r
    print("The Circumference of the Circle with radius =%.3f" % r, "is: %.3f" % circumference)

FLAG = 0
while(FLAG ==0):
    try:
        FLAG = 1
        Choice = int(input("What do you want to Calculate?\n1 Area\n2 Circumference\nEnter your choice and press enter: "))
        if(Choice == 1):
            print("*************")
            print("****AREA*****")
            print("*************")
            area_circle(r,pi)
        elif(Choice == 2):
            print("**********************")
            print("****CIRCUMFERENCE*****")
            print("**********************")
            circum_circle(r,pi)
        elif(Choice > 2 or Choice <=0 ):
            print("Enter a valid Input")
            FLAG = 0
    except ValueError:
        print("Enter a Valid input")
        FLAG = 0
'''
Enter the radius of the circle:3
What do you want to Calculate?
1 Area
2 Circumference
1
*************
****AREA*****
*************
The Area of the Circle with radius =3.000 is:28.260

Enter the radius of the circle:21y12
Radius cannot be a string
Enter the radius of the circle:#%$#%$#
Radius cannot be a string
Enter the radius of the circle:21.5
What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =21.500 is: 135.020


Enter the radius of the circle:0
What do you want to Calculate?
1 Area
2 Circumference
1
*************
****AREA*****
*************
The Area of the Circle with radius =0.000 is:0.000

Enter the radius of the circle:0
What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =0.000 is: 0.000

Enter the radius of the circle:1
What do you want to Calculate?
1 Area
2 Circumference
3
Enter a valid Input
What do you want to Calculate?
1 Area
2 Circumference
3
Enter a valid Input

What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =1.000 is: 6.280

Enter the radius of the circle:2
What do you want to Calculate?
1 Area
2 Circumference
Enter your choice and press enter: 1
*************
****AREA*****
*************
The Area of the Circle with radius =2.000 is:12.560
'''


    



'''
Enter the radius of the circle:3
What do you want to Calculate?
1 Area
2 Circumference
1
*************
****AREA*****
*************
The Area of the Circle with radius =3.000 is:28.260

Enter the radius of the circle:21y12
Radius cannot be a string
Enter the radius of the circle:#%$#%$#
Radius cannot be a string
Enter the radius of the circle:21.5
What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =21.500 is: 135.020


Enter the radius of the circle:0
What do you want to Calculate?
1 Area
2 Circumference
1
*************
****AREA*****
*************
The Area of the Circle with radius =0.000 is:0.000

Enter the radius of the circle:0
What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =0.000 is: 0.000

Enter the radius of the circle:1
What do you want to Calculate?
1 Area
2 Circumference
3
Enter a valid Input
What do you want to Calculate?
1 Area
2 Circumference
3
Enter a valid Input

What do you want to Calculate?
1 Area
2 Circumference
2
**********************
****CIRCUMFERENCE*****
**********************
The Circumference of the Circle with radius =1.000 is: 6.280

Enter the radius of the circle:2
What do you want to Calculate?
1 Area
2 Circumference
Enter your choice and press enter: 1
*************
****AREA*****
*************
The Area of the Circle with radius =2.000 is:12.560
'''


    


