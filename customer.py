from restaurant import Customer

class CustomerActions:
    
    def __init__(self):
        customer = Customer("menu.txt", "order.txt","paybill.txt")
        self.customer = customer

    def display_menu(self):
        self.customer.display_menu()

    def place_order(self):
        product_id = int(input("Enter product ID to order: "))
        quantity = int(input("Enter quantity: "))
        self.customer.place_order(product_id, quantity)

    def pay_bill(self):
        customer = Customer("menu.txt", "order.txt", "paybill.txt")
        customer.pay_bill()
    