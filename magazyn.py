
items = [
    {"Name":"Milk", "Quantity": 120, "Unit": "l", "Unit Price (PLN)": 2.3},
    {"Name":"Sugar", "Quantity": 1000, "Unit": "kg", "Unit Price (PLN)": 3},
    {"Name":"Flour", "Quantity": 12000, "Unit": "kg", "Unit Price (PLN)": 1.2},
    {"Name":"Coffee", "Quantity": 25, "Unit": "kg", "Unit Price (PLN)": 40}
]

sold_items = []

def get_items(items):
    print("{:<10s}{:>7s}{:>9s}{:>20s}".format("Name","Quantity","Unit","Unit Price (PLN)"))
    dash = "-" * 47
    print(dash)
    for i in range(len(items)):
        print("{:<10s}{:>7d}{:>9s}{:>14.1f}".format(list(items[i].values())[0],list(items[i].values())[1],list(items[i].values())[2],list(items[i].values())[3]))

def add_item(items):
    print("Adding to warhouse...")
    name = str(input("Item name: ")) 
    quantity = int(input("Quantity: "))
    unit_name = str(input("Unit name: "))
    unit_price = float(input("Unit Price: "))
    items.append({"Name":name, "Quantity": quantity, "Unit": unit_name, "Unit Price (PLN)": unit_price})
    get_items(items)

def sell_item(items):
    name = str(input("Item name: "))
    quantity_to_sell = int(input("Quantity to sell: "))
    for i in range(len(items)):
        if items[i]["Name"] == name:
            items[i]["Quantity"] = items[i]["Quantity"] - quantity_to_sell
    
    get_items(items)

def menu(items):
    message = print("What would you like to do?: ")
    command = input().lower()
    if command == "exit":
        print("Exiting.... Bye!!")
        exit(1)
    elif command == "show":
        get_items(items)
    elif command == "add":
        add_item(items)
    elif command == "sell":
        sell_item(items)
    return message




if __name__ == "__main__":
    while True:
        menu(items)
        
