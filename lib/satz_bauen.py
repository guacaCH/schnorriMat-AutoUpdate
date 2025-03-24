import random

firstTxt = "data/fluechomat/first.txt"
secondTxt = "data/fluechomat/second.txt"
thirdTxt = "data/fluechomat/third.txt"

def get_random_line(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines).strip()

# Main script
def form_sentence():
    extra_word = "huere"
    first = get_random_line(firstTxt)
    second = get_random_line(secondTxt)
    third = get_random_line(thirdTxt)

    if random.randint(1, 10) == 1:
        second = f"{second} {extra_word}"
    sentence = f"{first}, {second} {third}."
    return sentence


spruchListe = "data/schnupfSprueche.txt"

def schnupfspruch():
    with open(spruchListe, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines)

weisheitenListe = "data/als-weisheiten.txt"
def weisheiten():
    with open(weisheitenListe, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines)

frageliste = "data/gespraechsstoff.txt"
def frage_stellen():
    with open(frageliste, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    return random.choice(lines)