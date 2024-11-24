def binary_search(arr, target):

    # Başlangıç ve bitiş indekslerini belirleyin
    start = 0
    end = len(arr) -1

    # while ile dögüye alarak işleme başlat starttan end e kadar
    while start <= end:

        # listenin orta indeksini hesaplamak
        mid = (start + end) //2

        # eğer hedef ortadaki öğe ile eşleşti ise öğe bulundu demektir
        if arr[mid] == target:
            return mid
        
        #hedef öğe ortadakinden küçükse, sol yarıya atla
        elif arr[mid] > target:
            end = mid -1

        # hedef öğe ortadakinden büyükse, sağ yarıya atla
        else:
            start = mid + 1
            
    # eğer öğe listede yoksa, -1 döndür
    return -1

arr = [-101,-80,-50,-45,-33,-26,-12,-5,-1,0,1,3,5,7,8,8,11,24,56,89,101,202]

target = -5

result = binary_search(arr,target)

if result !=-1:
    print(f"{target} öğesi {result}. indekste bulundu")
else:
    print(f"{target} bulunamadı")