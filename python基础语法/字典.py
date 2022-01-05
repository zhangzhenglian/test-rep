dict1={'name':'tom','age':20,'gender':'男'}
dict1['id']=110
dict1['name']='rose'
print(dict1)
del dict1['name']
print(dict1)
# dict1.clear()
print(dict1)
print(dict1['id'])
print(dict1.get('name'))
print(dict1.get('age'))
print(dict1.get('name','tom'))
print(dict1.keys())
print(dict1.values())
print(dict1.items())
