import random

class Enemy:
    #variables-fields
    kind = "waraiths"

    #Attributes
    weaponsList = ["Pike","Bow","Slingshot", "Axe"]

    def __init__(self, name, tribe, specialAbility,):
        self.name = name
        self.tribe = tribe
        self.specialAbility = specialAbility
        self.weapon = random.choice(Enemy.weaponsList)

    #Behaviour
    def attack(self):
        print("The enemy attacks")

    def set_attack_mode(self):
        self.__mode = "medium"

    def get_attack_mode(self):
        print(self.__mode)



    def setWeapon(self, weapon):
        self.weapon = weapon
        if self.weapon == "Pike":
            print("The enemy delt 5 damage")
        elif self.weapon == "Bow":
            print("The enemy dealt 10 damage")

enemy1 = Enemy("Widow", "Mangalo", "Shroud")


class Wraith(Enemy)

    def __init__(self,location, enemyName, clan, speciaAbility):
        Enemy.__init__(self, enemyName,clan,speciaAbility)
        self.location = location

print(enemy1.kind)
print(enemy1.name)
print(enemy1.tribe)
print(enemy1.specialAbility)
enemy1.setWeapon("Pike")
print(enemy1.weapon)

enemy1.attack()