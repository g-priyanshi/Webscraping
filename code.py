#importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
#taking input of actor's name and requesting webpage
actor_name= input("Enter name of actor: ")
actor_name = actor_name.split()
tag_name="_".join(actor_name)
url ="https://en.wikipedia.org/wiki/"+tag_name+"_filmography"
req =requests.get(url)
#print(req.status_code)
#scraping wikipedia for filmography information
soup= BeautifulSoup(req.text, "html.parser")
html_code = soup.find("table", {"class":"wikitable plainrowheaders sortable"})
#print(html_code)
#creating and printing database
df=pd.read_html(str(html_code))
df = pd.DataFrame(df[0])
#print(df.tail())
table=df.iloc[::-1].reset_index(drop=True)
table=table.iloc[:, 0:2]
table.index = table.index+1
print(table)
