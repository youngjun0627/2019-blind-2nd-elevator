import heapq

class Elevator(object):
    def __init__(self, elevator):
        self.id = elevator['id']
        self.floor = elevator['floor']
        passengers = elevator['passengers']
        self.passengers = []
        for passenger in passengers:
            id = passenger['id']
            time = passenger['timestamp']
            start = passenger['start']
            end = passenger['end']
            heapq.heappush(self.passengers, (time, id, start, end))
        self.status = elevator['status']
        self.command = None
        self.call_ids = []
        self.MAX_COUNT = 8
        self.count = len(self.passengers)

    def check_command(self):
        if self.command is None: return True
        return False

    def check_count(self):
        if self.count<self.MAX_COUNT-1: return True
        return False

    def check_empty(self):
        if self.passengers: return False
        return True

    def stop(self):
        if not self.check_command(): return False
        if self.status not in ['UPWARD', 'DOWNWARD', 'STOPPED']: return False
        self.command = 'STOP'
        return True

    def up(self):
        if not self.check_command(): return False
        if self.status not in ['UPWARD', 'STOPPED']: return False
        self.command = 'UP'
        return True

    def down(self):
        if not self.check_command(): return False
        if self.status not in ['DOWNWARD', 'STOPPED']: return False
        self.command = 'DOWN'
        return True

    def open(self):
        if not self.check_command(): return False
        if self.status not in ['STOPPED', 'OPENED']: return False
        self.command = 'OPEN'
        return True

    def close(self):
        if not self.check_command(): return False
        if self.status not in ['OPENED']: return False
        self.command = 'CLOSE'
        return True

    def enter(self, id):
        if self.command not in [None, 'ENTER']: return False
        if self.status not in ['OPENED']: return False
        if not self.check_count(): return False
        self.command = 'ENTER'
        self.call_ids.append(id)
        self.count+=1
        return True

    def exit(self, id):
        if self.command not in [None, 'EXIT']: return False
        if self.status not in ['OPENED']: return False
        self.command = 'EXIT'
        self.call_ids.append(id)
        self.count-=1
        return True

    def func_enter(self, calls, visit):
        check = False
        for call in calls:
            time, id, start, end = call
            if id in visit: continue
            if start==self.floor:
                if not self.enter(id):
                    if not self.open():
                        self.stop()
                visit.add(id)
                check = True
        return check

    def func_exit(self):
        calls = self.passengers
        check = False
        for call in calls:
            time, id, start, end = call
            if end==self.floor:
                if not self.exit(id):
                    if not self.open():
                        self.stop()
                check = True
        return check

    def move(self, calls, visit):
        if self.status=='OPENED':
            self.close()
            return True

        if not self.check_empty():
            first_call = heapq.heappop(self.passengers)
            time, id, start, end = first_call
            if self.floor>end:
                if not self.down():
                    self.stop()
            elif self.floor<end:
                if not self.up():
                    self.stop()

        else:
            first_call = None
            for call in calls:
                _, id, start, end = call
                if id in visit: continue
                first_call = call
                break
            if first_call is None:
                self.stop()
                return
            time, id, start, end = first_call
            if self.floor>start:
                if not self.down():
                    self.stop()
            elif self.floor<start:
                if not self.up():
                    self.stop()

        return False

    def func_return(self):
        if self.command is None: self.stop()
        if self.call_ids:
            return {'elevator_id': self.id,
                    'command': self.command,
                    'call_ids': self.call_ids
            }
        else:
            return {'elevator_id': self.id,
                    'command': self.command
            }

    def solution(self, calls):
        calls, visit = calls.q, calls.visit
        if not self.func_exit():
            if not self.func_enter(calls, visit):
                self.move(calls, visit)
        return self.func_return()
        '''
        if not self.check_count(): self.func_exit()
        for call in calls:
            time, id, start, end = call
            if start == self.floor:
                self.enter(id)
                visit.add(id)
        if not self.check_count():
            check = self.func_exit()
            if check: return self.func_return()
            self.move(calls)
            return self.func_return()

        else:
            check = self.func_enter(calls, visit)
            if check: return self.func_return()
            self.move(calls)
            return self.func_return()
        '''

class Calls(object):
    def __init__(self, calls):
        self.q = []
        for call in calls:
            id = call['id']
            timestamp = call['timestamp']
            start = call['start']
            end = call['end']
            heapq.heappush(self.q, (timestamp, id, start, end))
        self.visit = set()
    def get_calls(self):
        return self.q
