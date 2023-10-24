import random

Words = ["python", "hang", "apple", "man", "guess"]
words = list(random.choice(Words))
#-으로 전부 초기화
EWords = ["-" for i in range(len(words))]
a = [] #정답이 될 것
YN = False
cnt = 0

hangman = ["",
           "_______",
           "|      ",
           "|      ",
           "|      ",
           "|______"]


while True:
    
    chr = input("Enter your guess: ")
    a.append(chr)
    
    for i in range(len(words)):
        if(words[i] == chr):
            EWords[i] = chr
            YN = True

    if YN == True:
        print("Yes!",chr,"is in the word!")
        YN = False

    else :
        print("No!",chr,"is not in the word!")
        cnt+=1
    
    if cnt == 1:
        hangman[1]="|    | "
    elif cnt == 2:
        hangman[2]="|    O "
    elif cnt == 3:
        hangman[3]="|    + "
    elif cnt == 4:
        hangman[3]="|   -+"
    elif cnt == 5:
        hangman[3]="|   -+-"    
    elif cnt == 6:
        hangman[4]="|   / "
    elif cnt == 7:
        hangman[4]="|   /|"

    for i in range(len(hangman)):
            print(hangman[i]) #메인 스크린 출력

    if cnt == 7 :
        print("\nGame Over!")
        break
    
    print("You've used the following letters:")
    print(a)
    print("\nCurrently entered word: ")
    #EWords출력
    for i in range(len(EWords)):
        print(EWords[i],end=' ')
    print("\n")
    if(EWords == words):
        print("Congratulations, you won.")
        break


    
