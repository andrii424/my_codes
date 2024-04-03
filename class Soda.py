class Soda:

    def __init__(self, what = None):
        if isinstance(what, str):
            self.what=what
        else:
            self.what = None

    def show_my_drink(self):
        if self.what:
            print(f"Soda with {self.what}")
        else:
            print("Common soda")


my_soda = Soda()

my_soda.show_my_drink()

        


        
        


         