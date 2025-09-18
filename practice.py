import math

def calculate_square_root(number):
    roots = []
    for n in number:
        root = math.sqrt(n)
        roots.append((n, root))
    return roots



num = list(map(int, input("Enter The Numbers (space-separated): ").split()))
result = calculate_square_root(num)

print("\n📌 Square Root Results:")
for n, r in result:
    # Check if root is whole number
    if r.is_integer():
        print(f"√{n} = {int(r)}")
    else:
        print(f"√{n} = {r}")