from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass


class Sword(Weapon):
    def __init__(self, name,  damage):
        self.name = name
        self.damage = damage

    def attack(self, monster):
        print("Боец наносит удар мечом.")
        monster.health -= self.damage
        if monster.health <= 0:
            print("Монстр побежден!")
        else:
            print("Монстр ранен!")


class Bow(Weapon):
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self, monster):
        print("Боец делает выстрел из лука.")
        monster.health -= self.damage
        if monster.health <= 0:
            print("Монстр побежден!")
        else:
            print("Монстр ранен!")


class Fighter():
    def __init__(self, health, strength, weapon: Weapon):
        self.health = health
        self.strength = strength
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"Боец выбирает {new_weapon.name}")

    def hit(self, monster):
        self.weapon.attack(monster)


class Monster():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength


sword = Sword("меч", 90)
bow = Bow("лук", 70)

fighter = Fighter(100, 80, bow)
monster1 = Monster(100, 60)

fighter.change_weapon(bow)
fighter.hit(monster1)

fighter.change_weapon(sword)
fighter.hit(monster1)
