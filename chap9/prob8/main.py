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

    def feed(self, food):
        print(f"Thanks")
        # Mood level changes based on the food level
        food.set_critter_level(self)

    def play(self):
        print(f"Whee!")
        # Mood level increases after playing
        self.mood_level += 3

    def set_mood(self, level):
        self.mood_level = level

    def get_mood(self):
        return self.mood_level


class Food:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_level(self):
        return self.level

    def set_critter_level(self, critter):
        critter.mood_level += self.level


def main():
    critter_name = input("What do you want to name your critter?: ")
    critter = Critter(critter_name)

    # 음식 메뉴 생성
    food1 = Food("Kibble", 3)
    food2 = Food("Meat", 5)
    food3 = Food("Veggies", 2)

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
            print("Food Menu:")
            print("1-Kibble")
            print("2-Meat")
            print("3-Veggies")

            food_choice = input("Choose food (1-3): ")
            if food_choice == "1":
                critter.feed(food1)
            elif food_choice == "2":
                critter.feed(food2)
            elif food_choice == "3":
                critter.feed(food3)
            else:
                print("Invalid food choice. Please choose a valid option.")
        elif choice == "3":
            critter.play()
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()

