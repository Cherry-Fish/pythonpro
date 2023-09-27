import random as r
a=r.randrange(1,100)
cnt = 0
print("Welcome to 'Guess My Number'!\n")
print('between 1 and 100.\nTry to guess it in as tew attempts as possilb.')
while True:
	cnt +=1
	n = int(input('Take a guess: '))
	#print(f'{a}')
	if n < a:
		print('Higher...')
	elif n > a:
		print('Lower...')
	elif n == a :
		print(f'You guessed it! The mumber was 15\nAnd it only took you {cnt} trues!')
		break
input("\n\nPress the enter key to exit.")
