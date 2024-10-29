import sys

'''
        The sys module in Python provides access to some variables and functions used or maintained 
        by the interpreter and to functions that interact strongly with the interpreter.
'''



# FUNCTIONS IN sys MODULE------>>>>


"""
                                                    VARIABLES;-------->>>>>>

(1)sys.argv: The list of command line arguments passed to the Python script.

(2)sys.exit([arg]): Exit the program with a given status.

(3)sys.path: A list of strings that specifies the search path for modules.

(4)sys.platform: A string that indicates the platform on which Python is running.

(5)sys.version: A string that indicates the version number of the Python interpreter.

(6)sys.stdin, sys.stdout, sys.stderr: File objects used for standard input, output, and error.

                                                    FUNCTIONS:------>>>>>>

(7)sys.exit([arg]): Exit the program with a given status.

(8)sys.getsizeof(object): Return the size of an object in bytes.

(9)sys.modules: A dictionary that maps module names to modules which have already been loaded.

(10)sys.argv: The list of command line arguments passed to the Python script.

(11)sys.byteorder: A string that indicates the byte order of the platform (either 'little' or 'big').

(12)sys.callstats(): Return a dictionary that contains statistics about the number of function calls.


    """
    
    
    
'''
try:
    print("hello my name is", sys.argv[0])   
except IndexError:
    print("no arguments passed")
    

if len(sys.argv) != 4:
    print("Usage: python calculator.py num1 operator num2")
    sys.exit(1)

num1 = float(sys.argv[1])
operator = sys.argv[2]
num2 = float(sys.argv[3])

if operator == "+":
    print(f"Result: {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1 * num2}")
elif operator == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Unsupported operator")
    '''
    
'''  
if len(sys.argv)<3:
    sys.exit("too few arguments")                             #print("too few arguments")
elif len(sys.argv)>3:
    sys.exit("too many arguments")                            #print("too many arguments")
else:
    print("your name is",sys.argv[1],sys.argv[2])
    '''
    
if len(sys.argv)<100:                                   #this code take arguments as input and store in a list and check# if the size of list is 
    for arg in sys.argv[1:6]:                                #greater than 100 or not and if the list's size is greater than 100 it will print an error
        print(arg,end=" ")                               #in line 85 we start counting from 1st index  so we use 1: to get all the arguments(use slice's concept)
elif len(sys.argv)>100:                                 #  1:---->1 to last
    print("too many arguments")                         # 1:6----->1 to 5th element
                                                        # 1:n------> 1 to (n-1)th element