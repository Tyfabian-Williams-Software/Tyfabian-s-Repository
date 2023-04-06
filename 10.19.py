# Tyfabian Williams
# 2142655

# Tyfabian Williams
# 2142655

class ItemToPurchase:

    def __init__(self, name1="none", price1=0, quantity1=0, description1="none"):
        self.item_name = name1
        self.item_price = price1
        self.item_quantity = quantity1
        self.item_description = description1

    def print_item_cost(self):
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}")

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        found = False
        for i, cart_item in enumerate(self.cart_items):
            if cart_item.item_name == item.item_name:
                self.cart_items[i] = item
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for item in self.cart_items:
            num_items += item.item_quantity
        return num_items

    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
            print("Number of Items: {}".format(self.get_num_items_in_cart()))
            print()
            for item in self.cart_items:
                item_total = item.item_price * item.item_quantity
                print("{} {} @ ${} = ${}".format(item.item_name, item.item_quantity, item.item_price, item_total))
            print()
            print("Total: ${}".format(self.get_cost_of_cart()))

    def print_descriptions(self):
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Item Descriptions")
        print()
        for item in self.cart_items:
            print("{}: {}".format(item.item_name, item.item_description))
        print()


def print_menu(cart):
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print('q - Quit')
    print()

    while True:

        option = input("Choose an option:\n")
        if option == 'a':
            item_name = input("Enter the item name: ")
            item_description = input("Enter the item description: ")
            item_price = int(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            cart.add_item(ItemToPurchase(item_name, item_price , item_quantity, item_description))
        elif option == 'r':
            item_name = input("Enter the item name: ")
            cart.remove_item(item_name)
        elif option == 'c':
            item_name = input("Enter the item name: ")
            item_quantity = int(input("Enter the new quantity: "))
            cart.modify_item(ItemToPurchase(item_name, 0, item_quantity, ''))
        elif option == 'i':
            cart.print_total()
        elif option == 'o':
            cart.print_descriptions()
        elif option == 'q':
            break

def main():
    cart = ShoppingCart()
    print_menu(cart)


if __name__ == "__main__":
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n\n")
    print("Customer name:", customer_name)
    print("Today's date:", current_date)
    main()