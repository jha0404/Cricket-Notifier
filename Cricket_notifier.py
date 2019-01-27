import os
import time
import requests
import webbrowser
from bs4 import BeautifulSoup
def sound(title):
    os.system("""
              osascript -e 'say "{}"'
              """.format(title))


def notify(title, text,subtitle):
    os.system("""
              osascript -e 'display notification "{}" with title "{}" subtitle "{}" sound name "frog"'
               """.format(text, title,subtitle))

page=requests.get("https://www.cricbuzz.com/cricket-match/live-scores")
soup=BeautifulSoup(page.content,'html.parser')
upper_view=soup.find_all(class_="cb-mat-mnu-itm cb-ovr-flo")
live_list=[]
for x in upper_view:
	t=x.get('title')
	#print(t)
	result_Preview=t.find("Preview",0,len(t))
	result_Live=t.find("Live",0,len(t))
	#print(result_Live)
	result_Toss=t.find("Toss",0,len(t))
	if result_Preview>=0 or result_Toss>=0:
		url=x.get('href')
		y="https://www.cricbuzz.com"
		y=y+url
		page_Preview=requests.get(y)
		soup_Preview=BeautifulSoup(page_Preview.content,'html.parser')
		#print(soup_Preview.prettify())
		etime=soup_Preview.find_all(class_="cb-nav-subhdr cb-font-12")
		#result_time=time[1].get_text()
		a=etime[0].find_all('a');
		venue=a[1].get('title')
		date_time=etime[0].find_all('span')
		date=date_time[-4].get_text()
		time_o=date_time[-3].get_text()
		subtitle="venue:"+" "+venue
		#print(subtitle)
		text="DATE AND TIME:"+" "+date+" "+time_o
		#print(text)
		notify(t,text,subtitle)
		#time.sleep(5)
	elif result_Live>=0:
		live_list=t;
		url1=x.get('href')
		y1="https://www.cricbuzz.com"
		y1=y1+url1
		#webbrowser.open(y1)
		page_live=requests.get(y1)
		soup_live=BeautifulSoup(page_live.content,'html.parser')
		upper=soup_live.find_all(class_="cb-col cb-col-67 cb-scrs-wrp")
		#print(upper[0].prettify())
		eq=upper[0].find_all(class_="cb-min-bat-rw")
		score1=eq[0].get_text()
		eq1=upper[0].find_all(class_="cb-text-inprogress")
		score2=eq1[0].get_text()
		#print(score2)
		notify(t,score1,score2)
		
	else:
		url2=x.get('href')
		y2="https://www.cricbuzz.com"
		y2=y2+url2;
		#webbrowser.open(y2);
		page_not=requests.get(y2);
		soup_not=BeautifulSoup(page_not.content,'html.parser')
		lower=soup_not.find_all(class_="cb-col cb-col-67 cb-scrs-wrp")
		eq2=lower[0].find_all(class_="cb-min-bat-rw")
		score3=eq2[0].get_text()
		#eq3=lower[0].find_all(class_="cb-text-inprogress")
		#score4=eq3[0].get_text()
		#print(score3)
		#print(score4)
		#eq3=soup_not.find_all(class_="cb-text-stump")
		#print(eq3)
		#print(eq3[0].get_text())
		#score4=eq3[0].get_text()
		#print(score4)
		subtitle="CHECK IT ONLINE"
		notify(t,score3,subtitle)

		

#PROJECT OVER THANK YOU
sound("THAT's ALL ABOUT CRICKET TODAY THANK YOU")
#.sleep(5)


		


	    


	
