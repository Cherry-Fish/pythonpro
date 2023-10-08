import random
print('Welcome to Word Jumble!')
print('Unscramble the letters to make a word.')
word = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
a=random.choice(word)
b=list(a)
random.shuffle(b)
b=''.join(b)

print('Jumbled word: ',b)
guess=input('Your guess: ')
if guess == a:
	print("That's right.")
else:
	print("Sorry, that's not correct. The word was: ",a)

