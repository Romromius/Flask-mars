import random

import requests

test_users = False
test_jobs = True

if test_users:
    print('TESTING USERS')
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
    john = json = {'name': 'john', 'email': chr(random.randint(0, 255)), 'password': 'smith'}
    print('POST john', requests.post('http://127.0.0.1:8080/api/v2/users', json=john).json())
    print('POST john AGAIN', requests.post('http://127.0.0.1:8080/api/v2/users', json=john).json())

if test_jobs:
    print('TESTING JOBS')
    test = requests.post('http://127.0.0.1:8080/api/v2/jobs',
                         json={'team_leader': 1,
                               'job': [chr(random.randint(0, 255)) for i in range(10)],
                               'work_size': 10})
    print('POST', test.json())
    job_id = test.json()['id']
    print('GET JOB', requests.get(f'http://127.0.0.1:8080/api/v2/jobs/{job_id}').json())
    print('GET LIST', requests.get('http://127.0.0.1:8080/api/v2/jobs').json())
    print('DELETE', requests.delete(f'http://127.0.0.1:8080/api/v2/jobs/{job_id}'))
    print()
    print('NOW LET\'S MAKE SOME ERRORS')
    print('GET NOT EXISTING JOB', requests.get('http://127.0.0.1:8080/api/v2/jobs/616').json())
    print('DEL NOT EXISTING JOB', requests.delete('http://127.0.0.1:8080/api/v2/jobs/616').json())
    print('GET WRONG ADDRESS', requests.get('http://127.0.0.1:8080/api/v2/jojo'))
