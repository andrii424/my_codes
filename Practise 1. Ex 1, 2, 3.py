# class Car:
#     def __init__(self, производитель, цвет, вес):
#         self.производитель = производитель
#         self.цвет = цвет
#         self.вес = вес

#     def __str__(self):
#         return f"Автомобиль: марка={self.производитель}, цвет={self.цвет}, вес={self.вес}"

#     def __eq__(self, другой):
#         return self.производитель == другой.производитель and self.цвет == другой.цвет

#     def __ge__(self, другой):
#         return self.вес >= другой.вес


# # Создание трех экземпляров класса Car
# автомобиль1 = Car("BMW", "Красный", 1400)
# автомобиль2 = Car("Mercedes", "Синий", 1600)
# автомобиль3 = Car("Audi", "Серый", 1500)

# # Демонстрация метода __str__
# print(автомобиль1)  # Автомобиль: марка=BMW, цвет=Красный, вес=1400
# print(автомобиль2)  # Автомобиль: марка=Mercedes, цвет=Синий, вес=1600
# print(автомобиль3)  # Автомобиль: марка=Audi, цвет=Серый, вес=1500

# # Демонстрация метода __eq__
# print(автомобиль1 == автомобиль2)  # False
# print(автомобиль1 == Car("BMW", "Красный", 1000))  # False
# print(автомобиль1 == Car("BMW", "Красный", 1400))  # True

# # Демонстрация метода __ge__
# print(автомобиль1 >= автомобиль2)  # False
# print(автомобиль2 >= автомобиль3)  # True
# print(автомобиль3 >= автомобиль1)  # True

class Hero:

    def __init__(self, name, damage, health=100):
        self.name = name 
        if damage>0:
            self.damage = damage 
        if health>0:
            self.health = health
        else:
            health = 100

    def set_damage(self, damage):
        if damage>0:
            self.damage=damage
    
    def hit(self, other):
        if isinstance(self, Hero):
            other.health = other.health - self.damage
    def heal(self, num):
        self.health = self.health + num

hero1 = Hero("xxx", 16, 150)
hero2 = Hero("zxcrused", 5, 200)

hero2.heal(20)
hero1.hit(hero2)
print(hero2.health)

        