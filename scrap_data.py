from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser=webdriver.chrome()
browser.get(url)

time.sleep(10)

scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,("https://en.wikipedia.org/wiki/Lists_of_stars"))
    
    url.find("table",attrs={"class","wikitable"})
    
    table_body=url.find('tbody')
    
    table_rows = table_body.find_all('tr')
    
    for row in table_rows:
            table_cols = row.find_all('td')
            
            temp_list=[]
            
            for col_data in table_cols:
                data=col_data.text.strip()
                temp_list().append(data)
                
    scraped_data.append(temp_list)
    
scrape()
stars_data=[]

for i in range(0,len(scraped_data)):
    Star_names = url[i][1]
    Distance =url[i][3]
    Mass = url[i][5]
    Radius = url[i][6]
    Lum = url[i][7]
    
    
    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

print(stars_data)

headers = ['Star_name','Distance','Mass','Radius','Luminosity']  

star_df_1 = pd.DataFrame(stars_data, columns=headers)
star_df_1.to_csv('scraped_data.csv',index=True, index_label="id")