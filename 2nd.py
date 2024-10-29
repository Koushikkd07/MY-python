import random 
students=[]
n=int(input("how many students you want to add:"))
for i in range(n):
        Name=input("Enter name:").strip().title()
        roll=int(input("enter roll no:"))
        house=input("enter your house :").strip()
        
        student={
            "NAME":Name,
            "ROLL":roll,
            "HOUSE":house
        }
students.append(student)

print("randomly print student data:",random.choice(students))