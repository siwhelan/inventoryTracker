from tabulate import tabulate


class Shoes:

    def __init__(self, country, code, product, cost, quantity):
        
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}"


# List to store shoes data


shoes_list = []


# Function to open and read the file inventory.txt,
# create a shoes object from the data and append it to the shoe list

def read_shoes_data():
    with open("inventory.txt", "r") as f:

        next(f)  # Skip the first line
        for line in f:

            try:
                country, code, product, cost, quantity = line.strip().split(",")
                cost = float(cost)
                quantity = int(quantity)
                shoe = Shoes(country, code, product, cost, quantity)
                shoes_list.append(shoe)

            except ValueError:
                print("Error reading data from file.")


# This function will allow a user to enter data about a shoe,
# use this data to create a shoe object 
# and append this object inside the shoe list.

def capture_shoes():
    country = input("Enter the country of origin: ")
    code = input("Enter the code: ")
    product = input("Enter the product name: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))
    shoe = Shoes(country, code, product, cost, quantity)
    shoes_list.append(shoe)
    update_inventory_file()


# Iterate over the shoes list and print the details of the shoes returned from the __str__ function.
# Print the info using tabulate

def view_all():
    data = [["Country", "Code", "Product", "Cost", "Quantity"]]
    for shoe in shoes_list:
        data.append([shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity])
    print(tabulate(data, headers="firstrow", tablefmt="pipe"))


# This function will find the shoe object with the lowest quantity
# Ask the user how many they'd like to add and then update the inventory

def re_stock():

    shoe_to_restock = min(shoes_list, key=lambda x: x.quantity)
    print(f"The shoe with the lowest quantity is: {shoe_to_restock}")
    add_qty = int(input("Enter the quantity to add: "))
    shoe_to_restock.quantity += add_qty
    update_inventory_file()


# Function to update the inventory with any changes

def update_inventory_file():
    with open("inventory.txt", "w") as f:
        f.write("country,code,product,cost,quantity\n")
        for shoe in shoes_list:
            f.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


# Function to search for a shoe from the list using the shoe's code
# and return this object so that it can be printed

def search_shoe(code):
    for shoe in shoes_list:
        if shoe.code == code:
            return shoe
    return None


# Function to calculate the total value for each item

def value_per_item():
    total_value = 0
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        total_value += value
        print(f'{shoe.product} - ' + str(total_value))


# Function to determine the product with the highest quantity
# and print this shoe as being for sale

def highest_qty():
    highest_qty_shoe = max(shoes_list, key=lambda x: x.quantity)
    print(f"{highest_qty_shoe} is now on sale!!")


# ===== Main Menu ===== #

def main():
    read_shoes_data()
    while True:
        print("\nMenu:")
        print("1. Capture shoes")
        print("2. View all shoes")
        print("3. Re-stock shoes")
        print("4. Search for a shoe")
        print("5. Calculate value per item")
        print("6. Find shoe with highest quantity")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            capture_shoes()
        elif choice == 2:
            view_all()
        elif choice == 3:
            re_stock()
        elif choice == 4:
            code = input("Enter the code of the shoe to search: ")
            shoe = search_shoe(code)
            if shoe is not None:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == 5:
            value_per_item()
        elif choice == 6:
            highest_qty()
        elif choice == 7:
            break
        else:
            print("Invalid choice.")


main()
