class Item(object):
    def __init__(self, name):
        self.name = name

class Weapon(Item):
    def __init__(self, name, damage):
        super(Weapon, self).__init(name)
        self.damage = damage

class Armor(Item):
    def __init__(self, name, armor_amt):
        super(Armor)

print("")
def attack(self, target):