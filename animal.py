#Copyright Talon Saylor
#Copyright Animal Farm by George Orwell


import random
import time

# Character class
class Character:
    def __init__(self, name, health, attack, defense, special_move=None, is_named=False):
        self.crit_rate = 0 #inital 0
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_move = special_move
        self.is_named = is_named  # Whether the character is a named enemy or not
        self.experience = 0  # Player's experience
        self.heal_used = False  # Track if healing has been used in battle
        self.level = 1  # Player's level
        self.crit_damage_multiplier = 1.0  # Default crit damage multiplier

    def take_damage(self, damage):
        reduced_damage = max(0, damage - self.defense)
        self.health -= reduced_damage
        return reduced_damage

    def is_alive(self):
        return self.health > 0

    def heal(self):
        if not self.heal_used:
            heal_amount = min(30, 100 - self.health)  # Cap healing to max health
            self.health += heal_amount
            self.heal_used = True
            return heal_amount
        return 0

    def gain_experience(self, amount):
        self.experience += amount
        # Level up when experience reaches 100
        while self.experience >= 100:
            self.experience -= 100
            self.level_up()

    def level_up(self):
        self.health += 10
        self.attack += 5
        self.defense += 2
        self.level += 1
        print(f"\n{self.name} leveled up to level {self.level}! New stats: HP +10, Attack +5, Defense +2.")

    def display_health(self):
        bar = "█" * (self.health // 5)
        print(f"{self.name}: [{bar}] {self.health} HP (Level {self.level})")

    def apply_item(self, item):
        print(f"\n{self.name} found a {item.name}! Applying its effect...")
        item.apply(self)

# Item class to create various item effects
class Item:
    def __init__(self, name, effect_type, effect_value):
        self.name = name
        self.effect_type = effect_type
        self.effect_value = effect_value

    def apply(self, character):
        if self.effect_type == "crit_damage":
            character.crit_damage_multiplier += self.effect_value
            print(f"{character.name}'s Critical Damage increased by {self.effect_value * 100}%!")
        elif self.effect_type == "crit_rate":
            character.crit_rate += self.effect_value  # Boost attack as a form of crit rate for simplicity
            print(f"{character.name}'s Crit Rate increased by {self.effect_value}!")
        elif self.effect_type == "attack_boost":
            character.attack += self.effect_value
            print(f"{character.name}'s Attack increased by {self.effect_value}!")
        elif self.effect_type == "defense_boost":
            character.defense += self.effect_value
            print(f"{character.name}'s Defense increased by {self.effect_value}!")
        elif self.effect_type == "heal":
            character.health += self.effect_value
            character.health = min(character.health, 100)  # Cap at 100 HP
            print(f"{character.name} healed for {self.effect_value} HP!")

# Define some example items with additional effects

item_pool = [
    Item("Critical Power Potion", "crit_damage", .2),  # +20% Crit Damage
    Item("Attack Boosting Amulet", "attack_boost", 3),  # +2 Attack
    Item("Lucky Charm", "crit_rate", 3),  # +3 crit (represents crit rate increase)
    Item("Berserker Stone", "crit_damage", .20),  # +20 Attack for Crit 
    Item("Healing Elixir", "heal", 30),  # Heal 30 HP
    Item("Damage Booster", "attack_boost", 7),  # +7 Attack
    Item("Swift Boots", "crit_rate", 5),  # +5 Crit (represents crit rate increase)
    Item("Strength Ring", "attack_boost", 4),  # +4 Attack
    Item("Powerful Elixir", "crit_damage", 0.15),  # +15% Crit Damage
    Item("Shield of Protection", "defense_boost", 3),  # +3 Defense
    Item("Magic Feather", "attack_boost", 2),  # 2 Attack
    Item("Mana Potion", "crit_damage", 0.1),  # +10% Crit Damage
    Item("Phoenix Feather", "heal", 50),  # Heal 50 HP
    Item("Strength Potion", "crit_damage", .1),  # +10 critdamage
    Item("Combant Manual", "crit_rate", 15),  # +15 crit (represents crit rate increase)
]
# Define the player character
player = Character(name="Napoleon", health=100, attack=15, defense=5, special_move="Revolutionary Command", is_named=True)

# Basic enemies (weaker than named enemies)
basic_enemies = [
    Character("Rabbit", health=70 + player.level * 2, attack=10+ player.level, defense=2+player.level-2),
    Character("Goat", health=80  + player.level * 2, attack=12+player.level, defense=3+player.level-2),
    Character("Chicken", health=45  + player.level * 2, attack=8+player.level, defense=1+player.level-2),
    Character("Cow", health=100  + player.level * 2, attack=7+player.level, defense=6+player.level-2),  
    Character("Duck", health=65  + player.level * 2, attack=9+player.level, defense=1+player.level-2),     
    Character("Turkey", health=70  + player.level * 2, attack=14+player.level, defense=4+player.level-2),  
]

# Enemy Characters from Animal Farm with special moves
named_enemies = [
    Character("Snowball the Pig", health=200+ player.level * 2, attack=26+player.level, defense=7+player.level-2, special_move="Revolutionary Charge", is_named=True),
    Character("Boxer the Horse", health=200  + player.level * 2, attack=25+player.level, defense=13+player.level-2, special_move="Mighty Kick", is_named=True),
    Character("Benjamin the Donkey", health=300+ player.level * 2, attack=14+player.level, defense=10+player.level-2, special_move="Cynical Stare", is_named=True),
    Character("Squealer the Pig", health=110  + player.level * 2, attack=15+player.level, defense=2+player.level-2, special_move="Propaganda Speech", is_named=True),
    Character("The Sheeps", health=130  + player.level * 2, attack=12+player.level, defense=3+player.level-2, special_move="Chanting Frenzy", is_named=True),
    Character("Old Major's Ghost", health=120  + player.level * 2, attack=20+player.level, defense=4+player.level-2, special_move="Spirit of Revolution", is_named=True),
    Character("Moses the Raven", health=20 + player.level * 2, attack=45+player.level, defense=12+player.level-2, special_move="Cloud of Lies", is_named=True),  
    Character("Clover the Horse", health=95 + player.level * 2, attack=18+player.level, defense=12+player.level-2, special_move="Moral Support", is_named=True),  
    Character("Napoleon's Hound", health=190 + player.level * 2, attack=23+player.level, defense=8+player.level-2, special_move="Bite", is_named=True),  
    Character("Femboy", health=120+player.level*2, attack=23+player.level, defense=3+player.level-2, special_move="Rile", is_named=True),  
]
#HE DONT EXIST IN ANIMAL FARM JUST THOUGHT IT WAS FUNN 
Snappy = Character("Snappy the Snapping Turtle", health=1 + player.level * 100, attack=999, defense=999) 

# Function to handle random attack damage
def random_attack_damage(base_attack):
    return random.randint(base_attack - 5, base_attack + 5)

def battle(player, enemy):
    EnemyLoop=0
    loop=0
    print(f"\nNapoleon encounters {enemy.name}!\n")
    time.sleep(1)

    # Reset healing ability for new battle
    player.heal_used = False

    # Clone the enemy so its health resets after battle (for basic enemies)
    if not enemy.is_named:
        enemy = Character(enemy.name, enemy.health, enemy.attack, enemy.defense)

    while player.is_alive() and enemy.is_alive():
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Defend")
        print("3. Special Move (50% chance to deal double damage)")
        print("4. Heal (Once per battle, restores 30 HP)")

        choice = input("Choose an action: ")

        if choice == "1":
            damage = int(random_attack_damage(player.attack) * player.crit_damage_multiplier)
            dealt = enemy.take_damage(damage)
            print(f"\nYou attacked {enemy.name} and dealt {dealt} damage!")
        elif choice == "2":
            player.defense += 5
            print("\nYou brace yourself! Defense increased temporarily.")
            loop=1
        elif choice == "3":
            critchance = random.randint(1,100)
            if critchance+player.crit_rate > 50:
                damage = int(random_attack_damage(player.attack) * 2 * player.crit_damage_multiplier)
                dealt = enemy.take_damage(damage)
                print(f"\nCritical hit! You dealt {dealt} damage!")
            else:
                print("\nYou missed your special move!")
        elif choice == "4":
            heal_amount = player.heal()
            if heal_amount > 0:
                print(f"\nYou healed for {heal_amount} HP!")
            else:
                print("\nYou have already used healing in this battle!")
        else:
            print("\nInvalid choice! You lose your turn.")

        time.sleep(1)
        
        if EnemyLoop==1:
            enemy.defense-=5
            
        if enemy.is_alive() and enemy.is_named==True:
            print(f"\n--- {enemy.name}'s Turn ---")
            enemy_action = random.choice(["attack", "special", "attack","defend"])  # Increased chance for attack
            
        elif enemy.is_alive() and enemy.is_named==False:
            print(f"\n--- {enemy.name}'s Turn ---")
            enemy_action = random.choice(["attack","defend","attack"]) 


            if enemy_action == "attack":
                damage = random_attack_damage(enemy.attack)
                dealt = player.take_damage(damage)
                print(f"\n{enemy.name} attacked you and dealt {dealt} damage!")
            elif enemy_action == "special" and enemy.special_move:
                print(f"\n{enemy.name} uses its special move: {enemy.special_move}")
                player.take_damage(random_attack_damage(enemy.attack) * 2)
            elif enemy_action == "defend":
                print(f"\n{enemy.name} defends increases defense for your next attack")
                enemy.defense+=5
                EnemyLoop=1

            time.sleep(1)

        # Display health
        print(f"\nCurrent XP: {player.experience}")
        print("Current Health:")
        player.display_health()
        enemy.display_health()
        if loop==1:
            player.defense-=5

    # Battle result
    if player.is_alive():
        print(f"\nYou defeated {enemy.name}!")
        if enemy.is_named:
            player.gain_experience(100)  # Named enemies give more XP
        else:
            player.gain_experience(random.randint(20,40))  # Basic enemies give less XP

        # After the battle, the player has a chance to find an item
        if random.random() < .5:  # 50% chance to find an item
        
            found_item = random.choice(item_pool)
            player.apply_item(found_item)

    else:
        print(f"\nYou have been defeated by {enemy.name}... Game Over!")
        exit()


def main():
    print("Welcome to Napoleon's Battle Against Animal Farm!")
    time.sleep(1)


    # Track which named enemies have been defeated
    defeated_named_enemies = set()

    while True:
        # Randomly choose an enemy (named or basic)
        if random.random() < 1/5:  # 20% chance for a named enemy
            snap = random.randint(1,100)
            if snap==1:
                enemy = Snappy
            else:
                possible_named_enemies = [enemy for enemy in named_enemies if enemy.name not in defeated_named_enemies]
                if possible_named_enemies:
                 enemy = random.choice(possible_named_enemies)
                else:
                    enemy = random.choice(basic_enemies)  # Fall back to basic enemiesr
        else:
            enemy = random.choice(basic_enemies)

        battle(player, enemy)

        if enemy.is_named:
            defeated_named_enemies.add(enemy.name)

        # Ensure all named enemies are defeated before ending the game
        if len(defeated_named_enemies) == len(named_enemies):
            print("\nAll named enemies have been defeated! You have conquered Animal Farm!")
            break

        print("\nYou march to the next battle...\n")
        time.sleep(2)

    if player.is_alive():
        print("\nCongratulations! You have conquered Animal Farm!")

# Start the game
if __name__ == "__main__":
    main()