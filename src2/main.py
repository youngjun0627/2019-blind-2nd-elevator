from API import startAPI, oncallsAPI, actionAPI
from helper import Elevator, Calls

def main(token):
    MAX = 10000
    while MAX>0:
        oncalls = oncallsAPI(url, token)
        calls = oncalls['calls']
        elevators = oncalls['elevators']
        calls = Calls(calls)
        elevators = [Elevator(elevator) for elevator in elevators]
        commands = []
        for i, elevator in enumerate(elevators):
            command = elevator.solution(calls)
            commands.append(command)
        result = actionAPI(url, token, {'commands': commands})
        print(result)
        if result['is_end']: break
        #print(result)

        MAX-=1

if __name__=='__main__':
    user = 'tester'
    num_elevator = 4
    url = 'http://localhost:8000'
    problem_id = 2
    token = startAPI(url, user, problem_id, num_elevator)
    main(token)
