'''
def main():
    x=int(input("enter a number:"))
    if is_even(x):
        print(x,"is even")
    else:
        print(x,"is odd")
def is_even(n):
   
    #return True if n%2==0 else  False                              # 4 individual ines in one single line
    
    return n%2==0                        #This line is more simple to understand then the previous line

main()


#SWITCH CASE IN PYTHON  
name=input("what is your name:")

match name:
    case "John" | "Alice" | "Bob" | "Emma":
        print("Hello, you are a friend of mine")
    case  "Admin" | "Superuser":
        print("Hello, you are an admin")
    case _:
            print("Hello, I don't know you")
for i in [0,100,2,3,5,4,7,56]:
    print(i)
   
print("Bye " *3)
print("Bye\n"*3, end="")

while True:
    n=int(input("enter value:"))
    if n<0:
        continue
    else:
        break
    return n
print("meow\n"*n, end="")
'''
student=["koushik","harry","ron"]           #[0,1,2,.......,n]
#print(student[1])
for i in range (len(student)):
    #student[i]=student.capitalize()
    print(i+1, student[i])
