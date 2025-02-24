import time

from boss_one import BossOne
from boss_two import BossTwo
from final_boss import FinalBoss
from enemies import *


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

    level1 = []
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
            quit()

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
