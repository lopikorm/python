# Список (list)
l = []
for i in range (1,101):
    if (i%3)==0 and (i%5)!=0:
        l.append('Fizz')
    elif (i%5)==0 and (i%3)!=0:
        l.append('Buzz')
    elif (i%5)==0 and (i%3)==0:
        l.append('FizzBuzz')
    else:
        l.append(i)
print(l)

# Или в столбик

for i in range (1,101):
    if (i%3)==0 and (i%5)!=0:
        print('Fizz')
    elif (i%5)==0 and (i%3)!=0:
        print('Buzz')
    elif (i%5)==0 and (i%3)==0:
        print('FizzBuzz')
    else:
       print(i)


