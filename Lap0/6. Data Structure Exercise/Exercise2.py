list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", list)
element = list.pop(4)
print("List After removing element at index 4 ", list)

list.insert(2, element)
print("List after Adding element at index 2 ", list)

list.append(element)
print("List after Adding element at last ", list)
