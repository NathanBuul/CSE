
class Item(object):
    def __init__(self, name):
        self.name = name


class Food(Item):
    def __init__(self, name, health):
        super(Food, self).__init__(name)
        self.food = health


class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init__(name)
        self.damage = damage


class LegendaryBubbleGun(Weapon):
    def __init__(self, name):
        super(LegendaryBubbleGun, self).__init__(name, 400)


class Smoothie(Food):
    def __init__(self, name):
        super(Smoothie, self).__init__(name, 100)


class LegendaryApple(Food):
    def __init__(self, name):
        super(LegendaryApple, self).__init__(name, 400)


class SuperJuice(Food):
    def __init__(self, name):
        super(SuperJuice, self).__init__(name, 400)


class Grenade(Item):
    def __init__(self, name):
        super(Grenade, self).__init__(name)
        self.attack_damage = 200


class SuperGrenade(Weapon):
    def __init__(self, name):
        super(SuperGrenade, self).__init__(name, 400)
        self.attack_damage = 400


class Juice(Food):
    def __init__(self, name):
        super(Juice, self).__init__(name, 200)


class Soda(Food):
    def __init__(self, name):
        super(Soda, self).__init__(name, 350)


class Yogurt(Food):
    def __init__(self, name):
        super(Yogurt, self).__init__(name, 400)


class BubbleGun(Item):
    def __init__(self, name):
        super(BubbleGun, self).__init__(name)
        self.attack_damage = 200


class Stick(Item):
    def __init__(self, name):
        super(Stick, self).__init__(name)
        self.attack_damage = 400


class PetBabyDragon(Item):
    def __init__(self, name):
        super(PetBabyDragon, self).__init__(name)
        self.attack_damage = 200


class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor, self).__init__(name)
        self.armor_amt = armor_amt


class Apple(Food):
    def __init__(self, name):
        super(Apple, self).__init__(name, 25)


class Banana(Food):
    def __init__(self, name):
        super(Banana, self).__init__(name, 50)
        self.health = 50


class Knife(Item):
    def __init__(self, name):
        super(Knife, self).__init__(name)
        self.attack_damage = 100


class Character (object):
    def __init__(self, name, health, weapon, armor):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.armor = armor

    def take_damage(self, damage):
        if damage < self.armor.armor_amt:
            print("No damage is done")
        else:
            self.health -= damage - self.armor.armor_amt
            if self.health < 0:
                self.health = 0
                print("%s has fallen" % self.name)
            print("% has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" %
              (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)
