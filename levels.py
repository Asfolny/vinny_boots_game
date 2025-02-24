import time
from boss_one import BossOne
from boss_two import BossTwo
from final_boss import FinalBoss
from enemies import NormalEnemy

boss_battle = "=========================================== | BOSS BATTLE | ==========================================="
tutorial = "================================================ TUTORIAL ================================================"

short = 1.5
mid = 2
long = 3
longer = 5

def spawn_normal_enemies(count):
    enemies = []
    for _ in range(count):
        enemies.append(NormalEnemy())
    return enemies

def show_enemy_hp(enemy):
    width = len(enemy.name) + 7
    print(f"-" * width)
    print(f"{enemy.name}: {enemy.hp}HP")
    print("-" * width)

 
def level_tutorial(b):
    dev_mode = False
    print(tutorial)
    print("You play as Boots the Necromancer in this game. Killing normal enemies adds minions to Boots' undead army.")
    print("These minions can be sacrificed for HP and they can also increase the damage of other spells per minion.")
    print("Enter number assigned to spells to play this turn-based game.")
    b.show_spells()
    print("You can also type '?' during your turn to see the spell-guide again.")
    print("You can type exit during your turn to quit.")
    while True:
        yn = input('Type "y" to play \n:').lower()
        if yn == "dev": 
            dev_mode = True
            break
        elif yn == "y":
            break
        else: 
            continue
    return dev_mode

def enemy_phase(b, level):
    print(f"---LEVEL {level}---")
    time.sleep(short)
    enemies = spawn_normal_enemies(level + 3)
    while len(enemies) != 0:
        time.sleep(1)
        show_enemy_hp(enemies[0])
        time.sleep(short)
        b.take_turn(enemies[0])
        if enemies[0].check_death() is True:
            b.add_to_undead_army(enemies[0])
            enemies.pop(0)
            time.sleep(short)
            continue
        time.sleep(short)
        enemies[0].normal_atk(b)
        time.sleep(short)
        if b.check_death() is True:
            quit()

def level_two_enemies(b):
    level2 = []
    print("---LEVEL 2---")
    time.sleep(short)
    spawn_normal_enemies(level2, 5)
    while len(level2) != 0:
        time.sleep(1)
        show_enemy_hp(level2[0])
        time.sleep(short)

        b.take_turn(level2[0])

        if level2[0].check_death() is True:
            b.add_to_undead_army(level2[0])
            level2.pop(0)
            time.sleep(short)
            continue
        time.sleep(short)
        level2[0].normal_atk(b)
        time.sleep(short)
        if b.check_death() is True:
            quit()

def level_one_boss(b):
    print(boss_battle)
    time.sleep(mid)
    boss1 = BossOne()
    time.sleep(long)
    while boss1.hp > 0:
        show_enemy_hp(boss1)
        time.sleep(long)

        b.take_turn(boss1)

        if boss1.check_death() is True:
            print(boss1.death_quote)
            time.sleep(longer)
            break
        time.sleep(mid)
        boss1.choose_random_atk(b)
        time.sleep(short)
        if boss1.check_death() is True:
            print(boss1.death_quote)
            time.sleep(longer)
            break

        if b.check_death() is True:
            quit()
        
def level_two_boss(b):

    print(boss_battle)
    time.sleep(mid)
    boss2 = BossTwo()
    time.sleep(long)
    while boss2.dans_zils_gems > 0:
        print("-" * 15)
        print(f"Dans Gems: {boss2.dans_zils_gems}")
        print(f"Boots Gems: {boss2.boots_zils_gems}")
        print("-" * 15)

        time.sleep(mid)
        boss2.choose_random_atk(b)

        if boss2.check_death() is True:
            print(boss2.death_quote)
            time.sleep(longer)
            break
        if boss2.check_boots_death() is True:
            b.hp -= 100
            b.check_death()
            quit()

def level_three_boss(b):
    print(boss_battle)
    time.sleep(mid)
    boss3 = FinalBoss()
    time.sleep(long)
    while boss3.hp > 0:
        show_enemy_hp(boss3)
        time.sleep(long)

        b.take_turn(boss3)

        time.sleep(mid)
        boss3.atk(b)
        time.sleep(short)
        if b.check_death() is True:
            print("Grandmaster Lane: Is it done?")
            time.sleep(mid)
            print(f"{boss3.name}: Ya it's done")
            time.sleep(long)
            print("=== GAME OVER ===")
            quit()

def level_one(b):    
    enemy_phase(b, 1)
    print("Grandmaster Lane: I think I see a boss up ahead.")
    print("Grandmaster Lane: I think we should be careful.")
    level_one_boss(b)
    print("===LEVEL 1 COMPLETE!===")
    time.sleep(3.5)

def level_two(b):
    
    enemy_phase(b, 2)
    level_two_boss(b)

    print("Grandmaster Lane: I knew I shouldn't have trusted that guy . . .")
    time.sleep(4)

    print("===LEVEL 2 COMPLETE!===")
    time.sleep(mid)

def level_three(b):
    print("Grandmaster Lane: I think I see the final boss up ahead.")
    print("Grandmaster Lane: This is it, Boots. The final battle.")
    print("Grandmaster Lane: We can do this.")
    time.sleep(long)
    enemy_phase(b, 3)
    level_three_boss(b)