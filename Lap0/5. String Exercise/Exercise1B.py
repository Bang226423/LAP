def ba_chu_giua(str1):
    print("Chuỗi đầu:", str1)
    mid = int(len(str1) / 2)
    result = str1[mid - 1:mid + 2]
    print("Ba chữ giữa là :", result)
ba_chu_giua("JhonDipPeta")
ba_chu_giua("JaSonAy")
ba_chu_giua("Trang")
