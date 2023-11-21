with open("test.txt","w") as w:
	while True:
		n = input()
		if n=='Q':
			break
		w.write(n+'\n')

with open("test.txt", "r") as f:
	a = f.read()
	print(a)
