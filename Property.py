class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print("No")

my_back = Backpack()

print(my_back.items)
my_back.items = ['Walter', 'Pen']

print(my_back.items)

