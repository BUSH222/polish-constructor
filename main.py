import random
import pyperclip

syltotal = []

with open('syllist-pol.txt') as sylfile:
    syltotal = [x.strip() for x in sylfile.readlines()]


def generate(syltotal=syltotal):
    """Generate a random word with a length of 2-5 syllables."""
    res = []
    for i in range(random.randint(2, 5)):
        res.append(random.choice(syltotal))

    return ''.join(res).lower()


while True:
    input()
    x = ' '.join([generate() for x in range(random.randint(8, 20))])
    print(x)
    pyperclip.copy(x)
