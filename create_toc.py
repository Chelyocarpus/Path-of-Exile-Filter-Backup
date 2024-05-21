# Open the file in read mode
with open('Book of Wisdom.filter', 'r') as file:
    # Read all the lines in the file
    lines = file.readlines()

# Initialize an empty list to store the headers
headers = []

# Loop through each line in the file
for i in range(len(lines)):
    # Check if the line starts with the search string
    if lines[i].startswith('#======================================================================'):
        # Extract the header name from the line below it
        header_name = lines[i-1].strip()
        # Add the header to the list of headers
        if header_name:
            headers.append(header_name)

# Open a new file in write mode
with open('output.txt', 'w') as output_file:
    # Loop through each header and write it to the output file with a line break
    for header in headers:
        output_file.write(header + '\n')
