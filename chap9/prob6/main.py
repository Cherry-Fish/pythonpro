class Critter:
    def __init__(self, name):
        self.__name = name
        print("Hi. I'm", self.name, "\n")

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if new_name == "":
            print("Critter's name can't be an empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    name = property(get_name, set_name)


critter = Critter("Poochie")

while True:
    
    print("Current name:", critter.get_name())

    
    new_name = input("Enter the new name for the critter: ")
    critter = Critter(new_name)
    if new_name != "":
        break
    
    if not new_name:
        
        continue

n = input('Press the enter key to exit.')