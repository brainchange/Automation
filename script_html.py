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
print("How many courses to choose from main link, main2 and extra links? (example: 2 1 3) ")
a,b,c=map(int,raw_input().strip(" ").split(" "))
with open('/home/Automation/main_links.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	for row in readfile:
		n=list()
		i=0
		no=len(row)
		while(i<a):
			x=random.randint(0,no-1)
			if (x not in n):
				A.append(row[x])
				n.append(x)
			i=i+1
with open('/home/Automation/main_links2.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	for row in readfile:
		n=list()
		i=0
		no=len(row)
		while(i<b):
			x=random.randint(0,no-1)
			if (x not in n):
				A.append(row[x])
				n.append(x)
			i=i+1
with open('/home/Automation/extra_links.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	for row in readfile:
		n=list()
		i=0
		no=len(row)
		while(i<c):
			x=random.randint(0,no-1)
			if (x not in n):
				A.append(row[x])
				n.append(x)
			i=i+1
from string import Template
print("<!DOCTYPE html>")
print("<html>\n")
   
print("<body>
      <h1>Hello World!</h1>
print("   </body>\n") 
print("</html>")