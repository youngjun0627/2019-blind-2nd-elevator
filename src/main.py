import requests
from API import start, oncalls, action
from helper import Elevator

def change_command(command):
    if len(command)==3:
        elevator_id, command, call_ids = command
        return {'elevator_id': elevator_id, 'command': command, 'call_ids':call_ids}
    elif len(command)==2:
        elevator_id, command = command
        return {'elevator_id': elevator_id, 'command': command}

def simulator(problem, count):
    user = 'tester'
    ret = start(user, problem, count)
    token = ret['token']
    visit = set()
    print('Token for %s is %s' % (user, token))
    cnt=0
    while cnt<10:
        cur_calls= oncalls(token)
        timestamp, elevators, calls, is_end = cur_calls
        elevators = [Elevator(elevator) for elevator in elevators]
        commands = []
        for elevator in elevators:
            command = elevator.solution(calls, visit)
            commands.append(change_command(command))
        action(token, commands)
        cnt+=1
    print(visit)
    return


    action(token, commands)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'ENTER', 'call_ids': [2, 3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [0, 1]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [2]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [1]}, {'elevator_id': 1, 'command': 'UP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'OPEN'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'EXIT', 'call_ids': [3]}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'CLOSE'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'DOWN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [0, 4]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'ENTER', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'CLOSE'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'UP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'STOP'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'OPEN'}, {'elevator_id': 1, 'command': 'STOP'}])

    oncalls(token)
    action(token, [{'elevator_id': 0, 'command': 'EXIT', 'call_ids': [5]}, {'elevator_id': 1, 'command': 'STOP'}])


if __name__ == '__main__':
    simulator(0,2)
