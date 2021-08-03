def displayInventory(inventory):
    print("Inventory:")
    print()
    item_total = 0
    
    for k, v in inventory.items():
        item_total += v
        print(f"{k}: {v}")

    print(f"Total item: {item_total}")

def addToInventory(inventory, addedItems):    
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item,1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']            

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)    