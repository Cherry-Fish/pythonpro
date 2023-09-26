name = input("Hi. What's your name? ")
old = int(input('And how old are you? '))
weigh = int(input('Okay, last question. How many pounds do you weigh? '))

print("Did you know that you're just 4 in dog years?")

sec = old * 365 * 24 * 60 * 60
print(f"But you're also over {sec} seconds old.")

print('If a small child were trying to get your attention, your name would become: ')

print(3*name)
print(f'Did you know that on the moon you would weigh only {weigh/6} pounds?')
print(f"But on the sun, you'd weigh {weigh*27.1} <but, ah... not for long>.")

input("\n\nPress the enter key to exit.")
