import random

def simple_chatbot(user_input):
    greetings = ["hello", "hi", "hey", "greetings", "howdy"]
    farewells = ["bye", "goodbye", "see you", "farewell"]
    responses = {
        "how are you": ["I'm good, thank you!", "I'm doing well.", "Not too bad."],
        "what's your name": ["I'm a chatbot.", "Call me ChatBot.", "I don't have a name."],
        "default": ["I'm not sure how to respond to that.", "Could you please elaborate?", "Interesting!"]
    }

    user_input = user_input.lower()

    for greeting in greetings:
        if greeting in user_input:
            return random.choice(["Hello!", "Hi there!", "Greetings!"])

    for farewell in farewells:
        if farewell in user_input:
            return random.choice(["Goodbye!", "See you later!", "Farewell!"])

    for question, answers in responses.items():
        if question in user_input:
            return random.choice(answers)

    return random.choice(responses["default"])

def main():
    print("Simple ChatBot: Hi there! Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("Simple ChatBot: Goodbye! Have a great day.")
            break
        
        response = simple_chatbot(user_input)
        print(f"Simple ChatBot: {response}")

if __name__ == "__main__":
    main()
