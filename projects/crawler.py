#importing required libraries
from bs4 import *
import requests as rq 
import os

#requesting web
r2=rq.get("https://unsplash.com/")
soup2= BeautifulSoup(r2.text,"html.parser")

links=[]

x=soup2.select('img[src^="https://unsplash.com/"]')

for img in x:
    links.append(img['src'])
for l in links:
    print(l)


os.mkdir('Mimo')
i=1
for index,img_link in enumerate(links):
    if i<=10:
        img_data=req.get(img_link).content
        with open("Mimo/"+str(index+1)+'.jpg','wb+') as f:
            f.write(img_data)
    else:
        f.close()
        break
