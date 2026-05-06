print("type 'hello' to start chatting with me")
while True:
    user = input("You: ").strip().lower()
    if user == "hello":
        print("Hi! Nice to meet you")
    elif user == "how are you?":
        print("I'm fine, thanks for asking! How about you?")
    elif user in ["i am fine", "i'm fine", "im fine", "i am good", "i'm good", "im good"]:
        print("Good to hear!")
    elif user in ["what can you do", "what can you do?"]:
        print("I can chat with you! Try saying hello, ask how I am, or type 'bye' to exit.")
    elif user in ["thanks", "thank you"]:
        print("You're welcome!")
    elif user in ["bye", "goodbye"]:
        print("Goodbye! Have a great day!")
        break
    else:
        print("Sorry, I don't understand that")