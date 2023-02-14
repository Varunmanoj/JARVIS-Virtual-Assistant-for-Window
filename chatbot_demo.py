import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
     [
        r"hi|hey|hello",
        ["Hello", "Hey there"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot and I don't have a name yet."]
    ],
    [
        r"how are you ?",
        ["I'm doing good, How about You?"]
    ],
    [
        r"sorry (.*)",
        ["Its alright", "Its OK, never mind",]
    ],
    [
        r"i am fine",
        ["Great to hear that, How can I help you today?"]
    ],
    [
        r"quit",
        ["Bye bye, take care. It was nice talking to you :) "]
    ],
]

chatbot = Chat(pairs, reflections)
chatbot.converse()

if __name__ == "__main__":
    chatbot.converse()
