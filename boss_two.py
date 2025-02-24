import time
from random import randint


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
