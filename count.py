#count  For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
sequence = [1,2,1,1]
item = 1

def count(sequence, item):
    cnt = 0
    for z in sequence:
        if z == item:
            cnt += 1
    return cnt

print(count(sequence, item))