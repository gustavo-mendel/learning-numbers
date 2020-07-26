lang = {
    "ar": "Arabic",
    "cz": "Czech",
    "de": "German",
    "dk": "Danish",
    "en": "English",
    "en_IN": "English - India",
    "es": "Spanish",
    "es_CO": "Spanish - Colombia",
    "es_VE": "Spanish - Venezuela",
    "fi": "Finnish",
    "fr": "French",
    "fr_BE": "French - Belgium",
    "fr_CH": "French - SWITZERLAND",
    "fr_DZ": "French - Algeria", 
    "he": "Hebrew",
    "id": "Indonesian",
    "it": "Italian",
    "ja": "Japanese",
    "kn": "Kannada",
    "ko": "Korean",
    "lt": "Lithuanian",
    "lv": "Lettish",
    "nl": "Dutch",
    "no": "Norwegian",
    "pl": "Polish",
    "pt": "Portuguese",
    "pt_BR": "Portuguese - Brazil",
    "ro": "Romanian",
    "ru": "Russian",
    "sl": "Slovenian",
    "sr": "Serbian",
    "th": "Thai",
    "tr": "Turkish",
    "uk": "Ukrainian",
    "vi": "Vietnamese"
}


def intro():
    print("="*35)
    print(f"={'Learning Numbers':^33}=")
    print("="*35)


def listAll():
    i = 0
    for v in lang.values():
        print(f"( {i:>2} ) {v}")
        i += 1


def getLanguage(number=4):
    langShort = setLang(number)
    langLarge = findLang(langShort)
    print(f"\nLanguage: {langLarge} [{langShort}]")
    change = input("Do you wanna change? [Y/n] ")
    while change not in "nNyY":
        change = input("Do you wanna change? [Y/n] ")
    if change in "yY":
        print("\nWe have these languages:")
        listAll()
        number = int(input("\nNew Language: [0 to 34] "))
        while number not in range(0, 35):
            print("\nInvalid option, try again ...")
            number = int(input("New Language: [0 to 34] "))
        return getLanguage(number)
    else:
        return number


def setLang(num):
    for k, v in enumerate(lang.keys()):
        if k == num:
            return v


def findLang(idiom):
    for k, v in lang.items():
        if idiom == k:
            return v
            