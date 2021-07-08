#player_name = input("Enter your name: ")

print("""
Class List:
1. Rogue
2. Knight
3. Ranger
4. Mage
5. Palidan
6. Priest
7. Barbarian""")
print("")
#player_class = input("Choose you class: ")

#attributes are capitalized because str = string in python
Hp = 0
Mp = 0
Dex = 0
Str = 0
Mag = 0
Def = 0
Spr = 0

def ranged_attack(dex, ranged_atk, tgt_def):
    damage = ranged_atk * (dex / 100)
    hit = damage - tgt_def
    if hit > 0:
        return round(hit, 2)
    elif hit <= 0:
        return "miss"
    
def melee_attack(strength, melee_atk, tgt_def):
    damage = melee_atk * (strength / 100)
    hit = damage - tgt_def
    if hit > 0:
        return round(hit, 2)
    else:
        return "miss"

print("this is a branch test")
