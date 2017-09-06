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
		wr.writerow(["Name"]+["Email"]+["Password"]+["Profile Link"]+["Credit Card"]+["Month"]+["Year"]+["CVV"]+["Courses"])
		for row in readfile:
			course_Heading=list()
			course_Subtitle=list()
			course_URL=list()
			course_Rating=list()
			course_Voters=list()
			course_Instructor=list()
			course_InstructorURL=list()
			course_Enrolled_Students=list()
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
							htmltext1=urllib.urlopen(tag['href']).read()
							soup1= BeautifulSoup(htmltext1,"lxml")
							elem=soup1.find('h1',{'class': 'clp-lead__title'})
							course_Heading.append(''.join(ch for ch in elem.text if ch.isalnum() or ch ==" ").strip(" "))
							course_Subtitle.append(soup1.find('div',{'class': 'clp-lead__headline'}).text.strip())
							course_URL.append(tag['href'])
							course_Rating.append(soup1.find('span',{'class': 'tooltip-container tooltip--rate-count-container'}).findAll('span')[0]['aria-label'][8:11])
							course_Voters.append(soup1.find('span',{'class': 'tooltip-container tooltip--rate-count-container'}).text.split("(")[1].split(" r")[0])
							iurls=list()
							inames=list()
							for name in soup1.find('span',{'data-purpose': 'instructor-name-top'}).findAll('a',href= True):
								name['href'] = mainsite+name['href']
								iurls.append(name['href'])
								inames.append(name.text.strip())
							course_InstructorURL.append(" and ".join(iurls))
							course_Instructor.append(" and ".join(inames))
							course_Enrolled_Students.append(soup1.find('div',{'data-purpose': 'enrollment'}).text.strip().partition(" ")[0])
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
								htmltext1=urllib.urlopen(tag['href']).read()
								soup1= BeautifulSoup(htmltext1,"lxml")
								elem=soup1.find('h1',{'class': 'clp-lead__title'})
								course_Heading.append(''.join(ch for ch in elem.text if ch.isalnum() or ch ==" ").strip(" "))
								course_Subtitle.append(soup1.find('div',{'class': 'clp-lead__headline'}).text.strip())
								course_URL.append(tag['href'])
								course_Rating.append(soup1.find('span',{'class': 'tooltip-container tooltip--rate-count-container'}).findAll('span')[0]['aria-label'][8:11])
								course_Voters.append(soup1.find('span',{'class': 'tooltip-container tooltip--rate-count-container'}).text.split("(")[1].split(" r")[0])
								iurls=list()
								inames=list()
								for name in soup1.find('span',{'data-purpose': 'instructor-name-top'}).findAll('a',href= True):
									name['href'] = mainsite+name['href']
									iurls.append(name['href'])
									inames.append(name.text.strip())
								course_InstructorURL.append(" and ".join(iurls))
								course_Instructor.append(" and ".join(inames))
								course_Enrolled_Students.append(soup1.find('div',{'data-purpose': 'enrollment'}).text.strip().partition(" ")[0])
							x=x+1
							urls.append(url+'?subscribed_courses='+str(x)+'&key=subscribed_courses')
				wr.writerow([row[0]]+[row[1]]+[row[2]]+[row[3]]+[row[4]]+[row[5]]+[row[6]]+[row[7]]+[','.join(courses)])
				csvfile2= open('/home/Automation/udemy_course_info.csv','w')
				wr2=csvfile2.write
				wr2(";".join(course_Heading)+"\n")
				wr2(";".join(course_Subtitle)+"\n")
				wr2(";".join(course_URL)+"\n")
				wr2(";".join(course_Rating)+"\n")
				wr2(";".join(course_Voters)+"\n")
				wr2(u";".join(course_Instructor).encode('utf-8').strip()+"\n")
				wr2(";".join(course_InstructorURL)+"\n")
				wr2(";".join(course_Enrolled_Students)+"\n")
				wr2("".join(list(";xxx"*len(course_Heading))[1:])+"\n")
				wr2("".join(list(";yyy"*len(course_Heading))[1:])+"\n")
os.system('mpack -s "Udemy CSV: current courses" /home/Automation/udemy_acc2.csv kaustavsmailbox1@gmail.com')
os.system('mpack -s "Udemy CSV: current courses" /home/Automation/udemy_course_info.csv kaustavsmailbox1@gmail.com')
