# class KgToPounds:

#     def __init__(self, kilo):
#         self._kilo = kilo

#     def kg_to_pounds(self):
#         return self._kilo * 2.6
    
#     def get_kg(self):
#         return self._kilo 
    
#     def set_kg(self, kilo):
#         if isinstance(kilo, (int, float)):
#             self._kilo = kilo
#         else:
#             print("Please enter a valid number")

#     solution = property(get_kg, set_kg)

    
class KgToPounds:

    def __init__(self, kilo):
        self._kilo = kilo

    def kg_to_pounds(self):
        return self._kilo * 2.6
    
    @property
    def kg(self):
        return self._kilo 
    @kg.setter
    def kg(self, kilo):
        if isinstance(kilo, (int, float)):
            self._kilo = kilo
        else:
            print("Please enter a valid number")


value = KgToPounds(15)

print(value.kg_to_pounds())
   