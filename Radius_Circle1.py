pi = 3.14
check_area = 0
area = 0
def radius_circle(check,area,pi):
    check_area = 0
    while (check_area == 0):
        check_area = 1

        try:
            area = float(input("Enter the area of the circle:"))
            if(area<0):
                check_area = 0
                print("Area of a Circle cannot be a negative value")
                continue

        except ValueError:
            print("Enter a Valid Input")
            check_area = 0
    radius_Square = (area)/pi
    radius = radius_Square ** 0.5
    print("The Radius of the Circle with Area = %.3f"  % area, "is: %.3f" % radius)
radius_circle(check_area,area,pi)

'''
TEST CASES:

SAMPLE INPUT/EXPECTED OUTPUT

Enter the area of the circle:55
The Radius of the Circle with Area = 55.000 is: 4.185

Enter the area of the circle:hks
Enter a Valid Input

Enter the area of the circle:&^*@!
Enter a Valid Input

Enter the area of the circle:-55
Area of a Circle cannot be a negative value

Enter the area of the circle:
Enter a Valid Input

Enter the area of the circle:64
The Radius of the Circle with Area = 64.000 is: 4.515

Enter the area of the circle:356fgf
Enter a Valid Input
'''

    


