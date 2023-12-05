class Critter:
    total = 0

    def __init__(self, name):
        print("A new critter has been born!")
        Critter.total += 1

    @staticmethod
    def status():
        print("Total critters", Critter.total)

print(Critter.total)

crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

print(crit1.total)

n = input('Press the enter key to exit.')