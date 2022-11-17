n=int(input("Enter the number of elements:"))
print("Enter the elements:")
list=[]
for i in range(0,n):
    element=int(input())
    if(element>100):
        list.append("over")
    else:
        list.append(element)
print(list)