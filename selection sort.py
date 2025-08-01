def selection_sort(arr):
    for i in range(len(arr)):
        smallest=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[smallest]:
               smallest=j
        temp=arr[i]
        arr[i]=arr[smallest]
        arr[smallest]=temp

arr=[20,15,21,18,23]
selection_sort(arr)
print(arr)









