import re

def if_pangram(text):
    # Convert to lowercase and remove non-alphabet characters
    text = re.sub(r'[^a-z]', '', text.lower())
    # Check if there are 26 unique letters in the text
    if len(set(text)) == 26:
        print("pangram")
    else:
        print("not pangram")
        
text = input("Enter a string: ")
if_pangram(text)
