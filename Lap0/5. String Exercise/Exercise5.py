def infostring(str1):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in str1:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1
    print("Chars =", char_count, "\nDigits =", digit_count, "\nSymbol =", symbol_count)
str1 = "P@yn2at&#i5ve"
print ("Total counts of chars, digits and symbols \n")
infostring(str1)
