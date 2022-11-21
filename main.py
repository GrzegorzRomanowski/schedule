from Classes import *
import random

Romanowski = LifeGuard("Grzegorz", "Romanowski", 910615, 20)
Romanowska = LifeGuard("Patrycja", "Romanowska", 910219, 20)
RomanowskaSara = LifeGuard("Sara", "Romanowska", 192729, 20)
RomanowskaIga = LifeGuard("Iga", "Romanowska", 222516, 20)
#del Romanowski
#print(EmployeeList)
#print(Romanowska.showLifeGuardInfo())

Łapino = Pool("Łapino", 1)
Osowa = Pool("Osowa", 2)
Łapino.timeShifts["start1"] = 9
Osowa.timeShifts["start1"] = 6
#del Osowa
#print(PoolList)
#print(Łapino.showPoolInfo())
#print(Osowa.showPoolInfo())

Romanowski.setAvailability()
Romanowska.setAvailability()
RomanowskaSara.setAvailability()
RomanowskaIga.setAvailability()
Romanowski.preferredPool = Osowa.name
Romanowska.preferredPool = Osowa.name
RomanowskaSara.preferredPool = Łapino.name
RomanowskaIga.preferredPool = Łapino.name
#print(Romanowska.availability)

#print(Osowa.schifts)
#print(Łapino.schifts)

def willing3(sp, x):      #np. Osowa, 1, M
    willingList = []
    for LG in EmployeeList:
        if LG.preferredPool == sp:
            if LG.availability[x] == 3:
                willingList.append(LG)
    return willingList

def willing(sp, x, y):      #np. Osowa, 1, M
    willingList = []
    for LG in EmployeeList:
        if LG.preferredPool == sp:
            if LG.availability[x] == y or LG.availability[x] == 3:
                willingList.append(LG)            
    return willingList

def match():
    for pool in PoolList:
        schiftRemoved = []        
        for schift in pool.schifts:            
            xx = schift % 100
            listOfWilling = willing3(pool.name, xx)
            try:
                winner = random.choice(listOfWilling)
                if (((schift + 100)//100)%10) == 1 or (((schift + 100)//100)%10) == 2:
                    schift2 = schift + 100
                elif   (((schift - 100)//100)%10) == 1 or (((schift - 100)//100)%10) == 2:
                    schift2 = schift - 100
                if schift not in pool.schedule:
                    pool.schedule[schift] = winner.name
                if schift2 not in pool.schedule:
                    pool.schedule[schift2] = winner.name                      
                if schift not in winner.schedule:
                    winner.schedule[schift] = pool.name
                if schift2 not in winner.schedule:
                    winner.schedule[schift2] = pool.name                       
                winner.availability[xx] = 0                          
                if schift not in schiftRemoved:
                    schiftRemoved.append(schift)
                if schift2 not in schiftRemoved:
                    schiftRemoved.append(schift2)
            except (IndexError):
                None
        for s in schiftRemoved:
            pool.schifts.remove(s)

    for pool in PoolList:
        schiftRemoved = []        
        for schift in pool.schifts:            
            if (schift % 1000) < 199:
                yy = 1
            else:
                yy = 2
            xx = schift % 100
            listOfWilling = willing(pool.name, xx, yy)
            try:
                winner = random.choice(listOfWilling)
                pool.schedule[schift] = winner.name          
                winner.schedule[schift] = pool.name            
                winner.availability[xx] -= yy                
                schiftRemoved.append(schift)
            except (IndexError):
                None
        for s in schiftRemoved:
            pool.schifts.remove(s)
            

match()
print("!!! OSOWA !!!")
print(Osowa.schedule)
print("!!! ŁAPINO !!!")
print(Łapino.schedule)
print("!!! Romanowski !!!")
print(Romanowski.schedule)
print("!!! Romanowska !!!")
print(Romanowska.schedule)
print("!!! Sara !!!")
print(RomanowskaSara.schedule)
print("!!! Iga !!!")
print(RomanowskaIga.schedule)

# Code is not ready.
# Minor fixes required.
# Missing GUI

print("KONIEC")
