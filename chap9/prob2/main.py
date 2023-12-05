class Critter:
    def __init__(self):
        print("A new critter has been born!")

    def talk(self):
        print("Hi. I'm an instance of class Critter.")


crit1 = Critter()
crit2 = Critter()
print()
crit1.talk()
print()
crit2.talk()
print()
print()
n = input('Press the enter key to exit.')