# This is an app for creating employee schedules based on their availability.

import os
import pickle
import shutil
import tkinter as tk
import random
from tkinter import ttk
script_dir = os.path.dirname(__file__)

# Fonts and font's sizes
f1 = "Nueva"
f2 = "Bookman Old Style"
f3 = "Impact"
f11 = "8"
f22 = "12"
f33 = "20"
f44 = "40"

# !!!!!!!!!!!!!!!!
# Defining Classes
# !!!!!!!!!!!!!!!!

class LifeGuard:
    def __init__(self, name, surname, PESEL, hourlyRate, preferredPool):
        self.name = name
        self.surname = surname
        self.PESEL = PESEL
        self.password = PESEL
        self.hourlyRate = hourlyRate
        self.preferredPool = preferredPool
        self.availability = {}
        self.schedule = {}
        self.addLifeGuardToEmployeeList()

    def addLifeGuardToEmployeeList(self):
        EmployeeList.append(self)
        fh = open(script_dir + "\\data\\LGs\\" + str(self.PESEL) + ".dat", "wb")
        pickle.dump(self, fh)
        fh.close()

    def showLifeGuardInfo(self):
        return {"Imię" : self.name,
                "Nazwisko" : self.surname,
                "PESEL" : self.PESEL,
                "Stawka godzinowa" : self.hourlyRate,
                "Preferowany basen" : self.preferredPool}

    def setAvailability(self):
        global my_radioValues
        my_radioValues = []
        def send():
            j = 0
            for i in my_radioValues:
                g = i.get()
                j += 1
                self.availability[j] = int(g)
            fh = open(script_dir + "\\data\\LGs\\" + str(self.PESEL) + ".dat", "wb")
            pickle.dump(self, fh)
            fh.close()
            filecopied = script_dir + "\\data\\LGs\\" + str(self.PESEL) + ".dat"
            shutil.copy(filecopied, script_dir + "\\data\\Months\\" + currentMonth + "\\LGs")
            ava.destroy()
            lgGUI()
            avaSended = """Dyspozycyjność została wysłana.

Możesz ją zmieniać / wysyłać ponownie dopóki grafik nie zostanie ułożony."""
            warningWindow(avaSended)
        ava = tk.Toplevel()
        ava.title("SCHEDULE   Availability")
        shift = tk.Label(ava, text=self.name + " " +self.surname, font=(f1, f11, "bold"))
        shift.grid(row=0, column=0, padx=2, pady=2)
        shift0 = tk.Label(ava, text='Wolne', font=(f1, f11))
        shift0.grid(row=1, column=0, padx=2, pady=2)
        shift1 = tk.Label(ava, text='Zmiana 1', font=(f1, f11))
        shift1.grid(row=2, column=0, padx=2, pady=2)
        shift2 = tk.Label(ava, text='Zmiana 2', font=(f1, f11))
        shift2.grid(row=3, column=0, padx=2, pady=2)
        shift3 = tk.Label(ava, text='Cały dzień', font=(f1, f11))
        shift3.grid(row=4, column=0, padx=2, pady=2)
        for i in range(1, 32):
            day = tk.Label(ava, text=str(i), fg="White", bg="Black", width=4, font=(f1, f11))
            day.grid(row=0, column=i)
            radioValue = tk.IntVar(value=0)
            radio_0 = tk.Radiobutton(ava, text='0', variable=radioValue, value=0, command=None, state=tk.ACTIVE, font=(f1, f11))
            radio_0.grid(row=1, column=i, sticky=tk.W)
            radio_1 = tk.Radiobutton(ava, text='1', variable=radioValue, value=1, command=None, font=(f1, f11))
            radio_1.grid(row=2, column=i, sticky=tk.W)
            radio_2 = tk.Radiobutton(ava, text='2', variable=radioValue, value=2, command=None, font=(f1, f11))
            radio_2.grid(row=3, column=i, sticky=tk.W)
            radio_3 = tk.Radiobutton(ava, text='12', variable=radioValue, value=3, command=None, font=(f1, f11))
            radio_3.grid(row=4, column=i, sticky=tk.W)
            my_radioValues.append(radioValue)
        buttonSend = tk.Button(ava, text='Wyślij', command=send, width=50, font=(f1, f11))
        buttonSend.grid(row=5, column=0, columnspan=32, padx=2, pady=2)
        labelAva = tk.Label(ava, text=" ", font=(f1, f11))
        if Exist == "EMPTY":
            labelAva.config(text=("Wcześniej podana dyspozycyjność:  " + str(self.availability)))
        if Exist == "NO":
            labelAva.config(text="Podajesz dyspozycyjność pierwszy raz na ten miesiąc")
        labelAva.grid(row=6, column=0, columnspan=32, padx=2, pady=2)
        ava.mainloop()

class Pool:
    def __init__(self, name, amountOfLifeGuards, sss, eee):
        self.name = name
        self.amountOfLifeGuards = amountOfLifeGuards
        self.timeShifts = {"start1" : sss,
                        "end1" : 15,
                        "start2" : 15,
                        "end2" : eee}
        self.shifts = (list(range(1001, 1032))) * 2
        for c in self.shifts:
            i = self.shifts.index(c)
            if i < len(self.shifts) * 0.5:
                self.shifts[i] = c + 100
            else:
                self.shifts[i] = c + 200
        a = 1
        shiftsAdded = []
        while a < self.amountOfLifeGuards:
            for d in self.shifts:
                e = d + (1000 * a)
                shiftsAdded.append(e)
            a += 1
        for f in shiftsAdded:
            self.shifts.append(f)
        self.schedule = {}
        self.addPoolToPoolList()

    def addPoolToPoolList(self):
        PoolList.append(self)
        fh = open(script_dir + "\\data\\Pools\\" + str(self.name) + ".dat", "wb")
        pickle.dump(self, fh)
        fh.close()

    def showPoolInfo(self):
        IP = "Nazwa basenu : " + self.name + "\n \nPierwsza zmiana\nod godz. " + str(
            self.timeShifts["start1"]) + " do godz. " + str(self.timeShifts["end1"]) + "\n \nDruga zmiana\nod godz. " + str(
            self.timeShifts["start2"]) + " do godz. " + str(self.timeShifts["end2"])
        return IP

class Month:
    def __init__(self, name, year, days=31):
        self.name = name
        self.year = year
        self.days = days
        self.addMonthToMonthList()

    def addMonthToMonthList(self):
        MonthList.append(str(self.name + " " + self.year))
        os.makedirs(script_dir + "\\data\\Months\\" + str(self.name + " " + self.year))
        os.makedirs(script_dir + "\\data\\Months\\" + str(self.name + " " + self.year) + "\\LGs")
        os.makedirs(script_dir + "\\data\\Months\\" + str(self.name + " " + self.year) + "\\Pools")
        for dirs, subdirs, files in os.walk(script_dir + "\\data\\Pools"):
            for file in files:
                if file.endswith(".dat"):
                    filename = os.path.join(script_dir + "\\data\\Pools", dirs, file)
                    shutil.copy(filename, script_dir+"\\data\\Months\\"+str(self.name + " " + self.year)+"\\Pools")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Defining Variables, Functions and Data Directory
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


EmployeeList = []
EmployeeList2 = []
PoolList = []
PoolList2 = []
MonthList = []
currentMonth = "!"
currentPool = ""
currentLG = ""

