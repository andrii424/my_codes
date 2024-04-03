class Cashier:
    taxx = 0.05

    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_something(self, new_product, how_many=1):
        if new_product['name'] in self.products:
            self.products[new_product['name']]['how_many'] += how_many
        else:
            self.products[new_product['name']] = {'price': new_product['price'], 'how_many': how_many}
    
    def show_product(self):
        print(self.products)

    def remove_prod(self, product):
        del self.products[product]

    def update_price(self, product, new_price):
        self.products[product]['price'] = new_price

    def sub_total(self):
        total = 0
        for product in self.products.values():
            total += product['price'] * product['how_many']
            self.total = total
        return self.total
    
    def taxes(self):
        tax = self.total * Cashier.taxx
        self.tax = tax
        return round(self.tax, 2)
        
    def abs_total(self):
        af_tax = self.total + self.tax
        return round(af_tax, 2)

    def clear_purchase (self):
        self.products.clear()
        


product1 = {'name': 'Pizza', 'price': 3.99}
product2 = {'name': 'Milk', 'price': 1.99}
product3 = {'name': 'Chips', 'price': 2.79}

products = Cashier("Nora")

products.add_something(product1)
products.add_something(product1)
products.add_something(product2)

products.show_product()

print(products.sub_total())
print(products.taxes())
print(products.abs_total())

print(products.clear_purchase())
