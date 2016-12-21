vowels = "aAiIuUeEoO"

def anti_vowel(text):
    new_text = ""
    text = str(text)
    for n in text:
        if text[n] not in vowels:
            new_text += str(text[n])
    return new_text

print anti_vowel(1234)
