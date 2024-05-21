import re
import random
import string

# Define a function to generate a random 5-digit alphanumeric string
def generate_id():
    return f"[{''.join(random.choices(string.ascii_uppercase + string.digits, k=5))}]"

# Open the input file and read its contents
with open('Book of Wisdom.filter', 'r') as f:
    contents = f.read()

# Replace all instances of "[ID]" with a random 5-digit alphanumeric string
modified_contents = re.sub(r'\[ID\]', generate_id(), contents)

# Open the output file and write the modified contents
with open('output.filter', 'w') as f:
    f.write(modified_contents)