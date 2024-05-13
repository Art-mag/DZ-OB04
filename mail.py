from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Дополнительное оружие можно добавить здесь

# Класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

class Monster:
    def __init__(self, lives):
        self.lives = lives

    def isDefeated(self):
        return self.lives <= 0

    def takeDamage(self):
        self.lives -= 1

# Реализация боя
def fight(fighter, monster):
    print(fighter.attack())
    monster.takeDamage()
    if monster.isDefeated():
        print("Монстр побежден!")

# Пример использования
print("Боец выбирает меч.")
fighter = Fighter(Sword())  # Боец выбирает меч
monster = Monster(1)  # Монстр с 1 жизнью
fight(fighter, monster)

print("\nБоец выбирает лук.")
fighter.changeWeapon(Bow())  # Боец выбирает лук
monster = Monster(1)  # Новый монстр с 1 жизнью
fight(fighter, monster)
