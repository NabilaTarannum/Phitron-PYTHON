""" Dynamic Attributes """


""" dynamic_attributes.py =====>> """


class Item:
    def __init__(self, itemName, itemPrice) -> None:
        self.itemName = itemName
        self.itemPrice = itemPrice


item1 = Item("Bowl", 100)
item2 = Item("Plate", 150)

print(item1.__dict__)
print(item2.__dict__)
