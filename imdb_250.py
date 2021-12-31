import requests
from bs4 import BeautifulSoup



url="https://www.imdb.com/chart/top/"

response=requests.get(url)

html_content=response.content

soup=BeautifulSoup(html_content,"html.parser")

user=float(input("Which rating movie would you like to reach?:"))

headers=soup.find_all("td",{"class": "titleColumn"})
ratings=soup.find_all("td",{"class": "ratingColumn imdbRating"})



for headers, ratings in zip(headers, ratings):
    headers=headers.text
    ratings=ratings.text
    
    headers=headers.strip()
    headers=headers.replace("\n","")
    
    ratings=ratings.strip()
    ratings=ratings.replace("\n","")
    
    
    if(float(ratings)>user):
        print("Movie name:{} rating:{}".format(headers,ratings))
    
    
    
