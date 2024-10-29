"""
    
def hello(name):
    first,last=name.split(" ")
    print(f"Hello Mr.\"{last}\"")
name=input("enter your name:").strip().title()
hello(name)
"""

def hello(to="world"):
    print("Hello,",to)
hello()                               #hello("Alice")  # Output: Hello, Alice         #hello()  # Output: Hello, world
name=input("enter your name:").strip().title()
hello(name)