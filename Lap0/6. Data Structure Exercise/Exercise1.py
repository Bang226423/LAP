list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
result = list()
odd_elements = list1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)
even_elements = list2[0::2]
print("Element at even-index positions from list two")
print(even_elements)
print("Printing Final third list")
result.extend(odd_elements)
result.extend(even_elements)
print(result)
