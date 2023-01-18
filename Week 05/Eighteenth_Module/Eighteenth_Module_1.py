""" Attributes Validation Using Assert """

""" todo.txt =====>>

1. Attributes Validation Using Assert
2. Dynamic Attributes
3. Create classes from json in files
4. Multiply inheritance and MRO(Method Resolution Order) """

""" validate.py =====>> """


class Item:
    def __init__(self, itemName, itemPrice) -> None:
        self.itemName = itemName
        self.itemPrice = itemPrice


item = Item("plate", 150)
print(item.itemName, item.itemPrice)
