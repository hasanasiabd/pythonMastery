# Project 8: Number Guessing Game and Simple Calculator

import random

def calculator():
    print("\n--- Simple Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    choice = input("Select operation (1-4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error! Division by zero is not allowed.")
    else:
        print("Invalid choice!")

def guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def main():
    while True:
        print("\n================ MAIN MENU ================")
        print("1. Play Number Guessing Game")
        print("2. Use Simple Calculator")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            guessing_game()
        elif choice == '2':
            calculator()
        elif choice == '3':
            print("Goodbye! Thanks for playing.")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()