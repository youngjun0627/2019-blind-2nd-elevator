import requests
import json

url = 'http://localhost:8000'


def start(user, problem, count):
    uri = url + '/start' + '/' + user + '/' + str(problem) + '/' + str(count)
    return requests.post(uri).json()


def oncalls(token):
    uri = url + '/oncalls'
    response = requests.get(uri, headers={'X-Auth-Token': token}).json()
    timestamp = response['timestamp']
    elevators = response['elevators']
    calls = response['calls']
    is_end = response['is_end']
    return timestamp, elevators, calls, is_end


def action(token, cmds):
    uri = url + '/action'
    return requests.post(uri, headers={'X-Auth-Token': token}, json={'commands': cmds}).json()

def p0_simulator():
    user = 'tester'
    problem = 0
    count = 2

    ret = start(user, problem, count)
    token = ret['token']
    print('Token for %s is %s' % (user, token))

    print(oncalls(token))
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'OPEN'}])