dirs = ["\\data", "\\data\\Months", "\\data\\LGs", "\\data\\Pools"]
welcome = 0
for ddd in dirs:
    try:
        os.makedirs(script_dir + ddd)
        welcome += 1
    except (FileExistsError):
        None

# auxiliary functions "willing..."
def willing(sp, x, y):
    willingList = []
    for LG in EmployeeList2:
        if LG.preferredPool == sp or LG.preferredPool == "":
            if LG.availability[x] == y or LG.availability[x] == 3:
                willingList.append(LG)
    return willingList
def willingAll(x, y):
    willingList = []
    for LG in EmployeeList2:
        if LG.availability[x] == y or LG.availability[x] == 3:
            willingList.append(LG)
    return willingList

# another auxiliary function
def getFreeShiftsAfterMatch():
    freeShiftsAfterMatch = []
    for pool in PoolList2:
        for shift in pool.shifts:
            freeShiftsAfterMatch.append([pool.name, shift])
    return freeShiftsAfterMatch

# main function of whole code
def match():
    global buttonMatch, buttonForce, buttonPublish
# assign LG with correct preferredPool and availability for all day
    for pool in PoolList2:
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
                if shift not in pool.schedule and shift2 not in pool.schedule:
                    winner.schedule[shift] = pool.name
                    winner.schedule[shift2] = pool.name
                    pool.schedule[shift] = winner.name + "\n" + winner.surname
                    pool.schedule[shift2] = winner.name + "\n" + winner.surname
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
    for pool in PoolList2:
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
                pool.schedule[shift] = winner.name + "\n" + winner.surname
                winner.schedule[shift] = pool.name
                winner.availability[xx] -= yy
                shiftRemoved.append(shift)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)
# third assign LG without correct preferredPool and availability for all day
    for pool in PoolList2:
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
                if shift not in pool.schedule and shift2 not in pool.schedule:
                    winner.schedule[shift] = pool.name
                    winner.schedule[shift2] = pool.name
                    pool.schedule[shift] = winner.name + "\n" + winner.surname
                    pool.schedule[shift2] = winner.name + "\n" + winner.surname
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
    for pool in PoolList2:
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
                pool.schedule[shift] = winner.name + "\n" + winner.surname
                winner.schedule[shift] = pool.name
                winner.availability[xx] -= yy
                shiftRemoved.append(shift)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)
    buttonMatch.config(state=tk.DISABLED)
    buttonPublish.config(state=tk.NORMAL)
    freeShifts = getFreeShiftsAfterMatch()
    if len(freeShifts) == 0:
        scheduleResult = """Grafik ułożony w całości.
Możesz go od razu opublikować"""
    else:
        buttonForce.config(state=tk.NORMAL)
        scheduleResult = """Ułożono grafik z pewnymi lukami. Masz teraz 2 opcje:

1) Możesz opuklikować go w obecnej formie z lukami.

2) Wymusić rozdanie zmian, których nikt nie chciał, aby grafik był kompletny.
Z fukcją wymuszania trzeba uważać, bo nie ma ona ograniczeń.
Dopnie grafik za wszelką cene, choćby każdy miał pracować 24/7 przez cały miesiąc.

Jeżeli opublikujesz w obecnej formie i luk okaże się za dużo, lub za mało,
to będzie dostępna możliwość ponownego ułożenia grafiku z użyciem wymuszenia.
Będzie też możliwe wprowadzenie nowego ratownika do systemu i rozdanie mu wolnych zmian."""
    warningWindow(scheduleResult)

# auxiliary functions "unwilling..."
def unwilling(sp, s):
    unwillingList = []
    for LG in EmployeeList2:
        if LG.preferredPool == sp or LG.preferredPool == "":
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
    for LG in EmployeeList2:
        ss = s % 1000
        List = [1000 + ss, 2000 + ss, 3000 + ss, 4000 + ss, 5000 + ss, 6000 + ss, 7000 + ss, 8000 +ss]
        x = 0
        for sss in List:
            if sss in LG.schedule:
                x += 1
        if x == 0:
            unwillingList.append(LG)
    return unwillingList

# forcing to get shifts that wasn't in workers availability (optional)
def force():
    global buttonForce
    forceResult = """Zakończono wymuszanie niechcianych zmian.
Grafik ułożony w całości.
Możesz go opublikować."""
# first force with preferred pool
    for pool in PoolList2:
        shiftRemoved = []
        for shift in pool.shifts:
            listOfUnwilling = unwilling(pool.name, shift)
            try:
                winner = random.choice(listOfUnwilling)
                pool.schedule[shift] = winner.name + "\n" + winner.surname
                winner.schedule[shift] = pool.name
                shiftRemoved.append(shift)
            except (IndexError):
                None
        for s in shiftRemoved:
            pool.shifts.remove(s)
# second force without preferred pool
    for pool in PoolList2:
        shiftRemoved = []
        for shift in pool.shifts:
            listOfUnwillingAll = unwillingAll(shift)
            try:
                winner = random.choice(listOfUnwillingAll)
                pool.schedule[shift] = winner.name + "\n" + winner.surname
                winner.schedule[shift] = pool.name
                shiftRemoved.append(shift)
            except (IndexError):
                forceResult = """Wygląda na to, że masz za mało pracowników!
Wszyscy pracują od rana do nocy przez 7 dni w tygodniu,
a i tak są wolne zmiany do obstawienia"""
                break
        for s in shiftRemoved:
            pool.shifts.remove(s)
    buttonForce.config(state=tk.DISABLED)
    warningWindow(forceResult)

# saving schedules and making it visible to workers
def publish():
    global buttonPublish, buttonMatch, buttonForce
    for pool in PoolList2:
        fh = open(script_dir + "\\data\\Months\\" + currentMonth + "\\Pools\\" + str(pool.name) + ".dat", "wb")
        pickle.dump(pool, fh)
        fh.close()
    for LG in EmployeeList2:
        fh = open(script_dir + "\\data\\Months\\" + currentMonth + "\\LGs\\" + str(LG.PESEL) + ".dat", "wb")
        pickle.dump(LG, fh)
        fh.close()
    adminGUI()
    publishResult = """Opublikowno grafik poprawnie.
Jest już widoczny dla pracowników"""
    warningWindow(publishResult)

# functions used to load and refresh data from binary files
def loadStartData():
    global EmployeeList, PoolList, MonthList
    EmployeeList = []
    PoolList = []
    MonthList = []
    for dirs, subdirs, files in os.walk(script_dir + "\\data\\LGs"):
        for file in files:
            if file.endswith(".dat"):
                filename = os.path.join(script_dir + "\\data\\LGs", dirs, file)
                fh = open(filename, "rb")
                LG = pickle.load(fh)
                EmployeeList.append(LG)
                fh.close()
    for dirs, subdirs, files in os.walk(script_dir + "\\data\\Pools"):
        for file in files:
            if file.endswith(".dat"):
                filename = os.path.join(script_dir + "\\data\\Pools", dirs, file)
                fh = open(filename, "rb")
                pool = pickle.load(fh)
                PoolList.append(pool)
                fh.close()
    try:
        MonthList = os.listdir(script_dir + "\\data\\Months")
    except (FileNotFoundError):
        MonthList = []

