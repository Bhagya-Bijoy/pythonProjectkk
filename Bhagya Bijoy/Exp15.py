list1=[23,56,12,67,34]
list2=[90,76,45,43,11]
c=0
a=len(list1)
b=len(list2)
if a==b:
    print("The length of two lists are same")
else:
    print("The length of two lists are not same")
sum1=sum(list1)
sum2=sum(list2)
if sum1==sum2:
    print("Sum is same")
else:
    print("Sum is not same")
for i in list1:
    for j in list2:
        if i==j:
            print(i," occurs in both")
            c=c+1
if c==0:
    print("There is no value common in both lists.")