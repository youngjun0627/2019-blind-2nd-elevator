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
    while cnt<10000:
        visit = set()
        cur_calls= oncalls(token)
        timestamp, elevators, calls, is_end = cur_calls
        if cnt%100==0:
            print(calls)
        elevators = [Elevator(elevator) for elevator in elevators]
        commands = []
        for elevator in elevators:
            command = elevator.solution(calls, visit)
            commands.append(change_command(command))
        #print(commands)
        result = action(token, commands)
        if result['is_end']:
            print(timestamp)
            break
        cnt+=1
    return



if __name__ == '__main__':
    simulator(2,4)
