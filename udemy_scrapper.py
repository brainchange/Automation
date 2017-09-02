import os
import urlparse
import urllib
import csv
from bs4 import BeautifulSoup
mainsite="https://www.udemy.com"
with open('/home/Automation/udemy_acc1.csv') as csvin:
	readfile=csv.reader(csvin, delimiter=";")
	with open('/home/Automation/udemy_acc2.csv','wb') as csvfile:
		wr=csv.writer(csvfile,delimiter=';')
		j=0
		for row in readfile:
			j=j+1
			if j!=1:
				print("Inside "+row[0]+"'s profile:")
				print("Collecting Courses, please wait.. ")
				courses=list()
				firstcourse=""
				currentcourse=""
				url=row[3]
				urls=list()
				htmltext=urllib.urlopen(url).read()
				soup= BeautifulSoup(htmltext,"lxml")
				x=1
				urls.append(url+'?subscribed_courses='+str(x)+'&key=subscribed_courses')
				while len(urls)>0: #getting all the urls that are needed to be parsed
					htmltext=urllib.urlopen(urls[0]).read()
					soup= BeautifulSoup(htmltext,"lxml")
					urls.pop(0)
					if x==1:
						for tag in soup.find('ul',{'class': 'course-cards-container'}).findAll('a',href= True):
							firstcourse=tag['href']
							break
						for tag in soup.find('ul',{'class': 'course-cards-container'}).findAll('a',href= True):
							tag['href'] = mainsite+tag['href']
							print(tag['href'])
							courses.append(tag['href'])
							courses.append(tag['href'])
						x=x+1
						urls.append(url+'?subscribed_courses='+str(x)+'&key=subscribed_courses')
					else:
						for tag in soup.find('ul',{'class': 'course-cards-container'}).findAll('a',href= True):
							currentcourse=tag['href']
							break
						if(firstcourse!=currentcourse):
							for tag in soup.find('ul',{'class': 'course-cards-container'}).findAll('a',href= True):
								tag['href'] = mainsite+tag['href']
								print(tag['href'])
								courses.append(tag['href'])
							x=x+1
							urls.append(url+'?subscribed_courses='+str(x)+'&key=subscribed_courses')
				wr.writerow([row[0]]+[row[1]]+[row[2]]+[row[3]]+[row[4]]+[row[5]]+[row[6]]+[row[7]]+[','.join(courses)])
os.system('mpack -s "Udemy CSV: current courses" /home/Automation/udemy_acc2.csv akshayg2014@email.iimcal.ac.in')
