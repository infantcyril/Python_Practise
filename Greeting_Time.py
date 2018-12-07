import datetime
currenttime = datetime.datetime.now()
a = currenttime.hour
def greet(a):
    FLAG = 0
    num = 0
    while(num == 0):
        num = 1
        print ("Please Enter Your Name : ")
        Name = input()
        #Enter a name (Accepts String and White Space as Input)
        #Greet the person based on current time (Format : Good Afternoon <Firstname>)
        if all(x.isalpha() or x.isspace() for x in Name):
            if currenttime.hour < 12:
                print("Good Morning", Name.split()[0])
            elif (12 <= currenttime.hour <= 16):
                print("Good Afternoon", Name.split()[0])
            elif(16 < currenttime.hour <= 19):
                print("Good Evening", Name.split()[0])
            elif(19 < currenttime.hour <= 23):
                print("Good Night", Name.split()[0])

            FLAG = 1
        if (FLAG == 0):        
            print("Please enter a Valid name")
            num = 0
greet(a)


'''
Test Case

AT TIME : 15:19

Sample Input:
Please Enter Your Name :
Infant Cyril

Expected Output:

Good Afternoon Infant

Sample Input:
Please Enter Your Name :
Jayanth Nag

Expected Output:

Good Afternoon Jayanth

AT TIME: 18:14

Sample Input :
Please Enter Your Name:
Infant Cyril

Expected Output:

Good Evening Infant

AT TIME: 01:15

Sample Input :
Please Enter Your Name:
Prabhu Ethna

Expected Output:

Good Morning Prabhu

'''

