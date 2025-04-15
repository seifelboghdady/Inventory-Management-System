from collections import defaultdict, Counter, OrderedDict
class inventory :
    def __init__ (self):
        self.product = defaultdict(int)
        self.sales_product = Counter()

    def add_product(self, name, quantity):
        self.product[name] += quantity

    def sell_product(self, name, quantity):
        self.product[name] -= quantity
        self.sales_product[name] += quantity

    def track_top_selling(self):
        print(f"The Top Sell is ")
        for name, quantity in self.sales_product.most_common(2):
            print(f"{name} : {quantity}")
        

    def Display(self):
        print("Inventory products =>",end ="")
        for name, quantity in self.product.items():
            print(f"{name} : {quantity}")

inv1 = inventory()
inv1.add_product("banana",4)
inv1.add_product("banana", 3)
inv1.Display()
inv1.sell_product("banana", 2)
inv1.Display()
inv1.add_product("apple", 6)
inv1.add_product("orange", 13)
inv1.sell_product("orange", 12)
inv1.track_top_selling()
inv1.sell_product("apple", 5)
inv1.track_top_selling()