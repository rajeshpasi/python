HISTORY_FILE = "calc_history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, "r") as file:
            lines = file.readlines()
            if len(lines) == 0:
                print("No history found.")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found.")

def clear_history():
    open(HISTORY_FILE, "w").close()
    print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, "a") as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
    parts = user_input.split()
    if len(parts) != 3:
        print("Invalid input format. Please use: number operator number (e.g., 3 + 4)")
        return None

    try:
        num1 = float(parts[0])
        operator = parts[1]
        num2 = float(parts[2])
    except ValueError:
        print("Invalid numbers.")
        return None

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print("Invalid operator. Please use one of: +, -, *, /")
        return None

def main():
    print("Welcome to the Calculator with History!")
    while True:
        user_input = input("Enter calculation (or 'history', 'clear', 'exit'): ").strip()
        if user_input.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break
        elif user_input.lower() == "history":
            show_history()
        elif user_input.lower() == "clear":
            clear_history()
        else:
            result = calculate(user_input)
            if result is not None:
                # Result को integer जैसा दिखाना (e.g., 7.0 → 7)
                if int(result) == result:
                    result = int(result)
                print(f"Result: {result}")
                save_to_history(user_input, result)

main()
