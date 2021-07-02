import time
import sys
import math
import datetime
import time
import random
import string

#Get number of records from command lie
num = input("Input the number (1 to 2,000,000) of records (or enter 'S' for sample data) : ")

char_set = string.ascii_uppercase
number_set = string.digits

file = open("luckydraw_result.csv", "w")

if num == 'S':
	file.write("HKID,MOBILE,NAME" + '\n')
	file.write('A4444444,90000000,RPJXNEAQWCAUJFY' + '\n')
	file.write('A3333333,80000000,PWGHFSIMHACFUSD' + '\n')
	file.write('A8888888,20000000,EQOKCEAGDFHRFZX' + '\n')
	file.write('A1111111,30000000,ACBJKXYKIRZNBNN' + '\n')
	file.write('A4444444,90000000,UCAIBZWHKRPPGVQ' + '\n')
	file.write('A8888888,70000000,QPFOOSLQLJASGPE' + '\n')
	file.write('A2222222,60000000,PPHXAQQCVFYWYIH' + '\n')
	file.write('A9999999,10000000,VWKRRPZPBBUYTDH' + '\n')
	file.write('A5555555,50000000,NGVJYSBGJKZECPB' + '\n')
	file.write('A3333333,90000000,ZVYFKJAIGVHNSVA' + '\n')
	file.write('A8888888,70000000,ZVYFKJAIGVHNSVA' + '\n')
else :
	file.write("HKID,MOBILE,NAME" + '\n')

	for i in range(int(num)):
		random_char = ''.join(random.sample(char_set*1, 1))
		random_number = ''.join(random.sample(number_set*5, 5))
		random_mobile = ''.join(random.sample(number_set*3, 3))
		random_name = ''.join(random.sample(char_set*15, 15))
		file.write(random_char + random_number + ',' + random_mobile + ',' + random_name + '\n')

file.close()
