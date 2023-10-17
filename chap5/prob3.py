import random
print('Guess the Word!!!')
print("In this game, the program selects a word at random, and the player's objective is to guess the chosen word.\n\n")
word = ("difficult", "banana", "apple", "python", "daegu", "catholic", "university")#튜플로 랜덤하게 보여질 단어들을 만든다.
a = random.choice(word)
wordl = len(a)
end_cnt = 0
cnt = 6
dword = ['_'] * wordl#dword 리스트를 생성하고, 선택된 단어의 길이에 맞게 _을 넣어준다.

print("Lenght of the selected word: ",wordl)
print("Remaining attempts: ",cnt)

while cnt > end_cnt:
	
	#join을 사용해서 dword리스트를 전부 출력한다.
	print("Current guessed word:"," ".join(dword))
	
	guess = input("Guess a letter: ")
	
	#a안에 사용자가 입력한 문자가 있으면 반복문을 실행한다.
	if guess in a:
		#선택된 단어의 길이만큼 반복한다.
		for i in range(wordl):
			#파이썬에서 문자열은 바로 배열처럼 사용이 가능하다.
			if a[i] == guess:
				dword[i] = guess
		#join을 사용해 만들어진 단어를 공백없이 하나의 문자열로 만들어 a와 비교한다.
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

