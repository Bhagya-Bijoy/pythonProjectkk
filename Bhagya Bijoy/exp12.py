string1=input("Enter the string:")
a=string1[0]
for i in string1:
    if i==a:
        string1=string1.replace(i,'$')
        string1=a+string1[1:]
print(string1)
