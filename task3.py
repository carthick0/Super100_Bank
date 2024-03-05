class Product:
    def __init__(self, name, price, stock_quantity):
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity

    def remove_item(self, product, quantity):
        if product in self.items:
            self.items[product] -= quantity
            if self.items[product] <= 0:
                del self.items[product]

    def view_cart(self):
        total_price = 0
        print("Shopping Cart:")
        for product, quantity in self.items.items():
            total_price += product.price * quantity
            print(f"{product.name}: {quantity} x ${product.price} = ${product.price * quantity}")
        print(f"Total Price: ${total_price}")

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def add_to_order_history(self, order):
        self.order_history.append(order)

# Example Usage:
# Creating some products
product1 = Product("Laptop", 999, 10)
product2 = Product("Headphones", 99, 20)

# Creating a user
user1 = User("karthikeya", "saikarthikeya")

# Creating a shopping cart
cart1 = ShoppingCart()

# Adding products to the cart
cart1.add_item(product1, 2)
cart1.add_item(product2, 1)


# Viewing the updated cart
cart1.view_cart()

# Adding the cart to the user's order history
user1.add_to_order_history(cart1)
