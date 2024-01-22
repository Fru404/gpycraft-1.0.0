with open('/workspaces/gpycraft-1.0.0/formatted_output_file.csv', 'a') as file:
    # Create a string representing your row of data
    
    data_row = "For .the .Lord. sake" # Modify this line based on your data format
    values = data_row.strip().split('.')

        # Format the row with tabs and indentation
    row = '\n'.join([f'{val}{" " * 50}' for val in values]) + '\n'

    # Append the data to the file
    file.write(row)

text = "Hello world"
spaced_text = text + " " * 50 + " me" # Add 5 spaces
print(spaced_text)

value1 = "apple"
value2 = "orange"
value3 = "banana"

data_row = f'{value1}\t{" " * 50}{value2}\t{value3}'
print(data_row)


# Assuming your input string has multiple lines, and each line represents a record
input_data = "John Doe.25.USA.Senior\nJane Smith.30.Canada.Junior\n"

# Split the input data into records based on newline characters
records = input_data.strip().split('\n')
print(input_data)
# Process each record
for record in records:
    # Split each record into fields based on dots
    fields = record.split('.')

    # Extract values for name, age, country, and class
    name, age, country, class_ = fields

    # Do something with the extracted values (e.g., print them)
    print(f"Name: {name}, Age: {age}, Country: {country}, Class: {class_}")
