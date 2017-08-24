import time
import random
import csv
import sys
import os
A=list()
with open('/home/Automation/Acc_Info1.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	i=0
	for row in readfile:
		print("["+str(i)+"]["+'|'.join(row)+"]")
		i=i+1
	print("Select Account: ")
with open('/home/Automation/Acc_Info1.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	x=int(raw_input())
	i=0
	for row in readfile:
		if(x==i):
			A.append(row[0])
			A.append(row[1])
			A.append(row[2])
			A.append(row[3])
			A.append(row[4])
			A.append(row[5])
			break	
		i=i+1