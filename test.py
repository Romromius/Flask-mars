import requests

test = requests.post('http://127.0.0.1:8080/api/v2/users',
                     json={'name': 'OLOLO',
                           'email': 'asd.awda.fae',
                           'password': 'hola'})
print(test.json())
