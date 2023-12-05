class Critter:
    def __init__(self, name, mood_level=5):
        self.name = name
        self.mood_level = mood_level

    def talk(self):
        if self.mood_level >= 8:
            print(f"개좋음")
        elif 5 <= self.mood_level < 8:
            print(f"좋음")
        elif 2 <= self.mood_level < 5:
            print(f"soso")
        else:
            print(f"ㅋㅋ;;")

        
        self.mood_level -= 1

    def feed(self):
        print(f"Thanks ")
        
        self.mood_level += 2

    def play(self):
        print(f"Whee!")
        
        self.mood_level += 3

    def set_mood(self, level):
        self.mood_level = level

    def get_mood(self):
        return self.mood_level


def main():
    critter_name = input("What do you want to name your critter?: ")
    critter = Critter(critter_name)

    while True:
        print("\nCritter Caretaker")
        print("0-Quit")
        print("1-Listen to your critter")
        print("2-Feed your critter")
        print("3-Play with your critter")

        choice = input("Choice: ")

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            critter.talk()
        elif choice == "2":
            critter.feed()
        elif choice == "3":
            critter.play()
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

