def greet():
        num = 0
        while(num == 0):
            num = 1
            print ("Please Enter Your Name : ")
            Name = input()
        #Enter a name (Accepts String and White Space as Input)
        #Greet the person (Format : Hi <Firstname>)
            if all(x.isalpha() or x.isspace() for x in Name):
                print("Hi", title().Name.split()[0])
                FLAG = 1
            else:        
                print("Please enter a Valid name")
                num = 0
greet()


'''
Test Case

Time : 01:xx
Sample Input:
Please Enter Your Name :
Infant Cyril

Expected Output:

Good Morning Infant



Time : 13:xx

Sample Input:
Please Enter Your Name :
Jayanth Nag

Expected Output:

Good Afternoon Jayanth

Sample Input :
Please Enter Your Name:
132132

Expected Output:

Please enter a Valid name


Sample Input :
Please Enter Your Name:
#$%#%$#

Expected Output:

Please enter a Valid name

Time : 17:xx

Sample Input:
Please Enter Your Name :
cyril infant

Expected Output:

Good Evening Cyril



'''

