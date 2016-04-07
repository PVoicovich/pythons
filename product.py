#Define a func. product that takes list of integers as input,returns product of all of the elements in the list.
#For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).

lst = [4, 5, 5]
def product(lst):
    sum = 1
    for x in lst:
        sum *= x
        print(sum)
    return sum

product(lst)

# problema bydet esli 0 peredatb