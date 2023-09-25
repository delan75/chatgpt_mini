import random

# Define a dictionary of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey!"], "hi": ["Hello!", "Hi there!", "Hey!"], "how old are you": ["I am pretty young", "I am quite old. How are you", "It is rude to ask someone's age, expecially if they are older than you","You will have to ask my developer", "I am old enough. How old are you?"],
    "how are you": ["I'm just a computer program, but I'm doing well.", "I am fine, how are you?", "I don't have feelings, but thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye-bye!"],
}

def response_method(user_input):
    user_input = user_input.lower()

    for keyword in responses:
        if keyword in user_input:
            return random.choice(responses[keyword])

    return "I'm sorry, I don't understand. Can you please rephrase your question?"


print("ChatGPT Mini: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("ChatGPT Mini: Goodbye!")
        break
    else:
        response = response_method(user_input)
        print("ChatGPT Mini:", response)

