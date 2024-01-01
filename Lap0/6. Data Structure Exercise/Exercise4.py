list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", list)

count = dict()
for item in list:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

print("Printing count of each item  ", count)
