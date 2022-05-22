x = input('Digite algo: ')
print(type(x))
s1=(x.isnumeric())
s2=(x.isupper())
s3=(x.isdecimal())
print('O que digitou é um numero?: {}'.format(s1))
print('O que digitou esta em caixa alta?:{} '.format(s2))
print('O que digitou é decimal?: {}'.format(s3))




