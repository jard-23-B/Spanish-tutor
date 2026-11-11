import random

words = {
    "hallo": "hola",
    "bedankt": "gracias",
    "alsjeblieft": "por favor",
    "water": "agua",
    "eten": "comida"
}

print("🇪🇸 Welkom bij je Spaanse tutor!")
print("We gaan 5 woorden oefenen.\n")

score = 0

questions = list(words.items())
random.shuffle(questions)

for dutch, spanish in questions:
    answer = input(f"Hoe zeg je '{dutch}' in het Spaans? ")

    if answer.lower().strip() == spanish:
        print("✅ ¡Muy bien!\n")
        score += 1
    else:
        print(f"❌ Het juiste antwoord is: {spanish}\n")

print(f"Je score: {score}/{len(questions)}")
