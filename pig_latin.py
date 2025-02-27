"""Jesse' pig latin program"""

VOWELS = 'aeiou'

while True:
    word = input("Please input the word to needed for translation to Pig Latin: ")
    if word[0] in VOWELS:
        pig_latin = word[1:] + 'way'
    else:
        pig_latin = word[1:] + word[0] + 'ay'

    print(f"Pig Latin for {word} is: {pig_latin}")

    try_again = input("Try Again? (Press enter else n to quit)")
    if try_again.lower() == "n":
        break
