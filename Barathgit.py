a = {'person1': {'name': 'Barath', 'age': 21, 'City': 'Salem'},
     'person2': {'name': 'arun','age': 21, 'City': 'Chennai'}
     }
for key,val in a.items():
    print(key)
    for k in val:
        print(k)
        print(val[k])