def loadScheduleData(m):
    global EmployeeList2, PoolList2
    EmployeeList2 = []
    PoolList2 = []
    for dirs, subdirs, files in os.walk(script_dir + "\\data\\Months\\" + m + "\\LGs"):
        for file in files:
            if file.endswith(".dat"):
                filename = os.path.join(script_dir + "\\data\\Months\\" + m + "\\LGs", dirs, file)
                fh = open(filename, "rb")
                LG = pickle.load(fh)
                EmployeeList2.append(LG)
                fh.close()
    for dirs, subdirs, files in os.walk(script_dir + "\\data\\Months\\" + m + "\\Pools"):
        for file in files:
            if file.endswith(".dat"):
                filename = os.path.join(script_dir + "\\data\\Months\\" + m + "\\Pools", dirs, file)
                fh = open(filename, "rb")
                pool = pickle.load(fh)
                PoolList2.append(pool)
                fh.close()


# !!!!!!!!!!!!!!!
# !!!   GUI   !!!
# !!!!!!!!!!!!!!!


adminPassword = "WOPR"

mainWindow = tk.Tk()
mainWindow.title("SCHEDULE")
logodir = script_dir + "/fotox.ico"
mainWindow.iconbitmap(logodir)

foto = tk.PhotoImage(file="foto3.png")

def whoLogin(h):
    for LG in EmployeeList:
        if h == str(LG.name) + " " + str(LG.surname):
            return LG

def warningWindow(war):
    avaNot = tk.Toplevel()
    avaNot.title("SCHEDULE   Warning")
    warning = tk.Label(avaNot, text=str(war), font=(f2, f33), padx=5, pady=5)
    warning.pack()
    def warDestroy():
        avaNot.destroy()
    warButton = tk.Button(avaNot, text="OK", width=15, font=(f2, f33), command=warDestroy)
    warButton.pack(padx=5, pady=5)
    avaNot.mainloop()

# Login Stuff
def openLogWindow():
    global login, loginList
    def logAdmin():
        global login
        login = entryName.get()
        password = entryPassword.get()
        if login == "ADMIN" and password == adminPassword:
            logInWindow.destroy()
            adminGUI()
            buttonLogin.config(text="Przeloguj się")
            labelLogo.config(text="Witaj\n" + "ADMIN'ie !")
        elif [login, password] in loginList:
            logInWindow.destroy()
            lgGUI()
            buttonLogin.config(text="Przeloguj się")
            labelLogo.config(text="Witaj\n" + login + " !")
        else:
            labelCommunique = tk.Label(logInWindow, text="Zły LOGIN lub HASŁO", font=(f2, f33))
            labelCommunique.grid(row=2, column=1, padx=2, pady=2)
    loadStartData()
    login = "NIKT"
    loginList = []
    for LG in EmployeeList:
        loginList.append([str(LG.name) + " " + str(LG.surname), str(LG.password)])
    logInWindow = tk.Toplevel()
    logInWindow.title("SCHEDULE   Log in")
    logInWindow.geometry("750x150")

    labelName = tk.Label(logInWindow, text="Imię i Nazwisko: ", font=(f2, f33))
    labelName.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
    labelPassword = tk.Label(logInWindow, text="Hasło: ", font=(f2, f33))
    labelPassword.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
    entryName = tk.Entry(logInWindow, font=(f2, f33), width=29)
    entryName.grid(row=0, column=1, padx=2, pady=2)
    entryPassword = tk.Entry(logInWindow, font=(f2, f33), width=29)
    entryPassword.grid(row=1, column=1, padx=2, pady=2)
    button = tk.Button(logInWindow, text="Zaloguj się", font=(f2, f33), command=logAdmin, width=12)
    button.grid(row=2, column=0, padx=2, pady=2)

    logInWindow.mainloop()

logoFrame = tk.Frame(mainWindow)
logoFrame.grid(row=0, column=0, padx=2, pady=2, sticky=tk.NW)
labelLogo = tk.Label(logoFrame, image=foto, width=520, height=250, anchor=tk.NW, text="", fg="yellow", font=(f3, f44), compound=tk.CENTER)
labelLogo.pack(padx=2, pady=2)
logFrame = tk.Frame(mainWindow)
logFrame.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NW)
buttonLogin = tk.Button(logFrame, text="Zaloguj się", font=(f2, f22), command=openLogWindow)
buttonLogin.pack(padx=2, pady=2)

