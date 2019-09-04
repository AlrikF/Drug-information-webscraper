from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import time

filename="product_info.csv"
f=open(filename,"w")
headers=("Name    " +" ," +"Information")
f.write(headers +"\n")
change=65
my_url ='https://www.medindia.net/doctors/drug_information/home.asp?alpha=A'

for i in range(26):
    
    #opening up connection ,grabbing the page 
    uClient=ureq(my_url)
    page_html= uClient.read()
    uClient.close()

    page_soup=soup(page_html,"html.parser")
    containers=page_soup.findAll("li",{"class":"list-item"})

    
    time.sleep(4)

    for container in containers:
        name=container.h4.text.strip()
        length=len(name)
        info=container.text.strip()
        info=info[length:].replace(",","")
        info=info.strip()
        info=info.replace("\u03b2","Beta")
        info=info.replace("\x92","")
        info=info.replace("\x94","")
        info=info.replace("\x96","")
        info=info.replace("\u03b1","Alpha")
        info=info.replace("\x91"," ")
        f.write(name + "," + info +"\n")
        print(info)
    my_url=my_url.replace(chr(change),chr(change+1))
    change=change+1
    
    print(my_url)
f.close()