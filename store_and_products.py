class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def show_all(self):
        return print("me")
    
    def add_product(self, new_product):
        self.products.append(new_product)
        return f"Products: {self.products}"
    
    def sell_product(self, id):
        self.products.pop(int(id))
        return f"Products: {self.products}"
    
    def inflation(self, percent_increase):
        for i in self.products:
            self.products.append(i * percent_increase)
        return f"Products: {self.products}"

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
    
    def show_info(self):
        return f"Product info: {self.name}, {self.price}, {self.category}"

    def update_price(self, percent_change, is_increased):
        new_price = percent_change * self.price
        if is_increased == True:
            self.price += new_price
        else:
            self.price -= new_price
        return f"New Price: {self.price}"



product_1 = Product("Detergent", "14.99", "Households")
store_1 = Store("Munch").add_product(product_1)
print(product_1.show_info())
print(store_1)