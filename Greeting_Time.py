import datetime
currenttime = datetime.datetime.now()
a = currenttime.hour
#print (a)
def greet(a):
    FLAG = 0
    num = 0
    while(num == 0):
        try:
            num = 1
            print ("Please Enter Your Name : ")
            Name = input()
        #Enter a name (Accepts String and White Space as Input)
        #Greet the person based on current time (Format : Good Afternoon <Firstname>)
            if all(x.isalpha() or x.isspace() for x in Name):
                if currenttime.hour < 12:
                    print("Good Morning", Name.title().split()[0])
                elif (12 <= currenttime.hour <= 16):
                    print("Good Afternoon", Name.title().split()[0])
                elif(16 < currenttime.hour <= 19):
                    print("Good Evening", Name.title().split()[0])
                elif(19 < currenttime.hour <= 23):
                    print("Good Night", Name.title().split()[0])

                FLAG = 1
            if (FLAG == 0):        
                print("Please enter a Valid name")
                num = 0
        except IndexError:
            print("You did not Enter Your Name")
            num = 0
greet(a)
