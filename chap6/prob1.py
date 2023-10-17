print('Your items:')
inven = ["sword", "armor", "shield", "healing potion"]
for item in inven:
	print(item)
input("\nPress the enter key to continue.")
print("You have", len(inven), "items in your possession.")
input("\nPress the enter key to continue.")
if "healing potion" in inven:
	print('You will live to fight another day.')
n = int(input('Enter the index number for an item in inventory: '))
print(f"At index {n} is", inven[n])
a = int(input('Enter the index number to begin a slice: '))
b = int(input('Enter the index number to end the slice: '))
print(f"inventory[ {a} : {b} ]", inven[a:b])
input("\nPress the enter key to continue.")
chest = ("gold", "gems")
print('You find a chest.	It contains:')
print (chest)
print('You add the contents of the chest to your inventory.')
inven += chest
print('Your inventory is now: ')
print (inven)
input("\nPress the enter key to continue.")
print('You teade your sword for a crossbow.')
inven[0]="crossbow"
print('Your inventory is now:')
print(inven)
input("\nPress the enter key to continue.")
print('You use your gold and gems to buy an orb of future telling.')
inven[4]="orb of future telling"
del inven[5]
print('Your inventory is now:')
print(inven)
input("\nPress the enter key to continue.")
print('In a great battle, your shield is destroyed.')
print('Your inventory is now:')
del inven[2]
print(inven)
input("\nPress the enter key to continue.")
print('Your crossbow and armor are stolen by thieves.')
print('Your inventory is now:')
del inven[:2]
print(inven)

input("\n\nPress the enter key to exit.")
