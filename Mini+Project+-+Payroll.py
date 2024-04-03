class Some:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand


    # Getters
    
    def get_price(self):
        return self.get_price

    def get_size(self):
        return self.get_size

    def get_brand(self):
        return self.get_brand


    # Setters 

    def set_price(self, new_argument):
        if isinstance(new_argument, int):
            self._price = new_argument

        else:
            print("Don't like it. Try again")


    def set_size(self, new_size):
        if isinstance (new_size, float):
            self._size = new_size

        else:
            print("Don't like it. Try again")


    def set_brand(self, new_name):
        if isinstance(new_name, str):
            self._brand = new_name

        else:
            print("Don't like it. Try again")

    price = property(get_price, set_price)
    size = property(get_size, set_size)
    brand = property(get_brand, set_brand)











class Some:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand


    @property  
    def price(self):
        return self.get_price
    
    @property
    def size(self):
        return self.get_size
    
    @property
    def brand(self):
        return self.get_brand
    

    @price.setter
    def price(self, new_argument):
        if isinstance(new_argument, int):
            self._price = new_argument

        else:
            print("Don't like it. Try again")


    @size.setter
    def size(self, new_size):
        if isinstance (new_size, float):
            self._size = new_size

        else:
            print("Don't like it. Try again")


    @brand.setter
    def brand(self, new_name):
        if isinstance(new_name, str):
            self._brand = new_name

        else:
            print("Don't like it. Try again")


    


	