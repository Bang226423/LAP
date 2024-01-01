def even_odd_list(list1, list2):
    result_list = []
    for number in list1:
        if number % 2 != 0:
            result_list.append(number)
    for number in list2:
        if number % 2 == 0:
            result_list.append(number)
    return result_list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", even_odd_list(list1, list2))
