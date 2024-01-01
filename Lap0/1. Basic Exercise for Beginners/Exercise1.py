def multiplication_or_sum(num1, num2) :
    nhan = num1 * num2
    if nhan <=1000:
        return nhan
    else:
        return num1 + num2
result = multiplication_or_sum(20, 30)
print("The result is ", result)
result = multiplication_or_sum(40, 30)
print("The result is ", result)

