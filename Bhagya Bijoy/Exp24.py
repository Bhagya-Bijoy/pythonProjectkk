str1=input("Enter the line of code:")
print(str1)
dict1={}
str2=str1.split(' ')
for i in str2:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for j,k in dict1.items():
    print(j,k)