from random import random

total_A_win = 0
total_B_win = 0
elections = 10000
for election in range(0, elections):
	A_win = 0
	B_win = 0
	if random() < .87:   #region 1
		A_win += 1
	else:
		B_win += 1
	if random() < .65:  #region 2
		A_win += 1
	else:
		B_win += 1
	if random() < .17:    #region 3
		A_win += 1
	else:
		B_win += 1
#determine overall election outcome
	if A_win > B_win:
		total_A_win += 1
	else:
		total_B_win += 1
print('A的概率：', total_A_win /elections)
print('B的概率：', total_B_win / elections)
