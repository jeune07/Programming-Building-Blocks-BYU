import csv

def read_dictionary(filename, key_column_index):
    # Create an empty dictionary.
    dictionary = {}

    # Open the CSV file.
    with open(filename) as products_file:
        # Create a CSV reader.
        reader = csv.reader(products_file)
        # Read the header row.
        header = next(reader)
        # Read the remaining rows.
        for row in reader:
            # Get the key from the row.
            #key = row[key_column_index]
            product=row[0]
            name=row[1]
            price=row[2]

            dictionary[product] = [name,price]

            # Create a new dictionary for this key.
            # dictionary[key] = {}


            # Add the other columns to the dictionary.
            # for i in range(len(header)):
            #     if i != key_column_index:
            #         dictionary[key][header[i]] = row[i]

    # Return the dictionary.
    return dictionary

# Call the read_dictionary function.
dictionary = read_dictionary("products.csv", "product")
print(dictionary)
