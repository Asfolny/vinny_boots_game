import time
from random import randint
from enemies import UndeadNormalEnemy


class Boots:
    def __init__(self):
        self.name = "Boots"
        self.hp = 100
        self.undead_army = []
        self.blood_bomb_timer = 0
        self.summon_skeletons_cd = 0 
        self.summon_gargoyle_cd = 0

    def show_spells(self):
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

    def take_turn(self, enemy):
        self.choose_atk(enemy)
        self.blood_bomb_detonate(enemy)
        self.handle_summon_skeletons(enemy)
        self.handle_summon_gargoyle(enemy)
        

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
            if atk not in ("0", "1", "2", "3", "4", "5", "?"):
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
                case "?":
                    self.show_spells()
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



