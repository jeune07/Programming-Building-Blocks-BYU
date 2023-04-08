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


def main():
    # Call the read_dictionary function and store the compound dictionary in a variable named products_dict.
    products_dict = read_dictionary("products.csv", 0)
    # Print the products_dict.
    print(products_dict)

    # Open the request.csv file for reading.
    with open("request.csv") as request_file:
        # Create a CSV reader.
        reader = csv.reader(request_file)

        # Skip the first line of the request.csv file because the first line contains column headings.
        next(reader)

        # Use a loop that reads and processes each row from the request.csv file.
        for row in reader:
            # Use the requested product number to find the corresponding item in the products_dict.
            product_number = row[0]
            quantity = int(row[1])
            if product_number in products_dict:
                product_name = products_dict[product_number][0]
                product_price = float(products_dict[product_number][1])
                # Print the product name, requested quantity, and product price.
                print(f"{product_name} ({product_number}): {quantity} x ${product_price:.2f} = ${quantity*product_price:.2f}")
            else:
                print(f"Unknown product: {product_number}")


# Call the main function.
if __name__ == "__main__":
    main()
