class BusBooking:
    def __init__(self, n: int):
        self.bus = defaultdict(set)
        self.bustimes = defaultdict(lambda: [0, 0, 0, 0])
        self.total = 0
        self.mintime = 0

    def toggle(self, seat_str: str) -> None:
        seat = seat_str[0]
        row = int(seat_str[1:])

        if seat == 'B':
            # FREEING
            if seat in self.bus[row]:
                self.bus[row].remove(seat)
                self.bustimes[row][1] = 0
                self.total -= 1
                self.mintime -= 1

            # BOOKING
            else:
                self.bus[row].add(seat)
                self.bustimes[row][1] = 1
                self.total += 1
                self.mintime += 1

        elif seat == 'C':
            # FREEING
            if seat in self.bus[row]:
                self.bus[row].remove(seat)
                self.bustimes[row][2] = 0
                self.total -= 1
                self.mintime -= 1

            # BOOKING
            else:
                self.bus[row].add(seat)
                self.bustimes[row][2] = 1
                self.total += 1        
                self.mintime += 1
                
        elif seat == 'A':
            # FREEING
            if seat in self.bus[row]:
                self.bus[row].remove(seat)
                self.total -= self.bustimes[row][0]
                self.mintime -= 1
                self.bustimes[row][0] = 0
            
            # BOOKING
            else:  
                self.bus[row].add(seat)
                if 'B' in self.bus[row]:
                    self.bustimes[row][0] = 3
                    self.total += 3
                    self.mintime += 1
                else:
                    self.bustimes[row][0] = 1
                    self.total += 1
                    self.mintime += 1
                    
        elif seat == 'D':
            # FREEING
            if seat in self.bus[row]:
                self.bus[row].remove(seat)
                self.total -= self.bustimes[row][3]
                self.mintime -= 1
                self.bustimes[row][3] = 0
            
            # BOOKING
            else:  
                self.bus[row].add(seat)
                if 'C' in self.bus[row]:
                    self.bustimes[row][3] = 3
                    self.total += 3
                    self.mintime += 1
                else:
                    self.bustimes[row][3] = 1
                    self.total += 1
                    self.mintime += 1
        

    def getTotalTime(self) -> int:
        return self.total

    def getMinTime(self) -> int:
        return self.mintime


# Your BusBooking object will be instantiated and called as such:
# obj = BusBooking(n)
# obj.toggle(seat)
# param_2 = obj.getTotalTime()
# param_3 = obj.getMinTime()

'''
Test cases (must expand window to see them lined up):

["BusBooking","toggle","toggle","getMinTime","toggle","getTotalTime","getTotalTime","getMinTime","getTotalTime","toggle","getTotalTime"]
[[1],         ["D1"],   ["C1"],      [],      ["D1"],      [],            [],            [],           [],       ["D1"],       []]
[null,         null,      null,       2,       null,        1,             1,             1,            1,        null,         4]


["BusBooking", "toggle", "toggle", "getTotalTime", "getMinTime", "toggle", "toggle", "getTotalTime", "getMinTime"]
[[20],          ["B3"],   ["A3"],        [],           [],        ["C3"],   ["D3"],        [],            []]
[null,           null,      null,         4,            2,         null,      null,         8,            4]
'''
