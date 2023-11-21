with open("test.txt", "w") as w:
	w.write("Line 1\n")
	w.write("This is line 2\n")
	w.write("That makes this line 3\n")
	print()
with open("test.txt", "w") as W:
	lines = ["Line 1\n", "This is line 2\n", "That makes this line 3\n"]
	W.writelines(lines)

