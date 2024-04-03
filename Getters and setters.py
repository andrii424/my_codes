import random
# class Players:

#     def __init__ (self, name):
#         self._name = name

#     def get_name(self):
#         return self._name
    
#     def set_name(self, new_name):
#         if isinstance (new_name, str):
#             self._name = new_name

#         else:
#             print("Please enter a name of the player")

    
class Cards:

    def __init__(self):
        return self
    
    def cards (self, scores):
        scores = random.randint(3, 10)
        return scores
    
    # def add_card(self):
    #     card = random.randint(self.min_card, self.max_card)

    
player_1 = Cards()

print (player_1.cards)







