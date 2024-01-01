str1 = 'Trang'
print("Chuỗi cũ:", str1)
result = str1[0]

# Get string size
l = len(str1)
# Get middle index number
mid = int(l / 2)
# Get middle character and add it to result
result = result + str1[mid]

# Get last character and add it to result
result = result + str1[l - 1]

print("Chuỗi mới:", result)
