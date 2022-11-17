str1=input("Enter the string:")
print(str1)
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for j,k in dict1.items():
    print(j,k)
