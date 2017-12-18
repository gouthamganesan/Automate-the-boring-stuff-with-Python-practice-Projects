#!/usr/bin/python

from fantacyGameInventory import display_inventory


def add_to_inventory(inventory_arg, added_items_arg):
    for key in added_items_arg:
        inventory_arg.setdefault(key, 0)
        inventory_arg[key] += 1
    return inventory_arg


inventory_inp = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dragger', 'gold coin', 'gold coin', 'ruby']

inventory_inp = add_to_inventory(inventory_inp, dragonLoot)

display_inventory(inventory_inp)
