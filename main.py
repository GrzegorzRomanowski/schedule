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
Romanowski.preferredPool = Łapino.name
Romanowska.preferredPool = Łapino.name
RomanowskaSara.preferredPool = Łapino.name
RomanowskaIga.preferredPool = Łapino.name
#print(Romanowska.availability)

#print(Osowa.shifts)
#print(Łapino.shifts)

def willing(sp, x, y):
    willingList = []
    for LG in EmployeeList:
        if LG.preferredPool == sp:
            if LG.availability[x] == y or LG.availability[x] == 3:
                willingList.append(LG)            
    return willingList

def willingAll(x, y):
    willingList = []
    for LG in EmployeeList:
        if LG.availability[x] == y or LG.availability[x] == 3:
            willingList.append(LG)            
    return willingList

def match():
# assign LG with correct preferredPool and availability for all day
    for pool in PoolList:
        shiftRemoved = []        
        for shift in pool.shifts:            
            xx = shift % 100
            listOfWilling = willing(pool.name, xx, 3)
            try:
                winner = random.choice(listOfWilling)
                if (((shift + 100)//100)%10) == 1 or (((shift + 100)//100)%10) == 2:
                    shift2 = shift + 100
                elif (((shift - 100)//100)%10) == 1 or (((shift - 100)//100)%10) == 2:
                    shift2 = shift - 100
                if shift not in pool.schedule:
                    winner.schedule[shift] = pool.name
                    pool.schedule[shift] = winner.name
                    winner.availability[xx] = 0
                if shift2 not in pool.schedule:
                    winner.schedule[shift2] = pool.name
                    pool.schedule[shift2] = winner.name
                    winner.availability[xx] = 0                          
                if shift not in shiftRemoved:
                    shiftRemoved.append(shift)
                if shift2 not in shiftRemoved:
                    shiftRemoved.append(shift2)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)
# second try to assign LG with correct preferredPool
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
# third assign LG without correct preferredPool and availability for all day
    for pool in PoolList:
        shiftRemoved = []        
        for shift in pool.shifts:            
            xx = shift % 100
            listOfWilling = willingAll(xx, 3)
            try:
                winner = random.choice(listOfWilling)
                if (((shift + 100)//100)%10) == 1 or (((shift + 100)//100)%10) == 2:
                    shift2 = shift + 100
                elif (((shift - 100)//100)%10) == 1 or (((shift - 100)//100)%10) == 2:
                    shift2 = shift - 100
                if shift not in pool.schedule:
                    winner.schedule[shift] = pool.name
                    pool.schedule[shift] = winner.name
                    winner.availability[xx] = 0
                if shift2 not in pool.schedule:
                    winner.schedule[shift2] = pool.name
                    pool.schedule[shift2] = winner.name
                    winner.availability[xx] = 0                          
                if shift not in shiftRemoved:
                    shiftRemoved.append(shift)
                if shift2 not in shiftRemoved:
                    shiftRemoved.append(shift2)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)
# last assign LG without correct preferredPool
    for pool in PoolList:
        shiftRemoved = []        
        for shift in pool.shifts:            
            if (shift % 1000) < 199:
                yy = 1
            else:
                yy = 2
            xx = shift % 100
            listOfWilling = willingAll(xx, yy)
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

def getFreeShiftsAfterMatch():
    freeShiftsAfterMatch = []
    for pool in PoolList:
        for shift in pool.shifts:
            freeShiftsAfterMatch.append([pool.name, shift])
    return freeShiftsAfterMatch

def unwilling(sp, s):
    unwillingList = []
    for LG in EmployeeList:
        if LG.preferredPool == sp:
            ss = s % 1000
            List = [1000 + ss, 2000 + ss, 3000 + ss, 4000 + ss, 5000 + ss, 6000 + ss, 7000 + ss, 8000 +ss]
            x = 0
            for sss in List:
                if sss in LG.schedule:
                    x += 1
            if x == 0:
                unwillingList.append(LG)
    return unwillingList

def unwillingAll(s):
    unwillingList = []
    for LG in EmployeeList:
        ss = s % 1000
        List = [1000 + ss, 2000 + ss, 3000 + ss, 4000 + ss, 5000 + ss, 6000 + ss, 7000 + ss, 8000 +ss]
        x = 0
        for sss in List:
            if sss in LG.schedule:
                x += 1
        if x == 0:
            unwillingList.append(LG)
    return unwillingList

def force():    #dokończyć
    shiftRemoved = []
    for shift in freeShiftsAfterMatch:  #zrobić standardowo jak w match() czyli bez użycia freeShiftsAfterMatch()
        xx = shift[0]
        yy = shift[1]
        listOfUnwilling = unwilling(xx, yy)
        try:
            winner = random.choice(listOfUnwilling)
            shiftRemoved.append(shift)
            winner.schedule[yy] = xx
            #pool.schedule xxxx
        except (IndexError):
            print("Masz za mało pracowników!")
            break
    for s in shiftRemoved:
        freeShiftsAfterMatch.remove(s)

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

print("KONIEC")