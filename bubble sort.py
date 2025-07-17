def sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
              temp=num[j+1]
              num[j+1]=num[j]
              num[j]=temp
              

num=[5,3,1,4,2]
sort(num)
print(num)
