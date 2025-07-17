def sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
n=int(input("enter an size of an array:"))
num=[0]*n

for i in range(n):
    num[i]=int(input("enter a value:"))

sort(num)
print(num)
