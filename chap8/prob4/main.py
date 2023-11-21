import pickle
import shelve


l1 = ['sweet', 'hot', 'dill']
l2 = ['whole', 'spear', 'chip']
l3 = ['Claussen', 'Heinz', 'Vlassic']
with open('test.dat', 'wb') as f:
    pickle.dump(l1, f)
    pickle.dump(l2, f)
    pickle.dump(l3, f)


with open("test.dat", "rb") as f:
    txt1 = pickle.load(f)
    txt2 = pickle.load(f)
    txt3 = pickle.load(f)
    print(txt1)
    print(txt2)
    print(txt3)
print()


with shelve.open("test.dat", flag="n") as pickles:
    pickles["variety"] = ["sweet", "hot", "dill"]
    pickles.sync()
    pickles["shape"] = ['whole', 'spear', 'chip']
    pickles.sync()
    pickles["brand"] = ['Claussen', 'Heinz', 'Vlassic']
    pickles.sync()


with shelve.open("test.dat") as pickles:
    for key in pickles.keys():
        print(key, "-", pickles[key])
