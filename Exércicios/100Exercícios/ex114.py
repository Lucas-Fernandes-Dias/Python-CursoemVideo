#crie um código em Python que teste se o site PUDIM esta acessivel
import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.xvideos.com')
except:
    print('Deu erro')
else:
    print('Tem acesso')


