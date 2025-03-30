"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Faulhammer
email: faulhammer.petr@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
    '''This monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username: ")
password = input("password: ")

if username in users and users[username] == password:
    print("-" * 40)
    print(f"Welcome to the app, {username}")
    print(f"We have {len(TEXTS)} texts to be analyzed.")
    print("-" * 40)
else:
    print("unregistered user, terminating the program..")
    exit()

vyber = input("Enter a number btw. 1 and 3 to select: ")
print("-" * 40)

if not vyber.isdigit():
    print("Invalid input, must be a number.")
    exit()

cislo = int(vyber)
if cislo < 1 or cislo > len(TEXTS):
    print("Number out of range, terminating..")
    exit()

text = TEXTS[cislo - 1]
slova = text.split()
ocistena_slova = []

for slovo in slova:
    slovo = slovo.strip(".,")
    ocistena_slova.append(slovo)

pocet_slov = len(ocistena_slova)
titlecase = 0
uppercase = 0
lowercase = 0
cisla = 0
suma_cisel = 0

for slovo in ocistena_slova:
    if slovo.istitle():
        titlecase += 1
    elif slovo.isupper() and slovo.isalpha():
        uppercase += 1
    elif slovo.islower():
        lowercase += 1
    if slovo.isnumeric():
        cisla += 1
        suma_cisel += int(slovo)

print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {cisla} numeric strings.")
print(f"The sum of all the numbers {suma_cisel}")
print("-" * 40)

print(f"{'LEN':<3}|{'OCCURENCES':^20}|{'NR.':>3}")
print("-" * 40)

delky = {}

for slovo in ocistena_slova:
    delka = len(slovo)
    if delka not in delky:
        delky[delka] = 1
    else:
        delky[delka] += 1

for delka in sorted(delky):
    pocet = delky[delka]
    hvezdicky = "*" * pocet
    print(f"{delka:<3}|{hvezdicky:<20}|{pocet}")
