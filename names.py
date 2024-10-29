'''
(method) def readlines(
    hint: int = -1,
    /
) -> list[str]

'''
"""
    
with open("names.txt","r") as file:         #The line.rstrip() function in Python is used to remove trailing characters from a string. 
                                            #By default, it removes trailing whitespace characters, but you can also specify a set of characters to be removed. 
                                            # #The rstrip() method returns a copy of the string with the trailing characters removed.
    lines=file.readlines()

for line in lines:
    print("hello,",line.rstrip())
    """
    #optimized code :---
""" 
with open("names.txt","r") as file:             #sorted the elements of the file
    for name in sorted(file,reverse=True):                   #sorted(iterable, /, *,key=None,reverse=False)
        print("hello,",name.rstrip().title())
"""

    