def check_first_last(numlist):
    print("Given list:", numlist)
    first_num = numlist[0]
    last_num = numlist[-1]
    if first_num ==last_num:
        return True
    else:
        return False

numlistx = [10, 20, 30, 40, 10]
print("result is", check_first_last(numlistx))
numlisty = [75, 65, 35, 75, 30]
print("result is", check_first_last(numlisty))
