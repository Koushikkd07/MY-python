import csv
"""
x=int(input("how many names you want to enter:"))
school=[]

with open("students.csv","a") as file:
    for i in range(x):
        name=input("enter name:").title()
        home=input("enter home:").title()
        file.write(f"{name},{home}\n")
    
with open("students.csv","r") as file:
    for line in file:
        Names,Houses=line.strip().split(",")
        student={"Name":Names,"Houses":Houses}              #student{"Name": koushik , "Houses": rishra}
        school.append(student)                            # Append the student dictionary, not the students list
        
        
        

def get_names(student):
    return student["Name"]

def get_house(student):
    return student["Houses"]    #lambda is keyword in python we use it when we use to call a function or argument at 1 time in whole program
    

for student in sorted(school,key=lambda student: student["Name"],reverse=True):                             #(key=get_names) ----->>>>>#in key=get_name, here, we are not calling the function , we are passing the function itself by it's name so that sorted function can call that function by itself
    print(f"{student['Name']} is in {student['Houses']}")
    
    """
    
"""
                                                                                        #lambda (parameters:) expression ---> lambda  (x,y,z): x**2  ||| multiple parameters (x,y,z)

                                                    #lambda student: student["Name"]:
                                                    
                                                    
    # This is a small anonymous function (called a lambda function) 
    that takes each element in school (which is a list of dictionaries), 
    and returns the value associated with the "Name" key in each dictionary.  
    """
    
    
    
    
    
"""
                                                        CSV MODULE
                                                        
csv.reader()
Default form: Used to read data from a CSV file.

csv.reader(csvfile, dialect='excel', **fmtparams)


csv.writer()
Default form: Used to write data to a CSV file.

csv.writer(csvfile, dialect='excel', **fmtparams)


csv.DictReader()
Default form: Reads a CSV file and maps each row to a dictionary with keys based on the column headers.

csv.DictReader(csvfile, fieldnames=None, restkey=None, restval=None, dialect='excel', **fmtparams)


csv.DictWriter()
Default form: Writes dictionaries to a CSV file.

csv.DictWriter(csvfile, fieldnames, restval='', extrasaction='raise', dialect='excel', **fmtparams)


csv.register_dialect()
Default form: Registers a new CSV dialect (custom format settings).

csv.register_dialect(name, dialect=None, **fmtparams)

csv.unregister_dialect()
Default form: Removes a previously registered dialect by name.

csv.unregister_dialect(name)

csv.get_dialect()
Default form: Retrieves the dialect associated with a given name.

csv.get_dialect(name)


csv.list_dialects()
Default form: Lists all currently registered dialects.

csv.list_dialects()


csv.field_size_limit()
Default form: Returns or sets the maximum allowed field size.

csv.field_size_limit([new_limit])


                                                        Common Parameters (fmtparams):
                These are additional formatting parameters you can pass to most of the functions to control how CSV data is read or written.
                
delimiter: Character that separates fields (default is ,).
quotechar: Character used to quote fields containing special characters (default is ").
doublequote: Whether quote characters are doubled inside fields (default is True).
skipinitialspace: Whether whitespace after the delimiter is ignored (default is False).
lineterminator: String used to terminate lines (default is '\r\n').
quoting: Controls when quotes are used (csv.QUOTE_ALL, csv.QUOTE_MINIMAL, csv.QUOTE_NONNUMERIC, csv.QUOTE_NONE).
"""





"""

school=[]

with open("students.csv") as file:
    reader=csv.DictReader(file)                         #csv.DictReader->this function iterate the whole file and return a dictionary for each row
    #reader= csv.reader(file)                           #csv.reader-> this function read the csv file and figure out where are the commas,quotes,potential corner cases.
    #for name,home in reader:
    for row in reader:
        #school.append({"Name":row["name"],"Houses":row["home"]})
        school.append(row)                                      #{"Name":row["name"],"Houses":row["home"]}==(row) ,because Dictwriter returns a dictionary and in row we have the dictionary

        #school.append({"Name": name,"Houses":home})
    
    
for student in sorted(school,key=lambda student: student["Name"],reverse=True):
    print(f"{student['Name']} is in {student['Houses']}")
    """
    


# add element in csv file:-
name=input("what's your name:").title().strip()
home=input("enter your home:").title().strip()

with open("students.csv","a") as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])              #The csv.DictWriter class in Python's csv module is used to write rows to a CSV file using a dictionary, where the dictionary keys are used as the column headers.
    #writer=csv.writer(file,)
    writer.writerow({"name":name,"home":home})
