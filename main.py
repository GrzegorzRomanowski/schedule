from Classes import *
import random

Romanowski = LifeGuard("Grzegorz", "Romanowski", 910615, 20)
Romanowska = LifeGuard("Patrycja", "Romanowska", 910219, 20)

Lapino = Pool("Łapino", 1)
Osowa = Pool("Osowa", 2)
Lapino.timeShifts["start1"] = 9
Osowa.timeShifts["start1"] = 6

Romanowski.setAvailability()
Romanowska.setAvailability()

Romanowski.preferredPool = Lapino.name
Romanowska.preferredPool = Osowa.name

def willing(sp, x, y):
    willingList = []
    for LG in EmployeeList:
        if LG.preferredPool == sp:
            if LG.availability[x] == y or LG.availability[x] == 3:
                willingList.append(LG)            
    return willingList

def match():
    for pool in PoolList:
        shiftRemoved = []        
        for shift in pool.shifts:            
            if (shift % 1000) < 199:
                yy = 1
            else:
                yy = 2
            xx = shift % 100
            listOfWilling = willing(pool.name, xx, yy)
            try:
                winner = random.choice(listOfWilling)
                pool.schedule[shift] = winner.name          
                winner.schedule[shift] = pool.name            
                winner.availability[xx] -= yy                
                shiftRemoved.append(shift)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)

            
match()

print("!!! OSOWA !!!")
print(Osowa.schedule)
print("!!! ŁAPINO !!!")
print(Lapino.schedule)
print("!!! Romanowski !!!")
print(Romanowski.schedule)
print("!!! Romanowska !!!")
print(Romanowska.schedule)


# Code is not finished.
# Minor fixes and improvements required.
# Missing GUI
