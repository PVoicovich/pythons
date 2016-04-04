text = ("Hey You!") #"Hy Y!" NEED TO REMOVE a, e, i, o, u
vowel = ["a", "e", "i", "o" ,"u", "A", "E", "I", "O", "U"]
def anti_vowel(text):
    word = ""
    for l in text:
        if l not in "aeiouAEIOU":
            word += l
    return word

print(anti_vowel(text))





