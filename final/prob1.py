string = input("")
dic ={}
for chr in string:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr]=1
for key, value in sorted(dic.items()):
    print(key, ":", value)

