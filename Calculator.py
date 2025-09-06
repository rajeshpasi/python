# Step 1: User se numbers lena
num1 = float(input("Pehala number daalo:"))
num2 = float(input("Doosra number daalo:"))

# Step 2: User se operator lena
operator = input("Operator daalo (+, -, *, /): ")

# Step 3: Conditions check karna
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    result = num1 / num2
# Step 4: Output dikhana
print("Result:", result)