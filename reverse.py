
text = "abcd"
def reverse(text):
    L = len(text)
    word = ""
    for z in range(L-1,-1,-1):
        print(text[z])
        word+= text[z]
    return word
    #print(word)




print(reverse(text))

# return text[: : -1] simple solution