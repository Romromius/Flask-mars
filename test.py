import random

import requests

test = requests.post('http://127.0.0.1:8080/api/v2/users',
                     json={'name': 'test',
                           'email': chr(random.randint(0, 255)),
                           'password': 'hola'})
print('POST', test.json())
user_id = test.json()['id']
print('GET USER', requests.get(f'http://127.0.0.1:8080/api/v2/users/{user_id}').json())
print('GET LIST', requests.get('http://127.0.0.1:8080/api/v2/users').json())
print('DELETE', requests.delete(f'http://127.0.0.1:8080/api/v2/users/{user_id}'))
print()
print('NOW LET\'S MAKE SOME ERRORS')
print('GET NOT EXISTING USER', requests.get('http://127.0.0.1:8080/api/v2/users/616').json())
print('DEL NOT EXISTING USER', requests.delete('http://127.0.0.1:8080/api/v2/users/616').json())
print('GET WRONG ADDRESS', requests.get('http://127.0.0.1:8080/api/v2/use'))
