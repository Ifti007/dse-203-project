import csv
import pandas
from itertools import chain
from parsel import Selector
import time
from time import sleep

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

start_time = time.time()

if __name__ == '__main__':

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    options.add_argument('headless')
    time.sleep(0.5)
    driver = webdriver.Chrome(options=None)


    driver.get('https://venturebeat.com/')
    time.sleep(0.5)
    driver.set_window_position(500,0)
    driver.set_window_size(1400,1000)
    time.sleep(0.6)

    #initial page load
    #search button to input keys
    search_button = driver.find_element(By.XPATH, '//*[@class = "display-search-icon"]')
    search_button.click()
    time.sleep(0.5)
    search_query = driver.find_element(By.XPATH, '//input[@id = "search-input"]')
    time.sleep(0.5)
    search_query.send_keys('AI Funding')
    search_query.send_keys(Keys.RETURN)
    sleep(3)

    elements = []
    urls = []
    headers = []
    while True:
        try:
            print('\n\n*******Initiating page load*******')
            source = driver.page_source
            elements = driver.find_elements(By.XPATH, "//a[@class = 'ArticleListing__title-link']")
            print('\n*******Elements Found*******')

            urls.append([url.get_attribute('href') for url in elements])
            headers.append([header.get_attribute('title') for header in elements])
            print('******* URL/Header Extracted *******')

            loadMoreButton = driver.find_element(By.XPATH, "//a[@class = 'next page-numbers']")
            print('*******Load Button Found******')
            loadMoreButton.send_keys(Keys.RETURN)
            print('*****New page clicked*****')
            time.sleep(0.8)

        except:
            print('\n*****Loading new page failed***\n')
            break


    x = 0
    for i in range(len(urls)):
        x += len(urls[i])

    y = 0
    for i in range(len(headers)):
        y += len(headers[i])
    print('\n*********Results*********\n')
    print('{} URLs collected'.format(x))
    print('{} Headers collected'.format(y))
    time.sleep(0.5)

    writer = csv.writer(open('output/venturebeat_results_test.csv', 'w+', encoding='utf-8-sig', newline=''))
    writer.writerow(['Header', 'SubHeader', 'Date', 'Abstract'])

    for i in range(len(urls)):
        for j in range(len(urls[i])):
            try:
                print('\n**** Entering new URL ****')
                driver.get(urls[i][j])
                print('****New URL entered****')
                sleep(0.5)
                sel = Selector(text=driver.page_source)

                header_temp = sel.xpath("//*[@class = 'article-title']/text()").extract_first()
                print('****Header Extracted****')
                subheader_temp = sel.xpath("//div[@class = 'article-content']//p/em/text()").extract_first()
                print('****SubHeader Extracted****')
                body = sel.xpath("//div[@class = 'article-content']/p/text() | //div[@class = 'article-content']/p/a/text()").getall()
                print('****Body Extracted****')
                body = ' '.join(body)
                print('****Body Cleaned****')
                dttm = sel.xpath("//div[@class = 'article-time-container']/time/text()").extract_first()
                print('****Date Extracted****')
                print('Header: {}'.format(header_temp))
                print('SubHeader: {}'.format(subheader_temp))
                print('Date: {}'.format(dttm))
                # print('Abstract: {}'.format(body))
                print('**** End Page Results ****')
                # ag+=1
                writer.writerow([header_temp,
                                 subheader_temp,
                                 dttm,
                                 body])
            except:
                print('Error in URL [{}][{}]'.format(i,j))
                # ag+=1
                pass


    print('Program took {} seconds to execute'.format(time.time() - start_time))
    driver.quit()
