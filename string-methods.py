from dataclasses import replace
from unittest.mock import sentinel


message = "My name is Obiwan Kenobi. I am a jedi master."
# sentence = message.title()
# sentence = message.capitalize()
# sentence = message.lower()
# sentence = message.upper()

# sentence = message.isupper()

# sentence1 = "  012abd   ".strip()
# sentence = message.split()

# print(sentence1)
# print(sentence[8])

# sentence = message.split(".")
# sentence = message.split()
# sentence = "**".join(sentence)

# sentence = message.startswith('M')
# sentence = message.endswith('o')

# sentence = message.replace('Obiwan', 'Anakin').replace('Kenobi', 'Skywalker').replace('jedi', 'sith')
sentence = message.lower()
sentence = sentence.split()
sentence = "-".join(sentence)

print(sentence)