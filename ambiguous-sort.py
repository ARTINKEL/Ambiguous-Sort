import random

done = False
counter = 0
array = []

def ambiguous_sort(array):
    for x in array:
        pass

while (not done):
    number = input(("Enter Element " + str(counter) + ": "))
    try:
        array.append(int(number))
    except ValueError:
        done = True
        print(ambiguous_sort(array))
    counter += 1