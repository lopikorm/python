d = {
    'Russia': 'Moscow',
    'USA': 'Washington',
    'German':'Berlin',
    'Ukrain':'Kiev',
    'Latvia':'Riga',
    'Litva':'Vilnus',
    'Estonia':'Tallin'
}

print (d)
# for key in d.keys():
#     print(f'{key}')
# for value in d.values():
#     print(f'{value}')
for k,v in d.items():
    k,v = v,k
    print(f'{k}:{v}')
