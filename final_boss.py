import time
from random import randint


class FinalBoss:
    def __init__(self):
        self.name = "Allan the Unbeatable"
        self.hp = 1000000
        self.atk_quotes = ["You cannot stop me bearman",
                           "Boot dev is returning to a simpler time, without you",
                           "I cannot die, you cannot live"]
        self.death_quote = None
        self.weaknesses = None
        self.godlike = True
        print("Boots returns Zil's gems to the crab throne")
        time.sleep(2.5)
        print("Footsteps coming from behind catches Boots' attention")
        time.sleep(2.5)
        print(f"{self.name} dual wielding wands appears")
        time.sleep(2.5)
        print(f"{self.name}: You think I'm gonna let you get away with this after what you"
              f"did in the server room?")

    def atk(self, boots):
        print(f"{self.name}: {self.atk_quotes[randint(0, len(self.atk_quotes)-1)]}")
        time.sleep(3)
        self.heal()
        time.sleep(2)
        self.arcane_missiles(boots)

    def heal(self):
        print(f"{self.name} HEALS TO FULL HP")
        time.sleep(2)
        self.hp = 1000000

    def arcane_missiles(self, boots):
        print(f"--- {self.name} casts arcane missiles ---")
        time.sleep(2)
        print("--- MISSILE HITS BOOTS FOR 25 DMG")
        time.sleep(1)
        print("--- MISSILE HITS BOOTS FOR 25 DMG")
        time.sleep(1)
        print("--- MISSILE HITS BOOTS FOR 25 DMG")
        time.sleep(1)
        print("--- MISSILE HITS BOOTS FOR 25 DMG")
        time.sleep(1)
        boots.hp -= 100
