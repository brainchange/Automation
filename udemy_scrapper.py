import os
import urlparse
import urllib
import csv
from bs4 import BeautifulSoup
mainsite="https://www.udemy.com"
with open('/home/Automation/udemy_acc1.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	i=0
	for row in readfile:
		i=i+1
		if i!=1:
			print("Inside "+row[0]+"'s profile:")
			print("Collecting Courses, please wait.. ")
			courses=list()
			url=row[3]
			urls=list()
			htmltext=urllib.urlopen(url).read()
			soup= BeautifulSoup(htmltext,"lxml")
			no=len(soup.find('ul',{'class': 'pagination'}).findAll('a'))
			for i in range(1,no):
				urls.append(url+'?subscribed_courses='+str(i)+'&key=subscribed_courses')
			while len(urls)>0: #getting all the urls that are needed to be parsed
				htmltext=urllib.urlopen(urls[0]).read()
				soup= BeautifulSoup(htmltext,"lxml")
				urls.pop(0)
				for tag in soup.find('ul',{'class': 'course-cards-container'}).findAll('a',href= True):
					tag['href'] = mainsite+tag['href']
					print(tag['href'])
					courses.append(tag['href'])
				with open('/home/Automation/udemy_acc2.csv','wb') as csvfile:
					wr=csv.writer(csvfile,delimiter=';')
					wr.writerow([row[0]]+[row[1]]+[row[2]]+[row[3]]+[row[4]]+[row[5]]+[row[6]]+[row[7]]+[','.join(courses)])
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage      
try:
	msg = MIMEMultipart()
	msg.attach(MIMEText(file("/home/Automation/udemy_acc2.csv").read()))
	

	mail = smtplib.SMTP('smtp.gmail.com',587)

	mail.ehlo()
	mail.starttls()
	mail.login("youremailid", "password")
	mail.sendmail("youremailid@gmail.com", "targetemailid@gmail.com", msg.as_string())
	mail.quit
	print "Successfully sent email"
except smtplib.SMTPException,error:
	print str(error)
