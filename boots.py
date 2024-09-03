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


class BossTwo:
    def __init__(self):
        self.name = "Unethical Dan"
        self.dans_zils_gems = 50
        self.boots_zils_gems = 50
        self.atk_quotes = ["I'm rewriting boot dev's front end in React",
                           "I shall rule boot dev",
                           "Your luck is running out",
                           "You'll make a nice rug",
                           "I'll show you who's top dog, you filthy canine",
                           "I've got a bone to pick with you . . . no don't chew on it"]
        self.boots_shit_talk = ["So it's gonna be slow as fuck?",
                                "C# shall not pass",
                                "Good thing I've never relied on it",
                                "You'll make a nice meal",
                                "Byte me, human",
                                "I'm going to strangle you with my bear hands"]
        self.death_quote = "Damn you bearman, I was going to replace you with a parrot\n*** DAN DIES ***"
        print(f"{self.name}: WELCOME TO THE UNDERBELLY")
        time.sleep(3)
        print(f"{self.name}: So you've come to retrieve Zil's gems huh?")
        time.sleep(3)
        print(f"{self.name}: Tell you what, I'll give you half, gamble for the rest")
        time.sleep(3)
        print(f"{self.name}: You lose, you die")

    def check_death(self):
        if self.dans_zils_gems <= 0:
            return True
        return False

    def check_boots_death(self):
        if self.boots_zils_gems <= 0:
            print(f"{self.name} CASTS UNDEAD BIRD SWARM ON BOOTS")
            time.sleep(3)
            return True
        return False

    def choose_random_atk(self, boots):
        rand_num = randint(0, len(self.atk_quotes)-1)
        print(f"{self.name}: {self.atk_quotes[rand_num]}")
        time.sleep(2.5)
        print(f"Boots: {self.boots_shit_talk[rand_num]}")
        time.sleep(3)
        rand_atk = randint(0, 4)
        match rand_atk:
            case 0:
                self.slots()  # 11.11% CHANCE OF WINNING
            case 1:
                self.heads_or_tails()  # 50% CHANCE OF WINNING
            case 2:
                self.wheres_js()  # 66% CHANCE OF WINNING
            case 3:
                self.rock_paper_scissors()  # 33% CHANCE OF WINNING
            case 4:
                self.word_scrambler()  # SKILL BASED

    def bet_gems(self):
        lowest_bet = 5
        highest_bet = self.boots_zils_gems
        bet = 0

        while True:
            bet = int(input(f"PLACE BET - Lowest({lowest_bet})  Highest({highest_bet}) - must be multiples of 5: "))
            if bet not in [x for x in range(lowest_bet, highest_bet+1) if x % 5 == 0]:
                continue
            if bet == highest_bet:
                print(f"{self.name}: Oh, you intend on betting your life on a single game? Very bold, bearman")
                time.sleep(2)
            break

        return bet

    def slots(self):
        print("--- SLOTS ---")
        time.sleep(2)
        bet = self.bet_gems()

        while True:
            pull = input("Press enter to pull lever: ")
            if not pull:
                break
            continue

        nums1 = [randint(1, 3) for _ in range(7)]
        nums2 = [randint(1, 3) for _ in range(7)]
        nums3 = [randint(1, 3) for _ in range(7)]

        final_num1 = 0
        final_num2 = 0
        final_num3 = 0

        for num in nums1:
            ran = randint(1, 3)
            ran2 = randint(1, 3)
            print("\n" * 35)
            final_num1 = num
            print(f"{num} | {ran} | {ran2}")
            time.sleep(0.2)

        for num in nums2:
            ran = randint(1, 3)
            print("\n" * 35)
            final_num2 = num
            print(f"{final_num1} | {num} | {ran}")
            time.sleep(0.2)

        for num in nums3:
            print("\n" * 35)
            final_num3 = num
            print(f"{final_num1} | {final_num2} | {final_num3}")
            time.sleep(0.2)

        if final_num1 == final_num2 and final_num2 == final_num3:
            print("*** WINNER ***")
            time.sleep(2)
            print(f"{self.name}: Lucky bastard")
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
            return
        print("--- LOSER ---")
        time.sleep(2)
        print(f"{self.name}: Damn you suck")
        self.boots_zils_gems -= bet
        self.dans_zils_gems += bet

    def heads_or_tails(self):
        print("--- HEADS OR TAILS ---")
        time.sleep(2)
        bet = self.bet_gems()

        flip_result = "h"
        flip = randint(0, 1)
        if flip == 1:
            flip_result = "t"

        while True:
            ht = input("Heads or tails? (h/t): ").lower()
            if ht not in ["h", "t"]:
                continue
            break

        time.sleep(1)

        if flip_result == "h":
            print("--- HEADS ---")
        else:
            print("--- TAILS ---")

        time.sleep(1.5)

        if flip_result == ht:
            print("*** YOU WIN ***")
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
            return
        print("--- YOU LOSE ---")
        self.boots_zils_gems -= bet
        self.dans_zils_gems += bet

    def wheres_js(self):
        print("--- WHERE'S JAVASCRIPT? ---")
        time.sleep(2)
        bet = self.bet_gems()

        languages = ["js", "js", "go"]

        left_rand = randint(0, len(languages)-1)
        left = languages[left_rand]
        languages.pop(left_rand)

        mid_rand = randint(0, len(languages)-1)
        mid = languages[mid_rand]
        languages.pop(mid_rand)

        right_rand = randint(0, len(languages)-1)
        right = languages[right_rand]
        languages.pop(right_rand)

        print(" ___   ___   ___")
        print("|   | |   | |   |")
        print("| 1 | | 2 | | 3 |")
        print("|___| |___| |___|")
        time.sleep(2)

        while True:
            door = input("Which door contains javascript? ")
            if door not in ["1", "2", "3"]:
                continue
            break

        if door == "1" and left == "js":
            print(f"{left}")
            time.sleep(1.5)
            print("*** WINNER ***")
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
        elif door == "1" and left != "js":
            print(f"{left}")
            time.sleep(1.5)
            print("--- LOSER ---")
            self.boots_zils_gems -= bet
            self.dans_zils_gems += bet
        elif door == "2" and mid == "js":
            print(f"{mid}")
            time.sleep(1.5)
            print("*** WINNER ***")
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
        elif door == "2" and mid != "js":
            print(f"{mid}")
            time.sleep(1.5)
            print("--- LOSER ---")
            self.boots_zils_gems -= bet
            self.dans_zils_gems += bet
        elif door == "3" and right == "js":
            print(f"{right}")
            time.sleep(1.5)
            print("*** WINNER ***")
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
        elif door == "3" and right != "js":
            print(f"{right}")
            time.sleep(1.5)
            print("--- LOSER ---")
            self.boots_zils_gems -= bet
            self.dans_zils_gems += bet
        time.sleep(1.5)

    def rock_paper_scissors(self):
        print("--- ROCK/PAPER/SCISSORS ---")
        time.sleep(2)

        bet = self.bet_gems()

        while True:
            while True:
                rps = input("r/p/s: ").lower()
                while rps not in ["r", "p", "s"]:
                    continue
                break

            dan_move = randint(0, 2)
            dan_move_print = ""
            if dan_move == 0:
                dan_move_print = "ROCK"
            elif dan_move == 1:
                dan_move_print = "PAPER"
            else:
                dan_move_print = "SCISSORS"

            if dan_move == 0 and rps == "r":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---DRAW---")
                time.sleep(1.5)
                print(f"{self.name}: You read my mind bearman, AGAIN")
                time.sleep(2.5)
                continue
            if dan_move == 1 and rps == "p":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---DRAW---")
                time.sleep(1.5)
                print(f"{self.name}: You read my mind bearman, AGAIN")
                time.sleep(2.5)
                continue
            if dan_move == 2 and rps == "s":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---DRAW---")
                time.sleep(1.5)
                print(f"{self.name}: You read my mind bearman, AGAIN")
                time.sleep(2.5)
                continue

            if dan_move == 0 and rps == "p":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU WIN---")
                time.sleep(1.5)
                print(f"{self.name}: Lucky dog")
                self.boots_zils_gems += bet
                self.dans_zils_gems -= bet
                time.sleep(1.5)
                break
            if dan_move == 1 and rps == "s":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU WIN---")
                time.sleep(1.5)
                print(f"{self.name}: Lucky dog")
                self.boots_zils_gems += bet
                self.dans_zils_gems -= bet
                time.sleep(1.5)
                break
            if dan_move == 2 and rps == "r":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU WIN---")
                time.sleep(1.5)
                print(f"{self.name}: Lucky dog")
                self.boots_zils_gems += bet
                self.dans_zils_gems -= bet
                time.sleep(1.5)
                break

            if dan_move == 0 and rps == "s":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU LOSE---")
                time.sleep(1.5)
                print(f"{self.name}: All skill")
                self.dans_zils_gems += bet
                self.boots_zils_gems -= bet
                time.sleep(1.5)
                break
            if dan_move == 1 and rps == "r":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU LOSE---")
                time.sleep(1.5)
                print(f"{self.name}: All skill")
                self.dans_zils_gems += bet
                self.boots_zils_gems -= bet
                time.sleep(1.5)
                break
            if dan_move == 2 and rps == "p":
                print(f"{self.name} CHOOSES {dan_move_print}")
                time.sleep(1.5)
                print("---YOU LOSE---")
                time.sleep(1.5)
                print(f"{self.name}: All skill")
                self.dans_zils_gems += bet
                self.boots_zils_gems -= bet
                time.sleep(1.5)
                break

    def word_scrambler(self):
        print("--- WORD SCRAMBLER ---")
        time.sleep(2)
        bet = self.bet_gems()
        words = ["boots", "necromancer", "wizard", "javascript", "spell", "wand"]
        index = randint(0, len(words)-1)
        word = scramble(words[index])
        guess = input(f"{self.name}: Unscramble this word: {word} ").lower()

        if words[index] == guess:
            print("--- CORRECT ---")
            time.sleep(1.5)
            print(f"{self.name}: Damn skill-based games")
            time.sleep(1.5)
            self.boots_zils_gems += bet
            self.dans_zils_gems -= bet
            return
        print("--- WRONG ---")
        time.sleep(1.5)
        print(f"{self.name}: I knew you wouldn't get that shit")
        time.sleep(1.5)
        self.dans_zils_gems += bet
        self.boots_zils_gems -= bet


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
        print(f"==={self.name}: THROWS THE SANDAL TO THE {sandal_direction}===")
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


