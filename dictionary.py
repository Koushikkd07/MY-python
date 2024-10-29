'''
                                            Dictionary is a key value pair
'''



""" 
students={
        "koushik":"Rishra",
        "parambrata":"Chuchura",
        "sounak":"Rishra"                                           #{"key":"value"}
}
#print(students["koushik"])                  #In dictionary there is no index to found you have to use keys to print the value inside it
for student in students:
    print(student, students[student], sep=" at ")         #To print all the keys in dictionary         sep=separate
#for i in range(len(students)):
 #   print(i+1,students)
 """
 
 
 
'''
                                                LIST OF DICTIONARY                          
'''



"""
    
collage=[
    {"Name":"koushik","Age":"20","city":"Rishra"},
    {"Name":"Parambrata","Age":"21","city":"Chuchura"},
    {"Name":"sounak","Age":"20","city":"Rishra"},
    {"Name":"Ayan","Age":"25","city":None}  # "None" is keyword to represent the official absence of a value though it is a keyword so you have to write the keyword without " "

]

for student  in collage:
    print(student["Name"],student["Age"], sep=", ")    # student["keyword"] is used to print the particular value of that particular key in the dictionary and make sure that you have written the keyword within " "
"""




'''
                                                    MARIO.PY
'''



#print("[]\n" * 3 , end="")
#for _ in range(3):
    
#    print("[]")  
    
    
    


    #size=int(input("enter size:"))
    
    
'''
def square(size):
    for i in range(size):
        for j in range(size):
            print("[]",end="")
        print()
    
    

square(3)  
'''                                                 #[][][]
                                                    #[][][]   <------------------print the pattern
                                                    #[][][]
                                                                                                            
                                                                                                            
"""                                     more easy way to do the above code                                  
"""


def square(size):
    for i in range(size):
        print("[]"*size)

square(3)