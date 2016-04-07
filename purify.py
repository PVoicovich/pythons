# list of some numbers should return only even numbers
lst = [1,2,3,4,4]
lst2 = []
def  purify(lst):
    for x in lst:
        if x % 2 == 0:
            lst2.append(x)

    return lst2

print(purify(lst))