# GUI appearance depends on whether you are an Admin or an Employee
def adminGUI():
    global labelName, settingsButton, functionsFrame, listBoxesFrame, mainFrame, mainFrame2, buttonMatch, buttonForce, buttonPublish
    try:
        labelName.destroy()
        settingsButton.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        functionsFrame.destroy()
        listBoxesFrame.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        mainFrame.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        mainFrame2.destroy()
    except (NameError, UnboundLocalError):
        None

    def openAddMonthwindow():
        def addMonth():
            Monthname = entryMonth.get()
            Year = entryYear.get()
            month = Month(Monthname, Year)
            listBoxMonth.insert(tk.END, (month.name + " " + month.year))
            addMonthResult = "Dodano " + month.name + " " + month.year + " do listy miesięcy."
            addMonthwindow.destroy()
            warningWindow(addMonthResult)

        addMonthwindow = tk.Toplevel()
        addMonthwindow.title("SCHEDULE   Add Month")
        addMonthwindow.geometry("380x150")

        labelMonth = tk.Label(addMonthwindow, text="Miesiąc: ", font=(f2, f33))
        labelMonth.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
        labelYear = tk.Label(addMonthwindow, text="Rok: ", font=(f2, f33))
        labelYear.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
        # labelDays = tk.Label(addMonthwindow, text="Ilość dni w miesiącu: ", font=(f2, f33))
        # labelDays.grid(row=2, column=0, padx=2, pady=2)

        entryMonth = tk.Entry(addMonthwindow, font=(f2, f33), width=12)
        entryMonth.grid(row=0, column=1, padx=2, pady=2)
        entryYear = tk.Entry(addMonthwindow, font=(f2, f33), width=12)
        entryYear.grid(row=1, column=1, padx=2, pady=2)
        # entryDays = tk.Entry(addMonthwindow, font=(f2, f33), width=12)
        # entryDays.grid(row=2, column=1, padx=2, pady=2)

        buttonAddMonth2 = tk.Button(addMonthwindow, text="Dodaj nowy miesiąc", width=21, command=addMonth, font=(f2, f33))
        buttonAddMonth2.grid(row=3, column=0, columnspan=2, padx=2, pady=2)

        addMonthwindow.mainloop()

    def openAddPoolwindow():
        def addPool():
            PoolName = entryPoolName.get()
            AmountOfLifeGuards = int(entryAmountOfLifeGuards.get())
            S1Start = int(entryS1Start.get())
            S2End = int(entryS2End.get())
            sp = Pool(PoolName, AmountOfLifeGuards, S1Start, S2End)
            listBoxPool.insert(tk.END, sp.name)
            addPoolResult = "Dodano " + sp.name + " do listy basenów."
            addPoolwindow.destroy()
            warningWindow(addPoolResult)

        addPoolwindow = tk.Toplevel()
        addPoolwindow.title("SCHEDULE   Add Pool")
        addPoolwindow.geometry("475x320")

        labelPoolName = tk.Label(addPoolwindow, text="Nazwa basenu: ", font=(f2, f33))
        labelPoolName.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
        labelPoolAmountOfLifeGuards = tk.Label(addPoolwindow, text="Liczba ratowników: ", font=(f2, f33))
        labelPoolAmountOfLifeGuards.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
        labelS1Start = tk.Label(addPoolwindow, text="Początek 1 zmiany: ", font=(f2, f33))
        labelS1Start.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)
        labelS1End = tk.Label(addPoolwindow, text="Koniec 1 zmiany: ", font=(f2, f33))
        labelS1End.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)
        labelS2Start = tk.Label(addPoolwindow, text="Początek 2 zmiany: ", font=(f2, f33))
        labelS2Start.grid(row=4, column=0, padx=2, pady=2, sticky=tk.W)
        labelS2End = tk.Label(addPoolwindow, text="Koniec 2 zmiany: ", font=(f2, f33))
        labelS2End.grid(row=5, column=0, padx=2, pady=2, sticky=tk.W)

        entryPoolName = tk.Entry(addPoolwindow, font=(f2, f33), width=10)
        entryPoolName.grid(row=0, column=1, padx=2, pady=2)
        entryAmountOfLifeGuards = tk.Entry(addPoolwindow, font=(f2, f33), width=10)
        entryAmountOfLifeGuards.grid(row=1, column=1, padx=2, pady=2)
        entryS1Start = tk.Entry(addPoolwindow, font=(f2, f33), width=10)
        entryS1Start.grid(row=2, column=1, padx=2, pady=2)
        entryS1End = tk.Label(addPoolwindow, text="15", font=(f2, f33))
        entryS1End.grid(row=3, column=1, padx=2, pady=2, sticky=tk.W)
        entryS2Start = tk.Label(addPoolwindow, text="15", font=(f2, f33))
        entryS2Start.grid(row=4, column=1, padx=2, pady=2, sticky=tk.W)
        entryS2End = tk.Entry(addPoolwindow, font=(f2, f33), width=10)
        entryS2End.grid(row=5, column=1, padx=2, pady=2)

        buttonAddPool2 = tk.Button(addPoolwindow, text="Dodaj Nowy Basen", width=27, command=addPool, font=(f2, f33))
        buttonAddPool2.grid(row=6, column=0, columnspan=2, padx=2, pady=2)

        addPoolwindow.mainloop()

    def openAddLGwindow():
        def addLG():
            LGName = entryLGName.get()
            LGSurname = entryLGSurname.get()
            LGPESEL = entryLGPESEL.get()
            LGHourlyRate = entryLGHourlyRate.get()
            LGPreferredPool = entryLGPreferredPool.get()
            spList = []
            for sp in PoolList:
                spList.append(sp.name)
            if LGPreferredPool in spList or LGPreferredPool == "":
                Employee = LifeGuard(LGName, LGSurname, LGPESEL, LGHourlyRate, LGPreferredPool)
                listBoxLG.insert(tk.END, (Employee.name + " " + Employee.surname))
                addLgResult = "Dodano \"" + Employee.name + " " + Employee.surname + "\" do listy ratowników."
                addLGwindow.destroy()
                warningWindow(addLgResult)
            else:
                labelCommunique2 = tk.Label(addLGwindow, text="Nieprawidłowa nazwa Preferowanego Basenu", font=(f2, f33))
                labelCommunique2.grid(row=6, column=0, columnspan=2, padx=2, pady=2)

        addLGwindow = tk.Toplevel()
        addLGwindow.title("SCHEDULE   Add LifeGuard")
        addLGwindow.geometry("635x320")

        labelLGName = tk.Label(addLGwindow, text="Imię: ", font=(f2, f33))
        labelLGName.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
        labelLGSurname = tk.Label(addLGwindow, text="Nazwisko: ", font=(f2, f33))
        labelLGSurname.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
        labelLGPESEL = tk.Label(addLGwindow, text="PESEL :", font=(f2, f33))
        labelLGPESEL.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)
        labelLGHourlyRate = tk.Label(addLGwindow, text="Stawka godzinowa: ", font=(f2, f33))
        labelLGHourlyRate.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)
        labelLGPreferredPool = tk.Label(addLGwindow, text="Preferowany basen: ", font=(f2, f33))
        labelLGPreferredPool.grid(row=4, column=0, padx=2, pady=2, sticky=tk.W)

        entryLGName = tk.Entry(addLGwindow, font=(f2, f33), width=19)
        entryLGName.grid(row=0, column=1, padx=2, pady=2)
        entryLGSurname = tk.Entry(addLGwindow, font=(f2, f33), width=19)
        entryLGSurname.grid(row=1, column=1, padx=2, pady=2)
        entryLGPESEL = tk.Entry(addLGwindow, font=(f2, f33), width=19)
        entryLGPESEL.grid(row=2, column=1, padx=2, pady=2)
        entryLGHourlyRate = tk.Entry(addLGwindow, font=(f2, f33), width=19)
        entryLGHourlyRate.grid(row=3, column=1, padx=2, pady=2)
        entryLGPreferredPool = tk.Entry(addLGwindow, font=(f2, f33), width=19)
        entryLGPreferredPool.grid(row=4, column=1, padx=2, pady=2)

        buttonAddLG2 = tk.Button(addLGwindow, text="Dodaj Nowego Ratownika", width=36, command=addLG, font=(f2, f33))
        buttonAddLG2.grid(row=5, column=0, columnspan=2, padx=2, pady=2)

        addLGwindow.mainloop()

    def delMonth():
        for i in listBoxMonth.curselection():
            d = listBoxMonth.get(i)
        MonthList.remove(d)
        shutil.rmtree(script_dir + "\\data\\Months\\" + d)
        listBoxMonth.delete(listBoxMonth.curselection())
        delMonthResult = "Usunięto " + d + " razem z grafikami."
        warningWindow(delMonthResult)

    def delPool():
        for i in listBoxPool.curselection():
            d = listBoxPool.get(i)
        for pool in PoolList:
            if pool.name == d:
                PoolList.remove(pool)
                os.remove(script_dir + "\\data\\Pools\\" + str(pool.name) + ".dat")
                listBoxPool.delete(listBoxPool.curselection())
                delPoolResult = "Usunięto " + d + " z listy pracowników."
                warningWindow(delPoolResult)

    def delLG():
        for i in listBoxLG.curselection():
            d = listBoxLG.get(i)
        for LG in EmployeeList:
            if (LG.name + " " + LG.surname) == d:
                EmployeeList.remove(LG)
                os.remove(script_dir + "\\data\\LGs\\" + str(LG.PESEL) + ".dat")
                listBoxLG.delete(listBoxLG.curselection())
                delLgResult = "Usunięto " + d + " z listy basenów."
                warningWindow(delLgResult)

    def showcurrentMonth():
        global PoolList2, EmployeeList2, currentMonth, mainFrame, mainFrame2
        try:
            mainFrame.destroy()
        except (UnboundLocalError, NameError):
            None
        try:
            mainFrame2.destroy()
        except (UnboundLocalError, NameError):
            None
        for i in listBoxMonth.curselection():
            currentMonth = listBoxMonth.get(i)
        if currentMonth != "!":
            buttonCurrentPOOL.config(state=tk.NORMAL, text="Grafik Basenu\nna \"" + currentMonth + "\"")
            buttonCurrentLG.config(state=tk.NORMAL, text="Grafik Ratownika\nna \"" + currentMonth + "\"")
            buttonMatch.config(state=tk.NORMAL, text="Ułóż grafik\nna \"" + currentMonth + "\"")
            buttonForce.config(text="Wymuś rozdanie wolnych zmian\nna \"" + currentMonth + "\"")
            buttonPublish.config(text="Zatwierdź i opublikuj grafik\nna \"" + currentMonth + "\"")
        PoolList2 = []
        EmployeeList2 = []
        loadScheduleData(currentMonth)
        listBoxPool.delete(0, tk.END)
        for pool in PoolList2:
            listBoxPool.insert(tk.END, pool.name)
        listBoxLG.delete(0, tk.END)
        for LG in EmployeeList2:
            listBoxLG.insert(tk.END, (LG.name + " " + LG.surname))

    def showcurrentPool():
        global mainFrame, currentPool
        try:
            mainFrame.destroy()
        except (UnboundLocalError, NameError):
            None
        for i in listBoxPool.curselection():
            p = listBoxPool.get(i)
        for pool in PoolList2:
            if p == pool.name:
                currentPool = pool
        # IP = currentPool.showPoolInfo()
        # PoolInfo.config(text=IP)
        wi = 410
        hi = 805
        mainFrame = tk.Frame(mainWindow, width=wi, height=hi)
        mainFrame.grid(row=0, column=3, rowspan=3, padx=2, pady=2)
        myCanvas = tk.Canvas(mainFrame, width=wi, height=hi)
        myScrollBar = ttk.Scrollbar(mainFrame, orient=tk.VERTICAL, command=myCanvas.yview)
        myScrollBar2 = ttk.Scrollbar(mainFrame, orient=tk.HORIZONTAL, command=myCanvas.xview)
        myScrollBar2.pack(side=tk.BOTTOM, fill=tk.X)
        myCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        myScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        myCanvas.configure(yscrollcommand=myScrollBar.set)
        myCanvas.configure(xscrollcommand=myScrollBar2.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox(tk.ALL)))
        framePool = tk.Frame(myCanvas, width=wi, height=hi)
        myCanvas.create_window((0, 0), window=framePool, anchor=tk.NW)
        z = ["Zmiana 1\nRatownik 1"]
        y = 1
        while y < currentPool.amountOfLifeGuards:
            y += 1
            z.append("Zmiana 1\nRatownik " + str(y))
        z.append("Zmiana 2\nRatownik 1")
        y = 1
        while y < currentPool.amountOfLifeGuards:
            y += 1
            z.append("Zmiana 2\nRatownik " + str(y))
        label0 = tk.Label(framePool, text=currentPool.name, font=(f1, f11, "bold"))
        label0.grid(row=0, column=0, padx=1, pady=1)
        m = 1
        for i in z:
            label1 = tk.Label(framePool, text=i, font=(f1, f11))
            label1.grid(row=0, column=(m), padx=1, pady=1)
            m += 1
        for i in range(1, 32):
            label2 = tk.Label(framePool, text=str(i), font=(f1, f11))
            label2.grid(row=i, column=0, padx=1, pady=1)
        shList = [[""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z)]
        for i in currentPool.schedule.keys():
            j = int((i - (i % 1000)) / 1000)
            if i % 1000 < 199:
                k = j
            elif i % 1000 > 199:
                k = int(j + (0.5 * len(z)))
            x = int(i % 100)
            shList[x - 1][k - 1] = currentPool.schedule[i]
        g = 0
        while g < len(shList):
            h = 0
            while h < len(z):
                button = tk.Button(framePool, text=shList[g][h], command=None, width=12, height=2, font=(f1, f11))
                button.grid(row=(g+1), column=(h+1), padx=1, pady=1)
                if h < 0.5 * len(z):
                    button.config(bg="yellow")
                else:
                    button.config(bg="orange")
                h += 1
            g += 1

    def showcurrentLG():
        global mainFrame2, currentLG
        try:
            mainFrame2.destroy()
        except (UnboundLocalError, NameError):
            None
        for i in listBoxLG.curselection():
            l = listBoxLG.get(i)
        for LG in EmployeeList2:
            if l == (LG.name + " " + LG.surname):
                currentLG = LG
        wi2 = 145
        hi2 = 805
        mainFrame2 = tk.Frame(mainWindow, width=wi2, height=hi2)
        mainFrame2.grid(row=0, column=2, rowspan=3, padx=2, pady=2)
        myCanvas2 = tk.Canvas(mainFrame2, width=wi2, height=hi2)
        myScrollBar3 = ttk.Scrollbar(mainFrame2, orient=tk.VERTICAL, command=myCanvas2.yview)
        myCanvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        myScrollBar3.pack(side=tk.RIGHT, fill=tk.Y)
        myCanvas2.configure(yscrollcommand=myScrollBar3.set)
        myCanvas2.bind('<Configure>', lambda e: myCanvas2.configure(scrollregion=myCanvas2.bbox(tk.ALL)))
        frameLG = tk.Frame(myCanvas2, width=wi2, height=hi2)
        myCanvas2.create_window((0, 0), window=frameLG, anchor=tk.NW)
        label0 = tk.Label(frameLG, text=(currentLG.name + " " + currentLG.surname), font=(f1, f11, "bold"))
        label0.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        label1 = tk.Label(frameLG, text="Zmiana 1", font=(f1, f11))
        label1.grid(row=1, column=1, padx=1, pady=1)
        label2 = tk.Label(frameLG, text="Zmiana 2", font=(f1, f11))
        label2.grid(row=1, column=2, padx=1, pady=1)
        sh1 = [""] * 31
        sh2 = [""] * 31
        for i in currentLG.schedule.keys():
            k = i % 100
            if (i % 1000) < 199:
                sh1[k - 1] = currentLG.schedule[i]
            elif (i % 1000) > 199:
                sh2[k - 1] = currentLG.schedule[i]
        for i in range(1, 32):
            label = tk.Label(frameLG, text=str(i), font=(f1, f11))
            label.grid(row=i+1, column=0, padx=1, pady=1)
            button1 = tk.Button(frameLG, text=sh1[i-1], command=None, width=6, bg="yellow", font=(f1, f11))
            button1.grid(row=i+1, column=1, padx=1, pady=1)
            button2 = tk.Button(frameLG, text=sh2[i-1], command=None, width=6, bg="orange", font=(f1, f11))
            button2.grid(row=i+1, column=2, padx=1, pady=1)

    labelName = tk.Label(logFrame, text="Zalogowano jako:\n" + "ADMIN", font=(f2, f22))
    labelName.pack(padx=2, pady=2)
    listBoxesFrame = tk.Frame(mainWindow)
    listBoxesFrame.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky=tk.NW)
    functionsFrame = tk.Frame(mainWindow)
    functionsFrame.grid(row=2, column=0, columnspan=2, padx=2, pady=2, sticky=tk.N)

    buttonAddMonth = tk.Button(listBoxesFrame, text="Dodaj Nowy Miesiąc", width=19, command=openAddMonthwindow, font=(f2, f22))
    buttonAddMonth.grid(row=0, column=0, padx=2, pady=2)
    buttonDelMonth = tk.Button(listBoxesFrame, text="Usuń Miesiąc", width=19, command=delMonth, font=(f2, f22))
    buttonDelMonth.grid(row=1, column=0, padx=2, pady=2)
    buttonAddLG = tk.Button(listBoxesFrame, text="Dodaj Nowego Ratownika", width=20, command=openAddLGwindow, font=(f2, f22))
    buttonAddLG.grid(row=0, column=1, padx=2, pady=2)
    buttonDelLG = tk.Button(listBoxesFrame, text="Usuń Ratownika", width=20, command=delLG, font=(f2, f22))
    buttonDelLG.grid(row=1, column=1, padx=2, pady=2)
    buttonAddPool = tk.Button(listBoxesFrame, text="Dodaj Nowy Basen", width=19, command=openAddPoolwindow, font=(f2, f22))
    buttonAddPool.grid(row=0, column=2, padx=2, pady=2)
    buttonDelPool = tk.Button(listBoxesFrame, text="Usuń Basen", width=19, command=delPool, font=(f2, f22))
    buttonDelPool.grid(row=1, column=2, padx=2, pady=2)

    list1Frame = tk.Frame(listBoxesFrame)
    list1Frame.grid(row=2, column=0, padx=2, pady=2)
    list2Frame = tk.Frame(listBoxesFrame)
    list2Frame.grid(row=2, column=1, padx=2, pady=2)
    list3Frame = tk.Frame(listBoxesFrame)
    list3Frame.grid(row=2, column=2,padx=2, pady=2)

    listBoxMonth = tk.Listbox(list1Frame, selectmode=tk.SINGLE, font=(f1, f11))
    listBoxMonth.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
    scrollBarMonth = tk.Scrollbar(list1Frame, command=listBoxMonth.yview)
    scrollBarMonth.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    listBoxMonth.config(yscrollcommand=scrollBarMonth.set)
    for m in MonthList:
        listBoxMonth.insert(tk.END, m)

    listBoxLG = tk.Listbox(list2Frame, selectmode=tk.SINGLE, font=(f1, f11))
    listBoxLG.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
    scrollBarLG = tk.Scrollbar(list2Frame, command=listBoxLG.yview)
    scrollBarLG.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    listBoxLG.config(yscrollcommand=scrollBarLG.set)
    for LG in EmployeeList:
        listBoxLG.insert(tk.END, (LG.name + " " + LG.surname))

    listBoxPool = tk.Listbox(list3Frame, selectmode=tk.SINGLE, font=(f1, f11))
    listBoxPool.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=2, pady=2)
    scrollBarPool = tk.Scrollbar(list3Frame, command=listBoxPool.yview)
    scrollBarPool.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    listBoxPool.config(yscrollcommand=scrollBarPool.set)
    for pool in PoolList:
        listBoxPool.insert(tk.END, pool.name)

    buttonCurrentMonth = tk.Button(listBoxesFrame, text="Wybierz miesiąc", width= 19, height=2, command=showcurrentMonth, font=(f2, f22))
    buttonCurrentMonth.grid(row=3, column=0, padx=2, pady=2)
    buttonCurrentLG = tk.Button(listBoxesFrame, text="Grafik Ratownika", width=20, height=2, command=showcurrentLG, state=tk.DISABLED, font=(f2, f22))
    buttonCurrentLG.grid(row=3, column=1, padx=2, pady=2)
    buttonCurrentPOOL = tk.Button(listBoxesFrame, text="Grafik Basenu", width=19, height=2, command=showcurrentPool, state=tk.DISABLED, font=(f2, f22))
    buttonCurrentPOOL.grid(row=3, column=2, padx=2, pady=2)

    spacesLabel = tk.Label(functionsFrame, text=" ", font=(f2, f22))
    spacesLabel.pack(padx=2, pady=2)
    buttonMatch = tk.Button(functionsFrame, text="Ułóż grafik", width=27, height=2, command=match, state=tk.DISABLED, font=(f2, f22))
    buttonMatch.pack(padx=2, pady=2)
    buttonForce = tk.Button(functionsFrame, text="Wymuś rozdanie wolnych zmian", width=27, height=2, command=force, state=tk.DISABLED, font=(f2, f22))
    buttonForce.pack(padx=2, pady=2)
    buttonPublish = tk.Button(functionsFrame, text="Zatwierdź i opublikuj grafik", width=27, height=2, command=publish, state=tk.DISABLED, font=(f2, f22))
    buttonPublish.pack(padx=2, pady=2)

