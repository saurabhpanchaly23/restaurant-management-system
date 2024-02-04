from restaurant import Admin
    
class AdminActions:
    def __init__(self):
        admin = Admin("menu.txt", "order.txt", "paybill.txt")
        self.admin = admin

    def display_menu(self):
        self.admin.display_menu()

    def add_product(self):
        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        self.admin.add_product(product_id, name, price, quantity)

    def update_product(self):
        product_id = int(input("Enter product ID to update: "))
        new_price = float(input("Enter new price: "))
        new_quantity = int(input("Enter new quantity: "))
        self.admin.update_product(product_id, new_price, new_quantity)

    def delete_product(self):
        product_id = int(input("Enter product ID to delete: "))
        self.admin.delete_product(product_id)

    def search_product(self):
        product_id = int(input("Enter product ID to search: "))
        self.admin.search_product(product_id)