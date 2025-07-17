def sort(num):
    for i in range(len(num)):
        for j in range(len(num)-1):
            if num[j]>num[j+1]:
              temp=num[j+1]
              num[j+1]=num[j]
              num[j]=temp
              

n=int(input("enter size of an array:"))
num=[]
for i in range(n):
  val=int(input("enter value:"))
  num.append(val)

sort(num)
print(num)
