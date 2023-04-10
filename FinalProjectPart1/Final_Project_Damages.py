#Tyfabian Williams
#2142655

import csv
from datetime import datetime


def get_man_values(item):
    return items[item]['manufacturer']


def get_price_values(item):
    return items[item]['price']


def get_service_date_values(item):
    return datetime.strptime(items[item]['service_date'], "%m/%d/%Y").date()


class Inv_output:

    def __init__(self, item_list):
        self.item_list = item_list

    def full_inv(self):
        with open('FullInventory.csv', 'w') as file:
            keys = sorted(items.keys(), key=get_man_values)
            for item in keys:
                id = item
                manufact_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, manufact_name, item_type, price, service_date, damaged))

    def by_type(self):
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
                for type in types:
                    file_name = type.capitalize() + 'Inventory.csv'
                    with open(file_name, 'w') as file:
                        for item in keys:
                            id = item
                            man_name = items[item]['manufacturer']
                            price = items[item]['price']
                            service_date = items[item]['service_date']
                            damaged = items[item]['damaged']
                            item_type = items[item]['item_type']
                            if type == item_type:
                                file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))

    def pastService(self):
        items = self.item_list
        keys = sorted(items.keys(), key=get_service_date_values, reverse=False)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))

    def damaged(self):
        items = self.item_list
        keys = sorted(items.keys(), key=get_price_values, reverse=True)
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))


if __name__ == "__main__":
    items = {}

    files = ["ManufacturerList.csv", "PriceList.csv", "ServiceDatesList.csv"]
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                # print(line)
                # print()
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manufact_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manufact_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:

                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:

                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    # print('-----')

Inventory = Inv_output(items)
Inventory.damaged()