class NormalEnemy:
    def __init__(self):
        self.names = ["Goblin", "Devilish Imp", "Evil Gnome", "Werewolf", "Ogre", "Bear Assassin"]
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


class Boots:
    def __init__(self):
        self.name = "Boots"
        self.hp = 100
        self.undead_army = []
        self.blood_bomb_timer = 0
        self.summon_skeletons_cd = 0
        self.summon_gargoyle_cd = 0

    def check_death(self):
        if self.hp <= 0:
            print("BOOTS HAS DIED, NOOOOOOOOOOOOOOOO")
            time.sleep(2)
            return True
        return False

    def add_to_undead_army(self, enemy):
        print(f"{enemy.name} added to Boots' undead army")
        self.undead_army.append(UndeadNormalEnemy(enemy.name))
        time.sleep(1.5)
        print(self.undead_army[-1].quote)

    def choose_atk(self, enemy):
        blood_bomb_not_ready = ""
        if self.blood_bomb_timer != 0:
            blood_bomb_not_ready = "(NOT READY)"
        summon_skeletons_not_ready = ""
        if self.summon_skeletons_cd != 0:
            summon_skeletons_not_ready = "(NOT READY)"
        summon_gargoyle_not_ready = ""
        if self.summon_gargoyle_cd != 0:
            summon_gargoyle_not_ready = "(NOT READY)"
        no_undeads_to_sacrifice = ""
        if len(self.undead_army) == 0:
            no_undeads_to_sacrifice = "(NO UNDEADS)"
        no_minions_at_all = ""
        if len(self.undead_army) == 0 and self.summon_skeletons_cd == 0 and self.summon_gargoyle_cd == 0:
            no_minions_at_all = "(NO MINIONS)"

        while True:
            atk = input(f"0: Shadow Bolt  "
                        f"1: Blood Bomb{blood_bomb_not_ready}  \n"
                        f"2: Summon Skeletons{summon_skeletons_not_ready}  "
                        f"3: Summon Gargoyle{summon_gargoyle_not_ready}  \n"
                        f"4: Sacrifice Undead{no_undeads_to_sacrifice}  "
                        f"5: Army Nuke{no_minions_at_all}\n"
                        f"---------------------------------------------------------\n"
                        f"| Boots HP: {self.hp} |                 | Undead Army Count {len(self.undead_army)} | \n"
                        f"Cast Spell: ")
            if atk not in ("0", "1", "2", "3", "4", "5"):
                continue
            match atk:
                case "0":
                    self.shadow_bolt(enemy)
                    break
                case "1":
                    if self.blood_bomb_timer == 0:
                        self.blood_bomb()
                        break
                    continue
                case "2":
                    if self.summon_skeletons_cd == 0:
                        self.summon_skeletons(enemy)
                        break
                    continue
                case "3":
                    if self.summon_gargoyle_cd == 0:
                        self.summon_gargoyle()
                        break
                    continue
                case "4":
                    if len(self.undead_army) > 0:
                        self.sacrifice_undead()
                        break
                    continue
                case "5":
                    if len(self.undead_army) > 0 or self.summon_skeletons_cd != 0 or self.summon_gargoyle_cd != 0:
                        self.army_nuke(enemy)
                        break
                    continue

    def shadow_bolt(self, enemy):
        crit = randint(0, 3)
        if crit == 0:
            print("--- CRIT ---")
            time.sleep(1.5)
            print(f"{self.name} SHADOW BOLTS {enemy.name} FOR 30 DMG")
            enemy.hp -= 30
            return
        print(f"{self.name} SHADOW BOLTS {enemy.name} FOR 15 DMG")
        enemy.hp -= 15

    def blood_bomb(self):
        if self.blood_bomb_timer == 0:
            self.blood_bomb_timer = 3
            print("Boots casts blood bomb, in 2 turns it will explode!")
            time.sleep(1.5)

    def blood_bomb_detonate(self, enemy):
        if self.blood_bomb_timer > 0:
            self.blood_bomb_timer -= 1
            if self.blood_bomb_timer == 0:
                dmg = 10 + 5 * len(self.undead_army)
                if self.summon_skeletons_cd != 0:
                    dmg += 10
                if self.summon_gargoyle_cd != 0:
                    dmg += 5
                print(f"--- BLOOD BOMB EXPLODES FOR {dmg} DMG ---")
                time.sleep(2)
                enemy.hp -= dmg

    def summon_skeletons(self, enemy):
        if self.summon_skeletons_cd == 0:
            self.summon_skeletons_cd = 4
            print("Boots summons 2 skeletons and does 20 DMG!")
            enemy.hp -= 20
            time.sleep(1.5)

    def handle_summon_skeletons(self, enemy):
        if 0 < self.summon_skeletons_cd < 4:
            print(f"1ST SKELETON STABS {enemy.name} FOR 10 DMG")
            time.sleep(0.7)
            print(f"2ND SKELETON STABS {enemy.name} FOR 10 DMG")
            time.sleep(2)
            enemy.hp -= 20
        if self.summon_skeletons_cd > 0:
            self.summon_skeletons_cd -= 1

    def summon_gargoyle(self):
        if self.summon_gargoyle_cd == 0:
            self.summon_gargoyle_cd = 5
            print("Boots summons a gargoyle for 5 turns!")
            time.sleep(1.5)

    def handle_summon_gargoyle(self, enemy):
        if self.summon_gargoyle_cd == 5:
            print(f"GARGOYLE BITES {enemy.name} FOR 25 DMG")
            time.sleep(1.5)
            print("GARGOYLE HEALS BOOTS FOR 20HP")
            time.sleep(2)
            enemy.hp -= 25
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
        if self.summon_gargoyle_cd == 3:
            print(f"GARGOYLE BITES {enemy.name} FOR 25 DMG")
            time.sleep(1.5)
            print("GARGOYLE HEALS BOOTS FOR 20HP")
            time.sleep(2)
            enemy.hp -= 25
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
        if self.summon_gargoyle_cd == 1:
            print(f"GARGOYLE BITES {enemy.name} FOR 25 DMG")
            time.sleep(1.5)
            print("GARGOYLE HEALS BOOTS FOR 20HP")
            time.sleep(2)
            enemy.hp -= 25
            self.hp += 20
            if self.hp > 100:
                self.hp = 100
        if self.summon_gargoyle_cd > 0:
            self.summon_gargoyle_cd -= 1

    def sacrifice_undead(self):
        self.undead_army.pop()
        print("BOOTS SACRIFICES AN UNDEAD AND HEALS FOR 40HP")
        self.hp += 40
        if self.hp > 100:
            self.hp = 100
        time.sleep(2)

    def army_nuke(self, enemy):
        dmg = 25 * len(self.undead_army)
        if self.summon_gargoyle_cd != 0:
            dmg += 25
        if self.summon_skeletons_cd != 0:
            dmg += 50
        print(f"{self.name} SACRIFICES ALL MINIONS")
        time.sleep(1.5)
        for i in range(5, 0, -1):
            print(i)
            time.sleep(1)
        print(f"=== === | {enemy.name} TAKES {dmg} DMG | === ===")
        enemy.hp -= dmg
        self.summon_skeletons_cd = 0
        self.summon_gargoyle_cd = 0
        for i in range(len(self.undead_army)):
            self.undead_army.pop()


