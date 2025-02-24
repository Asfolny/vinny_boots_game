import time
from random import randint


class BossOne:
    def __init__(self):
        self.name = "Flip Flops"
        self.hp = 200
        self.atk_quotes = ["Try this fuckbear",
                           "You're just a little cub",
                           "Nice timbs, I prefer comfort",
                           "Front end is where it's at",
                           "Your little blue bug eyed friend isn't saving you"]
        self.death_quote = ("===FLIP FLOPS DEFEATED===\nFlip Flops: DAMN YOU BOOTS, TELL LANE I WILL HAVE MY REVENGE, "
                            "I SHOULD'VE BEEN THE MASCOT OF BOOT DEV\n*** Flip Flops DIES ***")
        print("I, FLIP FLOPS, AM THE TRUE WIZARD BEAR OF BOOT DEV")

    def check_death(self):
        if self.hp <= 0:
            return True
        return False

    def choose_random_atk(self, boots):
        print(f"{self.name}: {self.atk_quotes[randint(0, len(self.atk_quotes) - 1)]}")
        time.sleep(3)
        rand_atk = randint(0, 4)
        match rand_atk:
            case 0:
                self.drain_soul(boots)
            case 1:
                self.throw_sandal(boots)
            case 2:
                self.risky_bet(boots)
            case 3:
                self.naruto_shit(boots)
            case 4:
                self.backflip_of_doom(boots)

    def drain_soul(self, boots):
        print(f"= = = = = = = = = = {self.name} CASTS DRAINS SOUL ON Boots = = = = = = = = = =")
        time.sleep(2)
        total = 0
        for _ in range(4):
            dmg = randint(2, 4)
            boots.hp -= dmg
            total += dmg
            print(f"--- {dmg} DMG ---")
            time.sleep(1)
        self.hp += total
        print(f"{self.name} HEALED FOR {total}HP")

    def throw_sandal(self, boots):
        print(f"= = = = = = = = = = {self.name} PREPARES TO THROW A SANDAL AT YOU = = = = = = = = = =")
        left_or_right = randint(0, 1)
        sandal_direction = "l"
        print_direction = "LEFT"
        if left_or_right == 1:
            sandal_direction = "r"
            print_direction = "RIGHT"

        time.sleep(2)

        while True:
            boots_guess = input("Move left or right? (l/r): ").lower()
            if boots_guess not in ("l", "r"):
                print(f"{self.name}: DUMB ASS")
                continue
            break

        if sandal_direction == boots_guess:
            print(f"==={self.name}: THROWS THE SANDAL TO THE {print_direction}===")
            time.sleep(2)
            print(f"===THE SANDAL SMACKS {boots.name} IN THE FACE===")
            print(f"==={boots.name} TAKES 15 DMG===")
            boots.hp -= 15
            return
        print(f"==={self.name}: THROWS THE SANDAL TO THE {print_direction}===")
        time.sleep(2)
        print(f"==={boots.name} DODGED THAT SHIT LIKE THE MATRIX===")
        time.sleep(2)
        print(f"==={self.name}: DAMN YOU BOOTS===")

    def risky_bet(self, boots):
        coin_flip = randint(0, 1)
        coin = "h"
        print_coin = "HEADS"
        if coin_flip == 1:
            coin = "t"
            print_coin = "TAILS"

        print(f"= = = = = = = = = = {self.name}: CASTS RISKY BET = = = = = = = = = =")
        time.sleep(2)

        while True:
            boots_guess = input("Heads or Tails? (h/t): ").lower()
            if boots_guess not in ("h", "t"):
                print(f"{self.name}: STUPID FUCK")
                continue
            break

        if coin == boots_guess:
            print(f"==={print_coin}===")
            time.sleep(1.5)
            print(f"{self.name}: YOU FUCK")
            time.sleep(1.5)
            print(f"{self.name} TAKES 50 DMG")
            self.hp -= 50
            return
        print(f"==={print_coin}===")
        time.sleep(1.5)
        print(f"{self.name}: OUTPLAYED")
        time.sleep(1.5)
        print(f"{boots.name} TAKES 25 DMG")
        boots.hp -= 25

    def naruto_shit(self, boots):
        print(f"= = = = = = {self.name} DOES SOME NARUTO SHIT AND MAKES 9 CLONES OF HIMSELF = = = = = =")
        time.sleep(2)
        print("1 | 2 | 3")
        print("4 | 5 | 6")
        print("7 | 8 | 9")

        real_flip_flops = str(randint(1, 9))

        while True:
            boots_guess = input("Which one is the real Flip Flops? (1-9): ")
            if boots_guess not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
                continue
            break

        print(f"{boots.name} STARTS CASTING DEATH BOLT")
        time.sleep(2)

        if boots_guess == real_flip_flops:
            print(f"DEATH BOLT HITS FLIP FLOPS")
            self.hp -= 200
            return
        print("DEATH BOLT DESTROYS A CLONE")
        time.sleep(2)
        print(f"{self.name}: MORON, I WAS #{real_flip_flops}")
        time.sleep(3)
        for _ in range(7):
            print("--- CLONE HITS BOOTS FOR 2 DMG ---")
            time.sleep(0.5)
        time.sleep(1)
        print(f"=== {self.name} HITS BOOTS FOR 4 DMG ===")
        boots.hp -= 18

    def backflip_of_doom(self, boots):
        print(f"= = = = = = = = = = {self.name} ATTEMPTS BACKFLIP OF DOOM = = = = = = = = = =")
        time.sleep(2)
        random_chance = randint(0, 10)
        if random_chance == 10:
            print(f"=== {self.name} LANDS ON HIS HEAD ===")
            self.hp -= 200
            return
        print(f"=== {self.name} LANDS THE BACKFLIP ===")
        time.sleep(2)
        print(f"=== SHOCKWAVE DEALS 20 DMG ===")
        boots.hp -= 20
