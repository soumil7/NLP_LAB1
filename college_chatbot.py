import random

def college_chatbot(user_input):
    greetings = ['hello', 'hi', 'hey', 'greetings', 'hola']
    farewells = ['bye', 'goodbye', 'see you', 'adios']
    about_college_keywords = ['college', 'university', 'institution']
    courses_keywords = ['courses', 'programs', 'degrees']
    faculty_keywords = ['faculty', 'professors', 'teachers']
    
    user_input_lower = user_input.lower()
    
    # Check for greetings
    if any(word in user_input_lower for word in greetings):
        return "Hello! How can I assist you today?"
    
    # Check for farewells
    elif any(word in user_input_lower for word in farewells):
        return "Goodbye! Have a great day!"
    
    # Check for inquiries about the college
    elif any(word in user_input_lower for word in about_college_keywords):
        return "Our college is dedicated to providing quality education and fostering academic excellence."
    
    # Check for inquiries about courses
    elif any(word in user_input_lower for word in courses_keywords):
        return "We offer a variety of courses in different disciplines. You can find more details on our website or contact the admission office."
    
    # Check for inquiries about faculty
    elif any(word in user_input_lower for word in faculty_keywords):
        return "Our faculty consists of experienced professors who are experts in their respective fields."
    
    # Default response
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase or ask a different question?"

# Main loop for the chatbot
def main():
    print("College Chatbot: Hi there! Ask me about the college or anything else.")
    
    while True:
        user_input = input("You: ")
        
        # Check for exit command
        if user_input.lower() == 'exit':
            print("College Chatbot: Goodbye!")
            break
        
        # Get response from the chatbot
        response = college_chatbot(user_input)
        print("College Chatbot:", response)

if __name__ == "__main__":
    main()
