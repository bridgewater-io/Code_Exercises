inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)

first = inventory[0]

last = inventory[-1]

inventory_2_6 = inventory[2:6]

first_3 = inventory[:3]

twin_beds = inventory.count("twin bed")

removed_item = inventory.pop(4)

inventory.insert(10, "19th Century Bed Frame")

inventory.sort()

print(f"The length of the inventory list is {inventory_len}.\nThe first element in the inventory list is the {first}.\nThe last element in the inventory list is the {last}.\nLook how we can slice certain elements, like {inventory_2_6}, to display anything we want.\nLook, I can select the first three items here: {first_3}\nWe can also count the number of occurrences of the twin bed in the inventory list: {twin_beds}\nI can remove an element and store it in a variable here: {removed_item}\nInserting new items is also a breeze, notice how the 11th element of the list has changed: {inventory}\nFinally, sorting this list alphabetically is simple: {inventory}")
