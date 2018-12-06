EMP =[{
        "Name": "Cyril",
        "Age": 30,
        "Email": "glcyril@gmail.com",
        "E_Id": "EA294",
        "Ph_No": 9894769493
        },
       
      { "Name": "Prabhu",
        "Age": 25,
        "Email": "prabhu@gmail.com",
        "E_Id": "EA292",
        "Ph_No": 9442563635
        },
       
      { "Name": "Raja",
        "Age": 24,
        "Email": "raja@gmail.com",
        "E_Id": "EA295",
        "Ph_No": 9176256965
      },
       
      { "Name": "Roy",
        "Age": 28,
        "Email": "roy@gmail.com",
        "E_Id": "EA285",
        "Ph_No": 9842569896
      },
       
      { "Name": "Rajesh",
        "Age": 26,
        "Email": "rajesh@gmail.com",
        "E_Id": "EA296",
        "Ph_No": 9894756236
      },
      
      {"Name": "Prasath",
        "Age": 26,
        "Email": "prasath@gmail.com",
        "E_Id": "EA298",
        "Ph_No": 9865462266
       }
    ]
Match_Name = []
def Dict_Search(EMP,Match_Name):
    FLAG = 0
    S_String =str(input("Enter the Search String: "))
    for Str in EMP:
        for key,value in Str.items():
            #Compare the Search String with Values in Dictionary
            if (S_String == str(value) or S_String.lower() in str(value) or S_String.upper() in str(value)):
                #if search string matches the value append it to the defined empty list and print the list if the value of FLAG variable = 1.
                Match_Name.append(Str["Name"])
                FLAG = 1
                           
    if FLAG == 0:
        print("The entered string does not match with any of the values")
    else:
        print("Name: ", Match_Name)
Dict_Search(EMP,Match_Name)

'''
Test Case

Sample Input : cyril || Expected Output : Name : [Cyril]
Sample Input : ea294 || Expected Output : Name : [Cyril]
Sample Input : EA294 || Expected Output : Name : [Cyril]
Sample Input : PRASATH@GMAIL.COM || Expected Output : Name : [PRASATH]
Sample Input : 26 || Expected Output : Name : ['Rajesh','Prasath']
'''




    

        
        
        
