import nltk
from nltk.chat.util import Chat, reflections

# Sample data for our chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey!"]
    ],
    [
        r"how are you?",
        ["I'm doing good, how about you?", "I'm great, thanks for asking!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem", "Don't worry about it"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye!", "See you later!", "Bye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that."]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hi, I'm your chatbot. Type 'bye' to exit.")
    chatbot.converse()

# Start the chat
if __name__ == "__main__":
    start_chat()
