
class Elevator(object):
    def __init__(self, elevator):
        self.id = elevator['id']
        self.floor = elevator['floor']
        self.passengers = elevator['passengers']
        self.status = elevator['status']
        self.command = None
        self.call_ids = []
        self.MAX_COUNT = 8
        self.count = len(self.passengers)
        #print(self.id, self.floor, self.passengers, self.status, self.count)
    def stop(self):
        if self.status=='OPENED': return False
        self.command='STOP'
        return True

    def open(self):
        if self.status=='UPWARD' or self.status=='DOWNWARD': return False
        self.command = 'OPEN'
        return True

    def enter(self, id):
        if not self.status=='OPENED': return False
        self.command ='ENTER'
        self.call_ids.append(id)
        return True

    def exit(self, id):
        if not self.status=='OPENED': return False
        self.command = 'EXIT'
        self.call_ids.append(id)
        return True

    def close(self):
        if not self.status=='OPENED': return False
        self.command='CLOSE'
        return True

    def up(self):
        if self.status=='OPENED' or self.status=='DOWNWARD': return False
        self.command='UP'
        return True
    
    def down(self):
        if self.status=='OPENED' or self.status=='UPWARD': return False
        self.command='DOWN'
        return True

    def func_exit(self):
        for passenger in self.passengers:
            if self.floor == passenger['end']:
                if self.status=='OPENED':
                    self.exit(passenger['id'])
                elif self.status=='STOPPED':
                    self.open()
                    return True
                else:
                    self.stop()
                    return True
        if self.call_ids:
            return True
        else:
            return False
    
    def func_enter(self, calls, visit):
        if self.count>=self.MAX_COUNT: return False
        for person_id, call in enumerate(calls):
            id = call.get('id')
            if person_id in visit: continue

            timestamp = call.get('timestamp')
            start = call.get('start')
            end = call.get('end')
            if start==self.floor:
                if self.status=='OPENED':
                    if self.MAX_COUNT>self.count:
                        self.enter(id)
                        visit.add(person_id)
                        self.count+=1
                elif self.status=='STOPPED':
                    self.open()
                    return True
                else:
                    self.stop()
                    return True
        if self.call_ids:
            return True
        else:
            return False

    def check_close(self):
        if self.status=='OPENED':
            self.close()
            return True
        return False
    
    def check_stop(self, calls):
        if not calls and not self.passengers and (self.status=='UPWARD' or self.status=='DOWNWARD'):
            self.stop()
            return True
        return False

    def move(self, calls):
        if self.passengers:
            end = self.passengers[0]['end']
            end = int(end)
            if end>self.floor:
                self.up()
                return True
            elif end<self.floor:
                self.down()
                return True
        else:
            dest = 0
            diff = 1000000
            for call in calls:
                start = int(call['start'])
                if diff>abs(self.floor-start):
                    diff = abs(self.floor-start)
                    dest = start
                    break
            #id, timestamp, start, end = first_passenger[0]
            if dest>self.floor:
                self.up()
                return True
            elif dest<self.floor:
                self.down()
                return True
        return False

    def return_result(self):
        result = []
        result.append(self.id)
        if self.command is not None:
            result.append(self.command)
        else:
            result.append('STOP')
        if self.call_ids:
            result.append(self.call_ids)
        return result

    def solution(self, calls, visit):
        check = self.func_exit()
        if check: return self.return_result()
        check = self.func_enter(calls, visit)
        if check: return self.return_result()
        check = self.check_close()
        if check: return self.return_result()
        check = self.check_stop(calls)
        if check: return self.return_result()
        check = self.move(calls)
        if check: return self.return_result()
        '''
        if calls:
            check = self.move(calls[0])
            if check: return self.return_result()
        '''
        return self.return_result()
