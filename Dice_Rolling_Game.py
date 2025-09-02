
import random

# Dice roll karne ka function
def roll_dice():
    return random.randint(1, 6)

print("🎲 Dice Rolling Game - Jo sabse pehle 12 score karega wahi jeetega! 🎲")

score = 0
target_score = 12

while True:
    player = input("Roll dice? (y/n): ").lower()   # Har baar input poochega
    
    if player == "y":
        roll = roll_dice()           # Ek hi baar random number aayega
        score += roll                # Score mein add hoga
        print(f"Aapne {roll} roll kiya. Total score: {score}")
        
        # Agar score target se zyada ho jaye
        if score >= target_score:
            print("🏆 Aap jeet gaye!")
            break
    
    elif player == "n":
        print("Game stop kar diya gaya!")
        break
    
    else:
        print("Sirf y ya n likhiye!")




# import random

# def roll_dice():
#     return random.randint(1, 6)

# print("🎲 Dice Rolling Game - First to reach 12 wins! 🎲")

# player = input("Enter y/n: ").lower()

# score= 0
# target_score = 12

# while True:
#     if player == "y":
#         roll = roll_dice() 
#         score += roll
#         print(f"You rolled {roll}. Total score: {score}")
        
#         if score >= target_score:
#             print("You win")
#             break
#     else:
#         print("Game stopped!")
#         break