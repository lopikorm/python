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

for k,v in d.items():
    k,v = v,k
    print(f'{k}:{v}')
