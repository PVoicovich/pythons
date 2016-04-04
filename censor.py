#censor >> "this **** is wack ****"

text = "this hack is wack hack"
word = "hack"

def censor(text, word):
    Z = []
    for g in text.split():
        if g != word:
            Z.append(g)
        elif g == word:
            P = ""
            for x in g:
               x = "*"
               P += x
            Z.append(P)
    return(" ".join(Z))

print(censor(text, word))
















