class Clinic:
    def __init__(self):
        self.data = {} 
        self.docs = {}  
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]

    def book(self):
        mob, name, doc = input("Mobile: "), input("Name: "), input("Doctor: ")
        if mob in self.data: return print("Already booked")
        
        sched = self.docs.setdefault(doc, {s: 0 for s in self.slots})
        avail = [s for s in self.slots if sched[s] < 3]

        if not avail: return print("Doctor full")
        print("Slots:", avail)
        
        slot = input("Pick Slot: ")
        if slot in avail:
            sched[slot] += 1
            self.data[mob] = {'name': name, 'doc': doc, 'slot': slot}
            print("Booked!")
        else: print("Invalid slot.")

    def view(self):
        print(self.data.get(input("Mobile: "), "Not found"))

    def cancel(self):
        mob = input("Mobile: ")
        if mob in self.data:
            appt = self.data.pop(mob)
            self.docs[appt['doc']][appt['slot']] -= 1
            print("Cancelled")
        else: print("Not found")

sys = Clinic()
while True:
    opt = input("\n1.Book 2.View 3.Cancel 4.Exit: ")
    if opt == '1': sys.book()
    elif opt == '2': sys.view()
    elif opt == '3': sys.cancel()
    elif opt == '4': break








class School:
    def __init__(self):
        self.db = {}
        self.id = 101

    def add(self):
        n = input("Name: ")
        a = int(input("Age 5-18: "))
        c = input("Class 1-12 : ")
        m = input("Mobile 10 digits: ")
        
        if 5 <= a <= 18 and len(m) == 10 and m.isdigit():
            self.db[self.id] = {'Name': n, 'Age': a, 'Class': c, 'Mob': m}
            print(f"Saved ID: {self.id}")
            self.id += 1
        else: print("Invalid Age or Mobile")

    def view(self):
        print(self.db.get(int(input("Enter ID: ")), "Not Found"))

    def update(self):
        sid = int(input("Enter ID: "))
        if sid in self.db:
            opt = input("1.Update Mobile 2.Update Class: ")
            val = input("New Value: ")
            if opt == '1': self.db[sid]['Mob'] = val
            elif opt == '2': self.db[sid]['Class'] = val
            print("Updated")
        else: print("Not Found")

    def remove(self):
        if self.db.pop(int(input("Enter ID: ")), None): print("Removed")
        else: print("Not Found")

s = School()
while True:
    ch = input("\n1.Add 2.View 3.Update 4.Remove 5.Exit: ")
    if ch == '1': s.add()
    elif ch == '2': s.view()
    elif ch == '3': s.update()
    elif ch == '4': s.remove()
    elif ch == '5': break








class BusSystem:
    def __init__(self):
        self.routes = {"Mumbai-Pune": [500, 0], "Delhi-Jaipur": [600, 0]}
        self.tix = {} 
        self.tid = 101

    def book(self):
        # 1. Show Routes
        for r, d in self.routes.items(): print(f"{r}: ₹{d[0]} ({40-d[1]} left)")
        
        # 2. Book
        rt = input("Route: ")
        if rt in self.routes and self.routes[rt][1] < 40:
            self.routes[rt][1] += 1  # Occupy seat
            self.tix[self.tid] = {'Name': input("Name: "), 'Rt': rt, 'Seat': self.routes[rt][1]}
            print(f"Booked! Ticket ID: {self.tid}")
            self.tid += 1
        else: print("Route Invalid or Bus Full")

    def view(self):
        print(self.tix.get(int(input("Ticket ID: ")), "Not Found"))

    def cancel(self):
        tid = int(input("Ticket ID: "))
        if tid in self.tix:
            self.routes[self.tix.pop(tid)['Rt']][1] -= 1
            print("Cancelled!")
        else: print("Not Found")

b = BusSystem()
while True:
    ch = input("\n1.Book 2.View 3.Cancel 4.Exit: ")
    if ch == '1': b.book()
    elif ch == '2': b.view()
    elif ch == '3': b.cancel()
    elif ch == '4': break