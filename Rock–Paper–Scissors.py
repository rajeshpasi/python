import random

emojis = {
    "r": "🪨",
    "p": "📄",
    "s": "✂️"
}  #Dictionary = ek aisa data type jisme data key : value pairs ke form me store hota hai.
choices = ('r','p','s') #🔹 Tuple ek data type hai jo list jaisa hota hai, बस fark ये है:  : List [] me banti hai aur change (mutable) hoti है. : Tuple () me banta hai aur change nahi hota (immutable).
while True:
    user_choice = input("Enter your choice: (r)ock, (p)aper, (s)cissors: ").lower() #lower() function string ke sare characters ko lowercase me convert kar deta hai.

    if user_choice not in choices:
        print("Invalid choice! Please choose r, p, or s.")

    computer_choice = random.choice(choices) #random.choice() function kisi sequence (list, tuple, string) me se randomly ek item choose karta hai.

    print(f"You chose {emojis[user_choice]}, computer chose {emojis[computer_choice]}.")

    if user_choice == computer_choice:
        print('Tie')
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print('You win!')
    else:
        print('Computer wins!')

    should_continue = input("Do you want to play again? (y/n): ").lower()
    if should_continue == 'y':
        continue