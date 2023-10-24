Words = {"404":"clueless", "Unintalled" : "being fired."}

while True :
    print("\n\tGeek Translator\n")
    print("\t0 - Quit")
    print("\t1 - Look Up a Geek Term")
    print("\t2 - Add a Geek Term")
    print("\t3 - Redefine a Geek Term")
    print("\t4 - Delete a Geek Term")
    print("\t5 - Words in the dictionary\n")
    num = int(input("Choice : "))

    if num == 0 :
        break

    elif num == 1 :
        f = input("What term  do you want me to translate?: ")

        if f in Words:
            print(f, "means", Words[f])
        
        else:
            print("I have no idea what", f, "is.")
    
    elif num == 2 :
        add = input("Enter characters to add: ")
       
        if add in Words:
            print("Already exists")
       
        else :
            mean = input("Enter the meaning of the characters: ")
            Words[add] = mean
    
    elif num == 3 :
        re = input("Enter the character you want to redefine: ")
        
        if re in Words:
            remean = input("Meaning of character to override: ")
            Words[re] = remean
        
        else :
            print("It does not exist.\n")
    
    elif num == 4 :
        dell = input("Enter the word you want to delete: ")
        
        if dell in Words:
            print("Deleted successfully.")
            del Words[dell]
       
        else :
            print("That word doesn't exist")
    
    elif num == 5 :
        #원래라면 줄바꿈 문자로 나오지만 end=''가 있으면 공백 문자가 삽입된다
        print("\nWords registered in the dictionary>> ",end='')
        
        for key, value in Words.items():
            print("[",key,"]", end = ' ')
        print("\n")
