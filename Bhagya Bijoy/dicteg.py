dict1={'fruit':'apple','climate':'hot','mark':10}
print(dict1)
print(dict1['mark'])
dict1.pop("climate")
print(dict1)
dict1.update({"fruit":"mango"})
print(dict1)
dict1.update({"car":"lumborgini"})
print(dict1)
x=dict1.copy()
print(x)
y=dict1.keys()
print(y)
z=dict1.values()
print(z)