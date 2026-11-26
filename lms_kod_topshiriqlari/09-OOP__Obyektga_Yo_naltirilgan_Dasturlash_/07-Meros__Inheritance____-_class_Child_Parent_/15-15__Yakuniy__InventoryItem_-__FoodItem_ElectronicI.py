class InventoryItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def final_price(self):
        return self.price
class FoodItem(InventoryItem):
    def final_price(self):
        return self.price * 1.05
class ElectronicItem(InventoryItem):
    def final_price(self):
        return self.price * 1.20
kind = input().strip()
name = input().strip()
try:
    price = int(input().strip())
except ValueError:
    print("BAD")
else:
    classes = {"FOOD": FoodItem, "ELEC": ElectronicItem}
    if kind in classes and name and price >= 0:
        print(int(classes[kind](name, price).final_price()))
    else:
        print("BAD")
    
    
    