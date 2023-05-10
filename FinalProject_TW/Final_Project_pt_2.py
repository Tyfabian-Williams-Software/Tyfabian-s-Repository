#Tyfabian Williams
#2142655

import csv
from datetime import datetime


def get_price(item):
    return item['price']


def convert_date(date_str):
    # Convert date string to datetime object
    try:
        date = datetime.strptime(date_str, "%m/%d/%Y")
        return date.strftime("%Y-%m-%d")  # Convert back to string in 'YYYY-MM-DD' format
    except ValueError:
        return None


def find_matching_items(items, manufacturer, item_type):
    #find any matching items in the inventory, excluding those after service date or damaged
    matching_items = []
    for item_id, item in items.items():
        if item['manufacturer'].lower() == manufacturer.lower() and item['item_type'].lower() == item_type.lower():
            if 'service_date' in item and convert_date(item['service_date']) > '2023-05-08':
                continue
            if 'damaged' in item and item['damaged'].lower() == 'damaged':
                continue
            matching_items.append((item_id, item))
    return matching_items


def find_similar_item(items, manufacturer, item_type, price):
    #finds a similar item by checking if manufacturer does not match but item type does. Price
    similar_item = None
    for item_id, item in items.items():
        if item['manufacturer'].lower() != manufacturer.lower() and item['item_type'].lower() == item_type.lower():
            if 'service_date' in item and convert_date(item['service_date']) > '2023-05-08':
                continue
            if 'damaged' in item and item['damaged'].lower() == 'damaged':
                continue
            item_price = float(item['price'])
            if similar_item is None or abs(item_price - price) < abs(float(similar_item['price']) - price):
                similar_item = item
    return similar_item

#
if __name__ == "__main__":
    #code used from project pt one to create a nested dictionary in a dictionary for traversal and query searches
    items = {}

    files = ["ManufacturerList.csv", "PriceList.csv", "ServiceDatesList.csv"]
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
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

    while True:
        query = input("Enter manufacturer and item type (or 'q' to quit):\n")
        if query.lower() == 'q':
            print("Goodbye!!")
            break

        # Extract manufacturer and item type using string methods and dictionary
        query_parts = query.split()
        if len(query_parts) < 2:
            print("Invalid query. Please provide both manufacturer and item type.")
            continue

        manufacturer = ''
        item_type = ''

        for word in query_parts:
            for items_id in items:
                if word.lower() in items[items_id]['manufacturer'].lower():
                    manufacturer = word
                elif word.lower() in items[items_id]['item_type'].lower():
                    item_type = word



        #get matching items with only the most expensive being printed
        matching_items = find_matching_items(items, manufacturer, item_type)

        if len(matching_items) == 0:
            print("No such item in inventory")
        elif len(matching_items) >= 1:
            max_price = 0
            max_price_item = None
            for item_id, item in matching_items:
                price = float(get_price(item))
                if price > max_price:
                    max_price = price
                    max_price_item = item

            item_id = matching_items[0][0]
            item = max_price_item
            price = float(get_price(item))

            print(f"Your item is: {item_id}, {item['manufacturer']}, {item['item_type']}, ${item['price']}")

            #getting a similar item by calling the function and only printing if it does not equal none
            similar_item = find_similar_item(items, manufacturer, item_type, price)


            if similar_item is not None:
                print(f"You may also consider: {similar_item['manufacturer']}, {similar_item['item_type']}, ${get_price(similar_item)}")

