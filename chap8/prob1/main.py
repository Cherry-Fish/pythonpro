with open("test.txt", "r") as f:
    txt = f.read(1)
    txt1 = f.read(5)
    print(txt)
    print(txt1)
    print()

with open("test.txt", "r") as f:
    f.seek(0)
    txt = f.read()
    print(txt)
    print()

with open("test.txt", "r") as f:
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print()

with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print()

with open("test.txt", "r") as f:
    for line in f:
        print(line)
    print()
n = input('Press the enter key to exit.')