def scramble(word):
    new_word = ""
    used_indexes = []

    while True:
        while len(word) != len(new_word):
            index = randint(0, len(word) - 1)

            if index not in used_indexes:
                new_word += word[index]
                used_indexes.append(index)

        hits = 0

        for i in range(len(word)):
            if word[i] == new_word[i]:
                hits += 1

        if hits >= 3:
            new_word = ""
            used_indexes = []
            continue

        break

    return new_word


def spawn_normal_enemies(arr, count):
    for i in range(count):
        arr.append(NormalEnemy())
        time.sleep(1)


def show_enemy_hp(enemy):
    width = len(enemy.name) + 7
    print(f"-" * width)
    print(f"{enemy.name}: {enemy.hp}HP")
    print("-" * width)


def main():
    b = Boots()

    print("================================================ TUTORIAL ================================================")
    while True:
        print("You play as Boots the Necromancer in this game. Killing normal enemies adds minions to Boots' undead army.")
        print("These minions can be sacrificed for HP and they can also increase the damage of other spells per minion.")
        print("Enter number assigned to spells to play this turn-based game.")
        print("=============================================== SPELL GUIDE ===============================================")
        print("0. Shadow Bolt")
        print(" - Does 15 DMG, has a 25% chance to crit for 30 DMG.")
        print("1. Blood Bomb")
        print(" - Explodes in 2 turns for 10 DMG + 5 DMG per undead minion + skeletons and gargoyle.")
        print("2. Summon Skeletons")
        print(" - Does 20 DMG and summons two skeletons for the next 3 turns, skeletons deal 10 DMG each per turn.")
        print("3. Summon Gargoyle")
        print(" - Summons Gargoyle that lasts for 5 turns, does 25 DMG and heals Boots for 20HP every 2 turns.")
        print("4. Sacrifice Undead")
        print(" - Sacrifices one minion from undead army and heals Boots for 40HP.")
        print("5. Army Nuke")
        print(" - Sacrifices all undead minions, skeletons, and gargoyle to nuke the enemy for 25 DMG per minion.")
        while True:
            yn = input('Type "y" to play  ').lower()
            if yn != "y":
                continue
            break
        break

    """level1 = []
    print("---LEVEL 1---")
    time.sleep(1.5)
    spawn_normal_enemies(level1, 4)
    while len(level1) != 0:
        time.sleep(1)
        show_enemy_hp(level1[0])
        time.sleep(1.5)

        b.choose_atk(level1[0])
        b.blood_bomb_detonate(level1[0])
        b.handle_summon_skeletons(level1[0])
        b.handle_summon_gargoyle(level1[0])

        if level1[0].check_death() is True:
            b.add_to_undead_army(level1[0])
            level1.pop(0)
            time.sleep(1.5)
            continue
        time.sleep(1.5)
        level1[0].normal_atk(b)
        time.sleep(1.5)
        if b.check_death() is True:
            quit()

    print("=========================================== | BOSS BATTLE | ===========================================")
    time.sleep(2)
    boss1 = BossOne()
    time.sleep(3)
    while boss1.hp > 0:
        show_enemy_hp(boss1)
        time.sleep(3)

        b.choose_atk(boss1)
        b.blood_bomb_detonate(boss1)
        b.handle_summon_skeletons(boss1)
        b.handle_summon_gargoyle(boss1)

        if boss1.check_death() is True:
            print(boss1.death_quote)
            time.sleep(5)
            break
        time.sleep(2)
        boss1.choose_random_atk(b)
        time.sleep(1.5)
        if boss1.check_death() is True:
            print(boss1.death_quote)
            time.sleep(5)
            break
        if b.check_death() is True:
            quit()

    print("===LEVEL 1 COMPLETE!===")
    time.sleep(3.5)

    level2 = []
    print("---LEVEL 2---")
    time.sleep(1.5)
    spawn_normal_enemies(level2, 5)
    while len(level2) != 0:
        time.sleep(1)
        show_enemy_hp(level2[0])
        time.sleep(1.5)

        b.choose_atk(level2[0])
        b.blood_bomb_detonate(level2[0])
        b.handle_summon_skeletons(level2[0])
        b.handle_summon_gargoyle(level2[0])

        if level2[0].check_death() is True:
            b.add_to_undead_army(level2[0])
            level2.pop(0)
            time.sleep(1.5)
            continue
        time.sleep(1.5)
        level2[0].normal_atk(b)
        time.sleep(1.5)
        if b.check_death() is True:
            quit()

    print("=========================================== | BOSS BATTLE | ===========================================")
    time.sleep(2)
    boss2 = BossTwo()
    time.sleep(3)
    while boss2.dans_zils_gems > 0:
        print("-" * 15)
        print(f"Dans Gems: {boss2.dans_zils_gems}")
        print(f"Boots Gems: {boss2.boots_zils_gems}")
        print("-" * 15)

        time.sleep(2)
        boss2.choose_random_atk(b)

        if boss2.check_death() is True:
            print(boss2.death_quote)
            time.sleep(5)
            break
        if boss2.check_boots_death() is True:
            b.hp -= 100
            b.check_death()
            quit()

    print("Grandmaster Lane: I knew I shouldn't have trusted that guy . . .")
    time.sleep(4)

    print("===LEVEL 2 COMPLETE!===")
    time.sleep(2)

    level3 = []
    print("---LEVEL 3---")
    time.sleep(1.5)
    spawn_normal_enemies(level3, 6)
    while len(level3) != 0:
        time.sleep(1)
        show_enemy_hp(level3[0])
        time.sleep(1.5)

        b.choose_atk(level3[0])
        b.blood_bomb_detonate(level3[0])
        b.handle_summon_skeletons(level3[0])
        b.handle_summon_gargoyle(level3[0])

        if level3[0].check_death() is True:
            b.add_to_undead_army(level3[0])
            level3.pop(0)
            time.sleep(1.5)
            continue
        time.sleep(1.5)
        level3[0].normal_atk(b)
        time.sleep(1.5)
        if b.check_death() is True:
            quit()"""

    print("=========================================== | BOSS BATTLE | ===========================================")
    time.sleep(2)
    boss3 = FinalBoss()
    time.sleep(3)
    while boss3.hp > 0:
        show_enemy_hp(boss3)
        time.sleep(3)

        b.choose_atk(boss3)
        b.blood_bomb_detonate(boss3)
        b.handle_summon_skeletons(boss3)
        b.handle_summon_gargoyle(boss3)

        time.sleep(2)
        boss3.atk(b)
        time.sleep(1.5)
        if b.check_death() is True:
            print("Grandmaster Lane: Is it done?")
            time.sleep(2)
            print(f"{boss3.name}: Ya it's done")
            time.sleep(3)
            print("=== GAME OVER ===")


if __name__ == "__main__":
    main()
