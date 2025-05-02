import random
random_text=[
    "Cool, I'm on it BRO",
    "okay BRO ,I'm working on it",
    "just a sec BRO",
]


def respond():
    response = random.choice(random_text)
    print(response)
    
    return response




respond()