#For example: remove_duplicates([1,1,2,2]) should return [1,2].
lst = [1,3,1,2,2]

def remove_duplicates(lst):
    lst_new = []
    for x in lst:
        if x not in lst_new:
            lst_new.append(x)
    return lst_new


print(remove_duplicates(lst))