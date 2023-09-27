import random as r
HHP=r.randrange(50,100)
MHP=r.randrange(50,100)
print(f'here HP: {HHP}, monster HP: {MHP}')
cnt =0
while True:
	cnt += 1
	Hatt=r.randrange(-10,20)
	Matt=r.randrange(-10,20)
	if Hatt>0 and Matt>0:
		MtH=HHP-Matt
		HtM=MHP-Hatt
		print(f'here(Hp:{MtH}, attck:{Hatt}) success <-> monster(HP:{HtM}, attck:{Matt}) success')
		HHP=MtH
		MHP=HtM
	elif Hatt>0 and Matt<=0:
		HtM=MHP-Hatt
		MtH=HHP-0
		print(f'here(Hp:{MtH}, attck:{Hatt}) success <-> monster(HP:{HtM}, attck:{Matt}) faill')
		HHP=MtH
		MHP=HtM
	elif Hatt<=0 and Matt>0:
		HtM=MHP-0
		MtH=HHP-Matt
		print(f'here(Hp:{MtH}, attck:{Hatt}) faill <-> monster(HP:{HtM}, attck:{Matt}) success')
		HHP=MtH
		MHP=HtM
	elif Hatt<=0 and Matt<=0:
		MtH=HHP-Matt
		HtM=MHP-Hatt
		print(f'here(Hp:{MtH}, attck:{Hatt}) faill <-> monster(HP:{HtM}, attck:{Matt}) faill')
	if HHP<=0:
		print('------------------------------------------------------------')
		print(f'Total phase: {cnt}\nMonster Win!!!')
		break
	elif MHP<=0:
		print('------------------------------------------------------------')
		print(f'Total phase: {cnt}\nHere Win!!!')
		break
