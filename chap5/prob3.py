import random
print('Guess the Word!!!')
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
word = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")
a = random.choice(word)
wordl = len(a)
end_cnt = 0
cnt = 6
dword = ['_'] * wordl

print("Lenght of the selected word: ",wordl)
print("Remaining attempts: ",cnt)

while cnt > end_cnt:
    
    print("Current guessed word:"," ".join(dword))

    guess = input("Guess a letter: ").lower()
    
    if guess in a:
        for i in range(wordl):
            if a[i] == guess:
                dword[i] = guess
        if ''.join(dword) == a:
            print("Congratulations! You guessed the word: ",a)
            break
        print("Remaining attempts: ",cnt)
    else:
        print("Incorrect guess.")
        cnt -= 1
        if cnt == end_cnt:
            continue
        print("Remaining attempts: ",cnt)

if cnt == end_cnt:
    print("You've used up all your attempts. The correct word was: ",a)

