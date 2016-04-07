# takes in a list of scores, scores, Computes the sum of the scores, Returns the computed sum
#Call the newly created grades_sum() function with the list of grades and print the result
# And DEF AVERAGE also here
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

"""def print_grades(grades):
    for x in grades:
        print(x)
        #return x
print(print_grades(grades))"""

def grades_sum(grades):
    total = 0
    for x in grades:
        total += x
    return total

def grades_average(grades):
    avg = grades_sum(grades) / float(len(grades))
    return avg

print(grades_average(grades))



