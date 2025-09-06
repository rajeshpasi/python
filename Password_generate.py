import random
import string

# Step 1: User se length lena
length = int(input("Enter the desired length of the password: "))

# Step 2: Characters ka pool define karna
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Randomly password generate karna
password = ''.join(random.choice(characters) for i in range(length))

# Step 4: Generated password dikhana
print("Generated Password:", password)