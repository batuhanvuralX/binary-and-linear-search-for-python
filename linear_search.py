def linear_search(arr,target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = -1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,12,13,14,15,16


target = 12

result = linear_search(arr,target)

if result != -1:
    print(f"{target} öğenin {result} indeksinde bulundu")
else:
    print(f"{target} bulunamadı")