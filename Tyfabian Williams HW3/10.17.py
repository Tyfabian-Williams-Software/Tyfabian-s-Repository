# Tyfabian Williams
# 2142655

class ItemToPurchase:

    def init(self, item_name="None"):
        self.item_name = item_name
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}')


if __name__ == '__main__':

    print("Item 1")

    item1 = ItemToPurchase()
    item2 = ItemToPurchase()

    item1.item_name = input("Enter the item name:\n")
    item1.item_price = int(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))

    print()
    print('Item 2')
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = int(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))

    total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
    print()
    print('TOTAL COST')
    print(f'{item1.item_name} {item1.item_quantity} @ ${item1.item_price} = ${item1.item_quantity * item1.item_price}')
    print(f'{item2.item_name} {item2.item_quantity} @ ${item2.item_price} = ${item2.item_quantity * item2.item_price}')
    print()
    print(f'Total: ${total}')
