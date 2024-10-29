name=input("what is your name:")
name=name.strip()                                                             #remove whitespaces from string
name=name.capitalize()                                                        #capitalize user's first name
name=name.title()                                                             #capitalize user's full name

name=name.strip().title()              #line 2 and 4 used together       #remove  whitespaces from string and capitalize user's full name

#print(*objects, sep=' ', end='\n', file=None, flush=False)  
print("hello,", end="")
print(name)

print(f"hello,\"{name}\"")                                                     #'\' ->escape quotes

name2=input("what is your name:").strip().title()                             # All above code in one single line

first,last=name2.split(" ")                                                   #split  user's name into first and last name
print("hello,",first)