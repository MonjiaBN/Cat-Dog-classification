import requests
from bs4 import BeautifulSoup
import os
import urllib.request 

headers={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}

url='https://freeimages.com/search/cat'
#url='https://freeimages.com/search/dog'

#make a get request in order to get the page content
 
response=requests.get(url,headers=headers).text  #return a response object which contain the server's response
 
# using BeautifulSoup to parse the response object
soup=BeautifulSoup(response , "lxml")   

Images=[]
img_links=soup.select('img[src^="https://images.freeimages.com/images"]')
print(img_links)
for i in range(len(img_links)):
    Images.append(img_links[i]['src'])

for i in range(len(Images)):
    name="C:/Users/Client/Desktop/pet_classification/Catimage/"+str(i)+ ".jpg"
    #name="C:/Users/Client/Desktop/pet_classification/Dogimage/"+str(i)+ ".jpg"
    urllib.request.urlretrieve(Images[i],name)








 