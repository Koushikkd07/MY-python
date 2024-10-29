import re
"""
email=input("enter email address:")

if "@" in email and  "." in email:

    print("valid email")
else:
    print("invalid email")
    """
    
    
#                             syntax of functions, exception and flags of reguler  expression

"""
    re.match()
Description: Matches a pattern only at the beginning of the string.
Return Value: If the pattern matches the string, it returns a match object, otherwise it returns None
re.match(pattern, string, flags=0)

re.search()
Description: Searches for the first occurrence of the pattern in the string.
Return Value: If the pattern matches the string, it returns a match object, otherwise it returns None
re.search(pattern, string, flags=0)

re.findall()
Description: Finds all occurrences of the pattern in the string and returns them as a list.
re.findall(pattern, string, flags=0)

re.split()
Description: Splits the string by occurrences of the pattern.
re.split(pattern, string, maxsplit=0, flags=0)

re.sub()
Description: Substitutes the matched pattern with a replacement string.
re.sub(pattern, repl, string, count=0, flags=0)

re.compile()
Description: Compiles a pattern into a regular expression object for repeated use.
re.compile(pattern, flags=0)


#                                                   Exceptions in the re Module

re.error: This exception is raised when a regular expression is invalid or cannot be compiled.

                                                    Flags in the re Module
                                                    
Flags are optional parameters that modify the behavior of pattern matching. They can be passed as the flags argument to any of the functions.
re.IGNORECASE (or re.I): Makes the pattern case-insensitive.
re.MULTILINE (or re.M): Changes the behavior of ^ and $ to match the start and end of each line, rather than the entire string.
re.DOTALL (or re.S): Makes the dot (.) match any character, including newlines (/n).
re.VERBOSE (or re.X): Allows for more readable regular expressions by ignoring whitespace and comments within the pattern.
re.ASCII (or re.A): Makes the \w, \ b, \d, \s, etc., match only ASCII characters (not Unicode).
re.LOCALE (or re.L): Makes the pattern dependent on the current locale settings.




"."---> any character except newline
"*"---> 0 or more repetition
"+"---> 1 or more repetition
"?"---> 0 or 1 repetition
"{m}"---> m number of repetition
{m,n}---> m-n repetition
"{n,}"---> At least n times
"^"---> matches the start of the string
"$"---> matches the end of the string or just before the newline at the end of the string
"[]"---> set of characters
"[^]"--->  set of characters not in the brackets or complimenting the set


                                                        "PARTIAL LIST"
    \d---> digit
    \D---> non-digit
    \s---> whitespace
    \S---> non-whitespace
    \w---> alphanumeric (word character as well as number and underscore)
    \W---> non-alphanumeric


(A|B)---> either A or B
(...)---> a group
(?:.....)---> non capturing version

    """
"""
    
email=input("enter your email:")

##if re.search(".*@.*",email):        #checks  if the email contains "@" and checks before @ is there any  character and after "@" is there any character or newline
#if re.search(".+@.+",email):          #checks if the email  contains "@" and checks before @ is there any  character and after "@" is there any character or newline with minimum one repetition
#if re.search("..*@..*",email):         #this will act same as (".+@.+") just written in another approach
#if re.search(r".+@.+\.edu",email):          #this "\.edu" checks if the email is ended with a ".edu" or not  
#if re.search(r"^.+@.+\.edu$",email):        #this escape sequence before period is used to escape the period so that it is treated as a literal period not as a special character
#if re.search(r"^[^@]+@[^@]+\.edu$",email):  # this checks if  the email is ended with a ".edu" or not and checks before @ is there any  character or repeated @ before and after the middle @
if re.search(r"^[a-zA-z0-9_]+@[a-zA-z0-9_]\.edu$",email):     # this checks if the email is ended with a ".edu" or not and checks before @ is there the pattern is maintained by the user or not
    print("valid")                               # '/'---> escape character
else:                                   # that r in re.search is stands for raw string
    print("invalid")
    """
    
#^[a-zA-z0-9_]----> we also can write this whole pattern as '"\w"' which means alpha numeric symbol it does the same thing as [a-zA-z0-9_]
email=input("enter your email:").strip()
if re.search(r"^\w+@\w+\.[a-zA-z]+$",email):
    print("valid")
else: 
    print("invalid")