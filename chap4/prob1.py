import random as r
mood=r.randrange(3)
print('you are...')
if mood == 0:
	print('😃')
    # happy
elif mood == 1:
	print('🙂')
    # neutral
elif mood == 2:
	print('😂')
    # sad
else:
    print('Illegal mood value!')
print('...today.')
input("\n\nPress the enter key to exit.")
