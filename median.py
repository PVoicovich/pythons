#For example: median([1,1,2]) should return 1.
#the median of the sequence [7,3,1,4] is 3.5, since the middle elements are 3 and 4 and (3 + 4) / (2.0) is 3.5.
# tip sorted([5, 2, 3, 1, 4]) returns [1, 2, 3, 4, 5]

#lst = [1,2,3,4,5,6] # need to get 4
lst = [6, 8, 12, 2, 23]
def median(lst):
    if len(lst) % 2 != 0:
        lst = sorted(lst)
        mdl = 0
        mdl += (len(lst)) / 2
        return lst[int(mdl)]
    if len(lst) % 2 == 0:
        lst = sorted(lst)
        mdl1 = int((len(lst)) / 2)
        mdl2 = int(((len(lst)) / 2) - 1)
        mdn = (lst[mdl1] + lst[mdl2]) / (2.0)
        #print(mdl1,"", mdl2, "", mdn)
        return mdn

print(median(lst))

