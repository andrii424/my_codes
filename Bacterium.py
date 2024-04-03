some = False

class Bacterium:

    def __init__(self, x, y, shape, health=100):
        self.x=x
        self.y=y
        self.shape = shape
        self.health = health

Bacilli = Bacterium(2, 1, 'rod-shaped')
Cocci = Bacterium(3, 2, 'sphere-shaped')
Spirilli = Bacterium(2, 1, 'spiral-shaped')

print(Bacilli.x, Bacilli.y, Bacilli.shape)
print(Cocci.x, Cocci.y, Cocci.shape)
print(Spirilli.x, Spirilli.y, Spirilli.shape)




try:
    hero_tall = int(input("What tall you have? "))
    hero_weigh = int(input("What weigh you have? "))
except:
    print("Write a number")

try: 
    class Hero: 

        def __init__(self, tall, weigh):
            if tall > 0 and weigh > 0:
                strength = (tall + weigh) / 8
                self.strength = round(strength)
                # self.strenght = int(strength)
            else:
                print("You are too small")

    main_hero = Hero(hero_tall, hero_weigh)
    print(main_hero.strength)
except:
    print("Try one more time")
    some = False

# Цикл для атаки бактерий
while Bacilli.health > 0 or Cocci.health > 0 or Spirilli.health > 0:
    try:
        inp = int(input("Which one do you want to hit? Pick Bacilli(1), Cocci(2), or Spirilli(3): "))
        some = True
    except:
        print("Pick number 1, 2, or 3")

    if some == True and inp == 1:
        Bacilli.health -= main_hero.strength
    elif some == True and inp == 2:
        Cocci.health -= main_hero.strength
    elif some == True and inp == 3:
        Spirilli.health -= main_hero.strength
    else:
        print("You wrote an incorrect number") 

    print("Bacilli health:", Bacilli.health)
    print("Cocci health:", Cocci.health)
    print("Spirilli health:", Spirilli.health)

print("All bacteria are killed!")
