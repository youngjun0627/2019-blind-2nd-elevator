import requests
import json

def startAPI(url, user, problem_id, num_elevator):
    url = url + '/start' + '/{}'.format(user) + '/{}'.format(problem_id) + '/{}'.format(num_elevator)
    resp = requests.post(url)
    resp = resp.json()
    return resp['token']

def oncallsAPI(url, token):
    url = url + '/oncalls'
    headers = {'X-Auth-Token': token}
    resp = requests.get(url = url, headers = headers)
    resp = resp.json()
    return resp

def actionAPI(url, token, commands):
    url = url + '/action'
    headers = {'X-Auth-Token': token,
            'Content-Type': 'application/json'
    }
    data = json.dumps(commands)
    resp = requests.post(url=url, headers = headers, data = data)
    resp = resp.json()
    return resp

if __name__=='__main__':
    url = 'http://localhost:8000'
    user = 'tester'
    problem_id = 1
    num_elevator = 4
    token =  startAPI(url, user, problem_id, num_elevator)
    ret = oncallsAPI(url, token)
    print(ret)
    

