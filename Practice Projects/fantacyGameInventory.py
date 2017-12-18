#!/usr/bin/python


def display_inventory(inventory_arg):
    total_items = 0
    print("Inventory:")
    for key, value in inventory_arg.items():
        print(str(value) + " " + key)
        total_items += value    
    print("Total number of items: " + str(total_items))


inventory_inp = {'rope': 1, 'torch': 6,
                 'gold coin': 42, 'dagger': 1, 'arrow': 12}

display_inventory(inventory_inp)