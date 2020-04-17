from textwrap import dedent

welcome_text ="""**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************"""

order_text ="""***********************************
** What would you like to order? **
***********************************
"""

menu_item = {
    "Appetizers":{
        "wings": 0,
        "cookies": 0,
        "spring rolls": 0
    },
    "Entrees":{
        "salmon": 0,
        "steak": 0,
        "meat tornado": 0,
        "a literal garden": 0
    },
    "Desserts":{
        "ice cream": 0,
        "cake": 0,
        "pie": 0
    },
    "Drinks":{
        "coffee": 0,
        "tea": 0,
        "unicorn tears": 0
    }
}

def print_menuitems():
    for itemType in menu_item:        
        print(dedent(f"""
        {itemType}
        ----------"""))        
        for item in menu_item[itemType]:            
            print(item.title())
        print("\n")

def take_order_details(order_input):
    for itemType in menu_item:
        current_Item_Type = menu_item[itemType]
        for item in current_Item_Type:
            if order_input == item:
                quantity = current_Item_Type[order_input]
                quantity += 1
                current_Item_Type[order_input] = quantity
                print(f"** {quantity} order of {order_input} have been added to your meal **")
                return
    print(f"** Sorry '{order_input}' does not exists in Menu **")

if __name__ == "__main__":
    print(dedent(welcome_text))    
    print_menuitems()
    order = input(dedent(order_text))
    while order.lower() != "quit":
        take_order_details(order.lower())
        order = input(dedent(order_text))