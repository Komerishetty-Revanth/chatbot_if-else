def chatbot():
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower().strip()
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot 101, at your service.")
        elif "help" in user_input:
            print("Chatbot: Sure, I can help! Ask me about weather, time, or just say hi.")
        elif "time" in user_input:
            from datetime import datetime
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time}.")
        elif "weather" in user_input:
            print("Chatbot: I can't fetch live weather data, but it's always sunny in my code!")
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm not sure how to respond to that. Try asking something else!")
chatbot()
