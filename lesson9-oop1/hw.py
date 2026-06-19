class Robot:
    def __init__(self, name, company, madeBy, madeIn, work):
        self.name = name
        self.company = company
        self.madeBy = madeBy
        self.madeIn = madeIn
        self.work = work

    def introduction(self):
        print(f"Hello Human! I am {self.name} from The {self.company}, made by {self.madeBy} in {self.madeIn}. I am the best Robo-Product out there if you need any help in {self.work}.")

Norm = Robot("Norm", "Orphic", "Mr. Nabhya", "India", " maintaining House-hold cleanliness")

Norm.introduction()
    