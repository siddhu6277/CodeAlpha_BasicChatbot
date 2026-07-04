print("=" * 50)
print("      Welcome to CodeAlpha Basic Chatbot")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! 👋")
print("I am your virtual assistant.")
print("Type 'help' to see what I can do.")
print("Type 'bye' anytime to exit.\n")

while True:

    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print(f"Bot: Hello {name}! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I'm doing great. Thanks for asking!")

    elif user == "who are you":
        print("Bot: I am a Basic Chatbot created using Python for the CodeAlpha Internship.")

    elif user == "what is your name":
        print("Bot: My name is CodeAlpha Bot.")

    elif user == "thank you":
        print("Bot: You're welcome! 😊")

    elif user == "help":
        print("\nI can respond to:")
        print("- hello")
        print("- hi")
        print("- how are you")
        print("- who are you")
        print("- what is your name")
        print("- thank you")
        print("- bye\n")

    elif user == "bye":
        print(f"Bot: Goodbye {name}! Have a wonderful day. 👋")
        break

    else:
        print("Bot: Sorry! I don't understand that.")