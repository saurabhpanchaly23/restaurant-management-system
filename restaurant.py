class Restaurant:
    def __init__(self, menu_file, order_file, bill_file):
        self.menu_file = menu_file
        self.order_file = order_file
        self.bill_file = bill_file

class Admin (Restaurant):
    
    def display_menu(self):
        try:
            with open("menu.txt", 'r') as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("file not found Please check Your Menu File")
        else:
            print("--------------------------")

    def add_product(self, product_id, name, price, quantity):
        try:
            with open("menu.txt", 'a') as file:
                file.write(f"{product_id},{name},{price},{quantity}\n")
            print("Product added successfully.")
        except IOError as e:
            print(f"Error adding product: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        else:
            print("------------------------------")

    def update_product(self, product_id, new_price, new_quantity):
        try:
            lines = []
            with open("menu.txt", 'r') as file:
                for line in file:
                    if line.startswith(str(product_id)):
                        parts = line.strip().split(',')
                        name = parts[1]
                        line = f"{product_id},{name},{new_price},{new_quantity}\n"
                    lines.append(line)
            with open("menu.txt", 'w') as file:
                for line in lines:
                    file.write(line)
        except FileNotFoundError:
            print("Menu file not Found")
        else:
            print("-----------------------------------")
            
    def delete_product(self, product_id):
        lines = []
        with open("menu.txt", 'r') as file:
            for line in file:
                if not line.startswith(str(product_id)):
                    lines.append(line)
                else:
                    print("product not found")
            with open("menu.txt", 'w') as file:
                for line in lines:
                    file.write(line)
                print("Product is deleted")
            
    def search_product(self, product_id):
        with open("menu.txt", 'r') as file:
            for line in file:
                if line.startswith(str(product_id)):
                    print(line.strip())
                    return
            print("Product not found.")
            print("-----------------------------------")

class Customer(Restaurant):
    
    def display_menu(self):
        with open("menu.txt", "r") as file:
            for line in file:
                print(line.strip())
        print("--------------------------------")

    def place_order(self, product_id, quantity):
        products = []
        order_details = None
        try:
            with open("menu.txt", "r") as fp:
                for p in fp:
                    product_data = p.split(',')
                    if product_data[0] == str(product_id):
                        product_name = product_data[1]
                        product_price = float(product_data[2])
                        available_quantity = int(product_data[3])

                        if quantity > available_quantity:
                            print("Insufficient product quantity.")
                            return

                        total_cost = product_price * quantity
                        remaining_quantity = available_quantity - quantity
                        order_details = {
                            'product_id': str(product_id),
                            'product_name': product_name,
                            'product_price': str(product_price),
                            'remaining_quantity': str(remaining_quantity),
                            'total_cost': str(total_cost),
                        }
                        updated_product_info = f"{product_id},{product_name},{product_price},{remaining_quantity}\n"
                        products.append(updated_product_info)
                    else:
                        products.append(p.strip())

            if order_details:
                with open("order.txt", "w") as order_file:
                    order_file.write("Product: " + order_details['product_id'] + "\n")
                    order_file.write("Product Name: " + order_details['product_name'] + "\n")
                    order_file.write("Quantity: " + str(quantity) + "\n")
                    order_file.write("Cost: " + order_details['total_cost'] + "\n")

                with open("menu.txt", "w") as file:
                    for e in products:
                        file.write(e)

                print("Order Placed Successfully.")
            else:
                print("Product not found.")

        except FileNotFoundError:
            print("File not found. Please check the menu file.")
        except IOError as e:
            print(f"Error: {e}. Could not place the order.")

    def pay_bill(self):
        try:
            total_bill = 0
            order_file_path = "order.txt"
            with open("order.txt", "r") as order_file:
                for line in order_file:
                    if line.startswith("Cost:"):
                        total_bill += float(line.split(":")[1].strip())
            if total_bill > 0:
                with open("paybill.txt", "w") as paybill_file:
                    paybill_file.write(f"Total Bill: Rs {total_bill:.2f}\n")
                print(f"Total Bill: Rs {total_bill:.2f}")
                # Clear the order file after payment
                with open("order.txt", 'w'):
                    pass  # This line clears the content of the order file
            else:
                print("No pending orders.")

        except FileNotFoundError:
            print("Order file not found.")
        except ValueError:
            print("Error reading bill information.")
        print("-------------------------------")

        # ... (Other methods remain unchanged)

    def clear_order_file(self, order_file_path):
        try:
            with open("order.txt", 'w') as order_file:
                order_file.write("")  # Clear the content of the order file
            print("Order file cleared successfully.")
        except FileNotFoundError:
            print(f"Error: {order_file_path} not found.")
        except IOError as e:
            print(f"Error: {e}. Could not clear the order file.")