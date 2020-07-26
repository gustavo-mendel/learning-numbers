from num2words import num2words
from random import randint
import functions

functions.intro()

numberAux = functions.getLanguage()
lang = functions.setLang(numberAux)


print(f"\nlang = {lang}")
number = randint(0, 1001)
ordinal = False

word = num2words(number, ordinal, lang)

print(f"{number}: ", end='')
resp = input()

print("\n" + resp)
print(word + "\n")

if resp == word:
    print("Resposta correta")
else:
    print("Resposta errada")