def lgGUI():
    global labelName, settingsButton, functionsFrame, listBoxesFrame, mainFrame, mainFrame2, buttonAvailability, buttonCurrentLG
    try:
        labelName.destroy()
        settingsButton.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        functionsFrame.destroy()
        listBoxesFrame.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        mainFrame.destroy()
    except (NameError, UnboundLocalError):
        None
    try:
        mainFrame2.destroy()
    except (NameError, UnboundLocalError):
        None

    def ScheduleExist():
        global Exist
        Exist = ""
        LoGin2 = whoLogin(login)
        try:
            fhExist = open(script_dir + "\\data\\Months\\" + currentMonth + "\\LGs\\" + LoGin2.PESEL + ".dat", "rb")
            scheduleExist = pickle.load(fhExist)
            fhExist.close()
            if len(scheduleExist.schedule) > 0:
                Exist = "YES"
            else:
                Exist = "EMPTY"
        except (FileNotFoundError):
            Exist = "NO"

    def showcurrentMonth():
        global PoolList2, EmployeeList2, currentMonth, mainFrame, mainFrame2
        try:
            mainFrame.destroy()
        except (UnboundLocalError, NameError):
            None
        try:
            mainFrame2.destroy()
        except (UnboundLocalError, NameError):
            None
        buttonCurrentPOOL.config(state=tk.DISABLED)
        buttonCurrentLG.config(state=tk.DISABLED)
        buttonCurrentLG.config(state=tk.DISABLED)
        for i in listBoxMonth.curselection():
            currentMonth = listBoxMonth.get(i)
        ScheduleExist()
        if currentMonth != "!":
            if Exist == "YES":
                buttonCurrentPOOL.config(state=tk.NORMAL, text="Grafik Basenu\nna \"" + currentMonth + "\"")
                buttonCurrentLG.config(state=tk.NORMAL, text="Wyświetl swój grafik\nna \"" + currentMonth + "\"")
                buttonAvailability.config(text="Podaj dyspozycyjności\nna \"" + currentMonth + "\"")
            elif Exist == "EMPTY":
                buttonCurrentPOOL.config(state=tk.NORMAL, text="Grafik Basenu\nna \"" + currentMonth + "\"")
                buttonCurrentLG.config(text="Twój grafik \nna \"" + currentMonth + "\" jest pusty")
                buttonAvailability.config(state=tk.NORMAL, text="Podaj dyspozycyjności\nna \"" + currentMonth + "\"")
            elif Exist == "NO":
                buttonCurrentPOOL.config(state=tk.NORMAL, text="Grafik Basenu\nna \"" + currentMonth + "\"")
                buttonCurrentLG.config(text="Wyświetl swój grafik\nna \"" + currentMonth + "\"")
                buttonAvailability.config(state=tk.NORMAL, text="Podaj dyspozycyjności\nna \"" + currentMonth + "\"")
        PoolList2 = []
        EmployeeList2 = []
        loadScheduleData(currentMonth)
        listBoxPool.delete(0, tk.END)
        for pool in PoolList2:
            listBoxPool.insert(tk.END, pool.name)

    def showcurrentPool():
        global mainFrame, currentPool
        try:
            mainFrame.destroy()
        except (UnboundLocalError, NameError):
            None
        for i in listBoxPool.curselection():
            p = listBoxPool.get(i)
        for pool in PoolList2:
            if p == pool.name:
                currentPool = pool
        IP = currentPool.showPoolInfo()
        PoolInfo.config(text=IP)
        wi = 410
        hi = 805
        mainFrame = tk.Frame(mainWindow, width=wi, height=hi)
        mainFrame.grid(row=0, column=3, rowspan=2, padx=2, pady=2)
        myCanvas = tk.Canvas(mainFrame, width=wi, height=hi)
        myScrollBar = ttk.Scrollbar(mainFrame, orient=tk.VERTICAL, command=myCanvas.yview)
        myScrollBar2 = ttk.Scrollbar(mainFrame, orient=tk.HORIZONTAL, command=myCanvas.xview)
        myScrollBar2.pack(side=tk.BOTTOM, fill=tk.X)
        myCanvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        myScrollBar.pack(side=tk.RIGHT, fill=tk.Y)
        myCanvas.configure(yscrollcommand=myScrollBar.set)
        myCanvas.configure(xscrollcommand=myScrollBar2.set)
        myCanvas.bind('<Configure>', lambda e: myCanvas.configure(scrollregion=myCanvas.bbox(tk.ALL)))
        framePool = tk.Frame(myCanvas, width=wi, height=hi)
        myCanvas.create_window((0, 0), window=framePool, anchor=tk.NW)
        z = ["Zmiana 1\nRatownik 1"]
        y = 1
        while y < currentPool.amountOfLifeGuards:
            y += 1
            z.append("Zmiana 1\nRatownik " + str(y))
        z.append("Zmiana 2\nRatownik 1")
        y = 1
        while y < currentPool.amountOfLifeGuards:
            y += 1
            z.append("Zmiana 2\nRatownik " + str(y))
        label0 = tk.Label(framePool, text=currentPool.name, font=(f1, f11, "bold"))
        label0.grid(row=0, column=0, padx=1, pady=1)
        m = 1
        for i in z:
            label1 = tk.Label(framePool, text=i, font=(f1, f11))
            label1.grid(row=0, column=(m), padx=1, pady=1)
            m += 1
        for i in range(1, 32):
            label2 = tk.Label(framePool, text=str(i), font=(f1, f11))
            label2.grid(row=i, column=0, padx=1, pady=1)
        shList = [[""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z), [""] * len(z),
                  [""] * len(z)]
        for i in currentPool.schedule.keys():
            j = int((i - (i % 1000)) / 1000)
            if i % 1000 < 199:
                k = j
            elif i % 1000 > 199:
                k = int(j + (0.5 * len(z)))
            x = int(i % 100)
            shList[x - 1][k - 1] = currentPool.schedule[i]
        g = 0
        while g < len(shList):
            h = 0
            while h < len(z):
                button = tk.Button(framePool, text=shList[g][h], command=None, width=12, height=2, font=(f1, f11))
                button.grid(row=(g+1), column=(h+1), padx=1, pady=1)
                if h < 0.5 * len(z):
                    button.config(bg="yellow")
                else:
                    button.config(bg="orange")
                h += 1
            g += 1

    def showcurrentLG():
        global mainFrame2, currentLG
        try:
            mainFrame2.destroy()
        except (UnboundLocalError, NameError):
            None
        for LG in EmployeeList2:
            if login == (LG.name + " " + LG.surname):
                currentLG = LG
        wi2 = 145
        hi2 = 805
        mainFrame2 = tk.Frame(mainWindow, width=wi2, height=hi2)
        mainFrame2.grid(row=0, column=2, rowspan=2, padx=2, pady=2)
        myCanvas2 = tk.Canvas(mainFrame2, width=wi2, height=hi2)
        myScrollBar3 = ttk.Scrollbar(mainFrame2, orient=tk.VERTICAL, command=myCanvas2.yview)
        myCanvas2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        myScrollBar3.pack(side=tk.RIGHT, fill=tk.Y)
        myCanvas2.configure(yscrollcommand=myScrollBar3.set)
        myCanvas2.bind('<Configure>', lambda e: myCanvas2.configure(scrollregion=myCanvas2.bbox(tk.ALL)))
        frameLG = tk.Frame(myCanvas2, width=wi2, height=hi2)
        myCanvas2.create_window((0, 0), window=frameLG, anchor=tk.NW)
        label0 = tk.Label(frameLG, text=(currentLG.name + " " + currentLG.surname), font=(f1, f11, "bold"))
        label0.grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        label1 = tk.Label(frameLG, text="Zmiana 1", font=(f1, f11))
        label1.grid(row=1, column=1, padx=1, pady=1)
        label2 = tk.Label(frameLG, text="Zmiana 2", font=(f1, f11))
        label2.grid(row=1, column=2, padx=1, pady=1)
        sh1 = [""] * 31
        sh2 = [""] * 31
        for i in currentLG.schedule.keys():
            k = i % 100
            if (i % 1000) < 199:
                sh1[k - 1] = currentLG.schedule[i]
            elif (i % 1000) > 199:
                sh2[k - 1] = currentLG.schedule[i]
        for i in range(1, 32):
            label = tk.Label(frameLG, text=str(i), font=(f1, f11))
            label.grid(row=i+1, column=0)
            button1 = tk.Button(frameLG, text=sh1[i-1], command=None, width=6, bg="yellow", font=(f1, f11))
            button1.grid(row=i+1, column=1, padx=1, pady=1)
            button2 = tk.Button(frameLG, text=sh2[i-1], command=None, width=6, bg="orange", font=(f1, f11))
            button2.grid(row=i+1, column=2, padx=1, pady=1)

    def openSettingsWindow():
        def applySettings():
            setOldPassword = entrySetOldPassword.get()
            setNewPassword = entrySetNewPassword.get()
            setNewPassword2 = entrySetNewPassword2.get()
            setPrefPool = entrySetPrefPool.get()
            spList = []
            for sp in PoolList:
                spList.append(sp.name)
            if setOldPassword == settedLG.password and setNewPassword != setOldPassword and setNewPassword == setNewPassword2:
                if setPrefPool in spList or setPrefPool == "":
                    settedLG.password = setNewPassword
                    settedLG.preferredPool = setPrefPool
                    settedLG.addLifeGuardToEmployeeList()
                    EditLgResult = """Zapisano zmiany.
UWAGA !!!
Jeżeli zmieniałeś preferowany basen i masz wysłaną już dyspozycyjność na miesiąc,
na który nie ma ułożonego jeszcze grafiku, to wyślij dyspozycyjność ponownie!
W przeciwnym wypadku grafik będzie ułożony przy założeniu, że twoim preferowanym
basenem jest ten, który był w momencie wysyłania dyspozycyjności!"""
                    settingsWindow.destroy()
                    warningWindow(EditLgResult)
                else:
                    labelCommunique3 = tk.Label(settingsWindow, text="Nieprawidłowa nazwa Basenu", font=(f2, f33))
                    labelCommunique3.grid(row=4, column=1, padx=2, pady=2)
            else:
                labelCommunique3 = tk.Label(settingsWindow, text="Nieprawidłowe hasło", font=(f2, f33))
                labelCommunique3.grid(row=4, column=1, padx=2, pady=2)



        for LG in EmployeeList:
            if login == (LG.name + " " + LG.surname):
                settedLG = LG
        settingsWindow = tk.Toplevel()
        settingsWindow.title("SCHEDULE   Settings")
        settingsWindow.geometry("770x230")

        labelSetPrefPool = tk.Label(settingsWindow, text="Preferowany basen: ", font=(f2, f33))
        labelSetPrefPool.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
        labelSetOldPassword = tk.Label(settingsWindow, text="Stare Hasło: ", font=(f2, f33))
        labelSetOldPassword.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
        labelSetNewPassword = tk.Label(settingsWindow, text="Nowe Hasło: ", font=(f2, f33))
        labelSetNewPassword.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)
        labelSetNewPassword2 = tk.Label(settingsWindow, text="Powtórz Nowe Hasło: ", font=(f2, f33))
        labelSetNewPassword2.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)

        entrySetPrefPool = tk.Entry(settingsWindow, font=(f2, f33), width=27)
        entrySetPrefPool.grid(row=0, column=1, padx=2, pady=2)
        entrySetPrefPool.insert(0, settedLG.preferredPool)
        entrySetOldPassword = tk.Entry(settingsWindow, font=(f2, f33), width=27)
        entrySetOldPassword.grid(row=1, column=1, padx=2, pady=2)
        entrySetNewPassword = tk.Entry(settingsWindow, font=(f2, f33), width=27)
        entrySetNewPassword.grid(row=2, column=1, padx=2, pady=2)
        entrySetNewPassword2 = tk.Entry(settingsWindow, font=(f2, f33), width=27)
        entrySetNewPassword2.grid(row=3, column=1, padx=2, pady=2)

        applySetButton = tk.Button(settingsWindow, text="Zatwierdź zmiany", command=applySettings, font=(f2, f33), width=16)
        applySetButton.grid(row=4, column=0, padx=2, pady=2)

        settingsWindow.mainloop()

    labelName = tk.Label(logFrame, text="Zalogowano jako:\n" + login, font=(f2, f22))
    labelName.pack(padx=2, pady=2)
    settingsButton = tk.Button(logFrame, text="Ustawienia", command=openSettingsWindow, font=(f2, f22))
    settingsButton.pack(padx=2, pady=2)

    functionsFrame = tk.Frame(mainWindow)
    functionsFrame.grid(row=1, column=0, columnspan=2, padx=2, pady=2, sticky=tk.NW)
    functionFrame1 = tk.Frame(functionsFrame)
    functionFrame1.grid(row=0, column=0, padx=2, pady=2, sticky=tk.NW)
    functionFrame2 = tk.Frame(functionsFrame)
    functionFrame2.grid(row=0, column=1, padx=2, pady=2, sticky=tk.NE)
    functionFrame3 = tk.Frame(functionsFrame)
    functionFrame3.grid(row=1, column=0, padx=2, pady=2, sticky=tk.NW)
    functionFrame4 = tk.Frame(functionsFrame)
    functionFrame4.grid(row=1, column=1, padx=2, pady=2, sticky=tk.NE)

    pickMonth = tk.Label(functionFrame1, text="Wybierz miesiąc: ", anchor=tk.W, font=(f2, f22))
    pickMonth.pack(anchor=tk.W, padx=2, pady=2)
    list1Frame = tk.Frame(functionFrame1)
    list1Frame.pack(anchor=tk.W, padx=2, pady=2)
    listBoxMonth = tk.Listbox(list1Frame, selectmode=tk.SINGLE, font=(f1, f11))
    listBoxMonth.pack(side=tk.LEFT, expand=1, fill=tk.BOTH, padx=2, pady=2)
    scrollBarMonth = tk.Scrollbar(list1Frame, command=listBoxMonth.yview)
    scrollBarMonth.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    listBoxMonth.config(yscrollcommand=scrollBarMonth.set)
    for m in MonthList:
        listBoxMonth.insert(tk.END, m)
    buttonCurrentMonth = tk.Button(functionFrame1, text="Wybierz zaznaczony miesiąc", width=23, height=2, command=showcurrentMonth, font=(f2, f22))
    buttonCurrentMonth.pack(anchor=tk.W, padx=2, pady=2)

    def AvaPressed():
        LoGin2 = whoLogin(login)
        LoGin2.setAvailability()
    buttonAvailability = tk.Button(functionFrame2, text="Podaj dyspozycyjność", width=23, height=2, command=AvaPressed, state=tk.DISABLED, font=(f2, f22))
    buttonAvailability.pack(padx=2, pady=2)
    buttonCurrentLG = tk.Button(functionFrame2, text="Wyświetl swój grafik", width=23, height=2, command=showcurrentLG, state=tk.DISABLED, font=(f2, f22))
    buttonCurrentLG.pack(padx=2, pady=2)

    pickPool = tk.Label(functionFrame3, text="\nWybierz basen: ", anchor=tk.W, font=(f2, f22))
    pickPool.pack(anchor=tk.W, padx=2, pady=2)
    list3Frame = tk.Frame(functionFrame3)
    list3Frame.pack(anchor=tk.W, padx=2, pady=2)
    listBoxPool = tk.Listbox(list3Frame, selectmode=tk.SINGLE, font=(f1, f11))
    listBoxPool.pack(side=tk.LEFT, expand=1, fill=tk.BOTH, padx=2, pady=2)
    scrollBarPool = tk.Scrollbar(list3Frame, command=listBoxPool.yview)
    scrollBarPool.pack(side=tk.RIGHT, fill=tk.Y, padx=2, pady=2)
    listBoxPool.config(yscrollcommand=scrollBarPool.set)
    for pool in PoolList:
        listBoxPool.insert(tk.END, pool.name)
    buttonCurrentPOOL = tk.Button(functionFrame3, text="Grafik Basenu", width=23, height=2, command=showcurrentPool, state=tk.DISABLED, font=(f2, f22))
    buttonCurrentPOOL.pack(anchor=tk.W, padx=2, pady=2)

    PoolInfoNewLines = tk.Label(functionFrame4, text=" \n  ", font=(f2, f22))
    PoolInfoNewLines.pack(padx=2, pady=2)
    PoolInfo = tk.Label(functionFrame4, text="", font=(f2, f22))
    PoolInfo.pack(padx=2, pady=2)

# Welcome Window if App is running first time
if welcome != 0:
    ww = """ Wygląda na to, że uruchamiasz program po raz pierwszy
oraz nie skorzystałeś/aś z dołączonej paczki przykładowych danych.
Twoja baza danych basenów, ratowników oraz grafików jest pusta.
Dla wygodniejszej pracy z programem zalecane jest stworzenie danych w następującej kolejności:
1) BASENY   -->   2) RATOWNICY   -->   3) MIESIĄCE
Gdybyś jednak chciał/a skorzystać z dołączonej przykładowej lokalnej bazy danych
podmień folder "data" wewnątrz folderu, w którym znajduje się przed chwilą uruchomiony plik."""
    warningWindow(ww)

mainWindow.mainloop()
