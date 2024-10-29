'''

try:                                # try is keyword used to test your code for errors
    x=int(input("what is x?:"))
except ValueError:                  #except is keyword used to handle the errors
    print("invalid input")          # ValueError is a built-in exception in python that is raised when a value is not of the expected type.
else:                               # else will be execute only if there is no error inside the try
    print(f"x is {x}")
'''    
'''
                                                ||||{[#### TYPES OF ERRORS IN PYTHON ####]}|||||
    '''
    
"""
      (1) ValueError: Raised when a function receives an argument of the right type but an inappropriate value. 
                        For example, trying to convert a non-numeric string to an integer.
                        
                        ### int("abc")  # Raises ValueError
                        
      (2)NameError: Raised when a local or global name is not found. 
                    This usually occurs when you try to use a variable that hasn’t been defined. 
                    
                         ###  print(x)  # Raises NameError if x is not defined
                                       
      (3)TypeError: Raised when an operation or function is applied to an object of inappropriate type.
                        For example, trying to add a string and an integer. 
                        
                            ### "2" + 2  # Raises TypeError            
                        
      (4)SyntaxError: Raised when the parser encounters a syntax error. 
                      This means that the code is not valid Python syntax.   
                      
                            ### eval("x === x")  # Raises SyntaxError
                                    
      (5)IndexError: Raised when a sequence subscript is out of range. 
                     This occurs when trying to access an index that does not exist in a list or tuple.
                     
                            ###  lst = [1, 2, 3]
                                 lst[5]  # Raises IndexError
                     
      (6)KeyError: Raised when a dictionary is accessed with a key that does not exist.
      
                            ### d = {'a': 1}
                                d['b']  # Raises KeyError
      
      (7)AttributeError: Raised when an invalid attribute reference is made, meaning the object does not have that attribute.
      
                            ### "hello".non_existent_method()  # Raises AttributeError
                            
      (8)IOError: Raised when an input/output operation fails, such as trying to open a file that does not exist. 
                  (Note: In Python 3, IOError is merged into OSError.)
                  
                            ### open("non_existent_file.txt")  # Raises IOError    
                            
      (9)ZeroDivisionError: Raised when attempting to divide by zero.
      
                            ### 1 / 0  # Raises ZeroDivisionError
                            
      (10)ImportError: Raised when an import statement fails to find the module or name to import.
      
                            ### import non_existent_module  # Raises ImportError
                            
      (11)RuntimeError: Raised when an error is detected that doesn’t fall into any of the other categories. 
                        This is a generic error.
                        
                            ###raise RuntimeError("This is a runtime error")  # Raises RuntimeError
                            
      (12)AssertionError: Raised when an assert statement fails. 
                          Assertions are used for debugging purposes.
                          
                            ### assert False  # Raises AssertionError
                            
      (13)FileNotFoundError: Raised when trying to open a file that does not exist. 
                                (This is a subclass of IOError in Python 3.)
                                
                                ### open("non_existent_file.txt")  # Raises FileNotFoundError
                                
      (14)OverflowError: Raised when the result of an arithmetic operation is too large to be expressed within the range of the integer type.
      
                                ### import math
                                    math.factorial(1000)  # May raise OverflowError in some contexts
                                   
      (15)IndentationError: Raised when there is an incorrect indentation in the code. 
                            This is a subclass of SyntaxError.
                            
                                  ###  def foo():
                                       print("Hello")  # Raises IndentationError
                                   
    """
    
    
    
"""
    
while True:
    try:
        x=int(input("what is x:"))
        break
    except  ValueError:
        print("that is not a number")

print(f"x is {x}")
"""

def main():
    num=GetValue()
    print(f"x is {num}")
    
def GetValue():
    while True:
        try:
            return int(input("what is x:"))                       # In this line we simply return the input value in one line
        except  ValueError:
            #print("x is not an integer")
            pass                                         # pass is a keyword use to skip the code in the loop
                                             # here pass used to ignore the wrong input and ask again for input without printing any error message



    
    

main()