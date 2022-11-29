import os, pickle
script_dir = os.path.dirname(__file__)

EmployeeList = []
PoolList = []

class LifeGuard:
    def __init__(self, name, surname, PESEL, hourlyRate):
        self.name = name
        self.surname = surname
        self.PESEL = PESEL
        self.hourlyRate = hourlyRate
        self.preferredPool = None
        self.availability = {}
        self.schedule = {}
        self.addLifeGuardToEmployeeList()

    def addLifeGuardToEmployeeList(self):
        EmployeeList.append(self)

    def __del__(self):
        EmployeeList.remove(self)

    def showLifeGuardInfo(self):
        return {"Imię" : self.name,
                "Nazwisko" : self.surname,
                "PESEL" : self.PESEL,
                "Stawka godzinowa" : self.hourlyRate,
                "Preferowany basen" : self.preferredPool}

    def setAvailability(self):
        v = 1
        while v <= 7:      #31
            x = input(str(self.name) + "- Podaj dyspozycyjność w dniu " + str(v) + ". \n0-wolne, 1-pierwsza zmiana, 2-druga zmiana, 3-cały dzień:  ")
            try:
                if int(x) in [0, 1, 2, 3]:
                    self.availability[int(v)] = int(x)
                    v += 1
                else:
                    print("Zły typ danych")
            except:
                print("Zły typ danych")
        fh = open(script_dir + "\\data\\" + str(self.PESEL) + ".dat", "wb")
        pickle.dump(self.availability, fh)
        fh.close


class Pool:
    def __init__(self, name, amountOfLifeGuards):
        self.name = name
        self.amountOfLifeGuards = amountOfLifeGuards
        self.timeShifts = {"start1" : 7,
                        "end1" : 15,
                        "start2" : 15,
                        "end2" : 22}
        self.shifts = (list(range(1001, 1008))) * 2     #1032
        for c in self.shifts:
            i = self.shifts.index(c)
            if i < len(self.shifts) * 0.5:
                self.shifts[i] = c + 100       #str(c) +  "M"
            else:
                self.shifts[i] = c + 200       #str(c) +  "E"        
        a = 1
        shiftsAdded = []
        while a < self.amountOfLifeGuards:            
            for d in self.shifts:
                e = d + (1000 * a)
                shiftsAdded.append(e)
            a += 1
        for f in shiftsAdded:
            self.shifts.append(f)        
        fh = open(script_dir + "\\data\\" + str(self.name) + ".dat", "wb")
        pickle.dump(self.shifts, fh)
        fh.close
        self.schedule = {}
        self.addPoolToPoolList()

    def addPoolToPoolList(self):
        PoolList.append(self)

    def __del__(self):
        PoolList.remove(self)

    def showPoolInfo(self):
        return {"Nazwa" : self.name,
                "Pierwsza zmiana" : "od godz. " + str(self.timeShifts["start1"]) + " do godz. " + str(self.timeShifts["end1"]),
                "Druga zmiana" : "od godz. " + str(self.timeShifts["start2"]) + " do godz. " + str(self.timeShifts["end2"])}

#Osowa = Pool("Osowa", 3)
#print(Osowa.schifts)