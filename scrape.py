#Scrape stock data of NTC on NEPSE (2011 AD to present) from
#stocksansar.com using bs4 and selenium and save to a CSV file

import bs4, requests
import pandas as pd
from selenium import webdriver
import time

total_data = []
driver = webdriver.Chrome(r'C:\Users\HP\Downloads\Compressed\chromedriver_win32_2/chromedriver.exe')
company_id = 'ntc'
driver.get('https://www.sharesansar.com/company/'+company_id)
elem = driver.find_element_by_id('btn_cpricehistory')
elem.click()
time.sleep(3)
i=0
while True:
    i+=1
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
    tables = soup.select('#myTableCPriceHistory')[0]
    df = pd.read_html(str(tables))[0]
    total_data.append(df)
    print(f'Added page {i}')
    nextPage = driver.find_element_by_id('myTableCPriceHistory_next')
    nextPage.click()
    if 'disabled' in nextPage.get_attribute('class'):
        break
    time.sleep(3)

total_df = pd.concat(total_data)
total_df.to_csv('stockdata.csv')
print('Successfully created csv file')
