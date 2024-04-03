import random
class Hero:
    def __init__(self, name,  min_damage, max_damage, health=100):
        
        self.health = health
        self.name = name
        self.min_damage = min_damage
        self.max_damage = max_damage

    def hit(self, other):
        damage = random.randint(self.min_damage, self.max_damage) 
        other.health -= damage
        
    def __del__ (self):
        if self.health <= 0:
            print(f"{self.name} is dead")

    def winner (self):
        if self.health > 0:
            print(f"{self.name} is winner")
        

        

hero1 = Hero("Igor", 12, 30)
hero2 = Hero("Andrii", 15, 25)

while hero2.health > 0 and hero1.health > 0:
    hero1.hit(hero2)
    hero2.hit(hero1)
    print(hero1.name, hero1.health)
    print(hero2.name, hero2.health)

if hero1.health>0:
    hero1.winner()

elif hero2.health>0:
    hero2.winner()