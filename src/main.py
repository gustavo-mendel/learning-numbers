from num2words import num2words
from random import randint
import functions

functions.intro()

numberAux = functions.getLanguage()
langShort = functions.setLang(numberAux)
langLarge = functions.findLang(langShort)

number = randint(0, 1001)
ordinal = False

word = num2words(number, ordinal, langShort)

print(f"\nHow to write the number {number} in {langLarge}?")
resp = input()

print(f"\nRight answer: {word}")
print(f"Your  answer: {resp}\n")

if resp == word:
    print("Resposta correta")
else:
    print("Resposta errada")
