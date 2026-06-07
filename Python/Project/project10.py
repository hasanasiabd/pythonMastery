# Project 10: Simple Chat Application

def chat():
    print("\n--- Simple Chat Application ---")
    print("Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chat ended. Goodbye!")
            break
        else:
            print(f"Bot: You said '{user_input}'")

if __name__ == "__main__":
    chat()
