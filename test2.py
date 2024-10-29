"""
    
x=input("enter 1st value:")
y=input("enter 2nd value:")

z=x+y
print(z)
z=int(x)+int(y)
print(z)
print(int(input("enter 1st value:"))+int(input("enter 2nd value:")))              #all above code in single ine using nested function
x=float(input("enter 1st value:"))
y=float(input("enter 2nd value:"))

z=round(x/y)                              #round(number, ndigits=None)   round figure the decimal number to the nearest interger
print(f"your first answer is:{z}")
z=round((x/y),2)
print(f"your answer is:{z}")

print(f"your answer is:{z:,}")              #formatted the number by using comma  as thousand separator

"""
x=float(input("enter 1st value:"))
y=float(input("enter 2nd value:"))
z=x/y    #or you can write it as  z=((x/y),2) for 2 decimal places
print(f"your answer is:{z:.2f}")            