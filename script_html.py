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
			A.append(row[6])
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
import sys

orig_stdout = sys.stdout
f = open('output.html', 'w')
sys.stdout = f
print("<!DOCTYPE html>")
print("<html>\n")
   
print("   <body>")
print("      <h1>"+"Name: "+A[0]+" Email: "+A[1]+" Password: "+A[2]+"<br>CC No. : "+A[3]+"CC Expiry date: "+A[4]+"/"+A[5][2:]+" CVV: "+A[6]+"</h1>\n")
print("      <h1>"+"<br> MAIN LINKS <br>"+"</h1>\n")
for i in range(7,7+a):
	print("     <a href="+A[i]+">"+A[i]+"<br></a> ")
print("      <h1>"+"<br> MAIN LINKS 2 <br>"+"</h1>\n")
for i in range(7+a,7+a+b):
	print("     <a href="+A[i]+">"+A[i]+"<br></a> ")
print("      <h1>"+"<br> EXTRA LINKS <br>"+"</h1>\n")
for i in range(7+a+b,7+a+b+c):
	print("     <a href="+A[i]+">"+A[i]+"<br></a> ")
print("   </body>\n") 
print("</html>")


sys.stdout = orig_stdout
f.close()
