import time
from random import randint


class NormalEnemy:
    def __init__(self):
        self.names = ["Goblin", "Devilish Imp", "Evil Gnome", "Werewolf", "Ogre", "Bear Assassin", "Bear Monk"]
        self.name = self.names[randint(0, len(self.names)-1)]
        self.hp = 30
        self.atk = 15
        self.death_quotes = ("Fuck you Boots, furry bastard",
                             "My friends will avenge me, bearman!",
                             "I hope you step on a bear trap",
                             "Furry wizard fuck")
        print(f"{self.name} APPEARS!")

    def buff_attack(self):
        print(f"{self.name} ATTEMPTS TO CAST -BUFF ATTACK-")
        time.sleep(1.5)
        flip = randint(0, 1)
        if flip == 0:
            print("SUCCESS")
            time.sleep(1.5)
            self.atk += 5
            print(f"{self.name} GETS +5 ATK")
            time.sleep(1.5)
        else:
            print("FAIL")
            time.sleep(1.5)

    def normal_atk(self, boots):
        buff = randint(0, 1)
        if buff == 0:
            self.buff_attack()
        print(f"{self.name} ATTACKS BOOTS FOR {self.atk} DMG")
        boots.hp -= self.atk

    def check_death(self):
        if self.hp <= 0:
            print(f"{self.name}: {self.death_quotes[randint(0, len(self.death_quotes)-1)]}")
            time.sleep(2)
            print(f"{self.name} DIES")
            time.sleep(2)
            return True
        return False


class UndeadNormalEnemy:
    def __init__(self, name):
        self.name = f"Undead {name}"
        self.quote = f"{self.name}: I serve Boots!"
