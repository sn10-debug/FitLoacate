
import imp
from selenium import webdriver

chrome_driver_path="C:\Dev-files\chromedriver.exe"

driver=webdriver.Chrome(executable_path=chrome_driver_path)

# This chrome driver tells the selenium how to work with the chrome and its latest versions

# driver.get('https://www.youtube.com/watch?v=_PQGIf1fr8o&list=WL&index=7&t=2s')

# driver.get('https://mail.google.com/mail/u/0/#inbox')

# driver.get('https://www.nseindia.com/get-quotes/equity?symbol=RELIANCE')
# stock_price=driver.find_element_by_id('quoteLtp')
# print(stock_price.text)


# logo_nse=driver.find_element_by_css_selector('.navbar .top_logomenu .navbar-brand img')
# print(logo_nse.get_attribute('src'))


# driver.get('file:///C:/Users/user/Desktop/Shakti/wallet/index.html')



# driver.get('https://www.python.org/')

# schedule_list=[i.text for i in driver.find_elements_by_css_selector('.event-widget .menu li time')]
# event_list=[i.text for i in driver.find_elements_by_css_selector('.event-widget .menu li a')]
# print(schedule_list)
# print(event_list)


# events={}

# for i,j in zip(schedule_list,event_list):
#     events[i]=j

# import pprint

# pprint.pprint(events)

# driver.get(logo_nse.get_attribute('src'))

# driver.close()

# driver.close() is used to close a particular tab



# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# num_articles=driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')

# print(num_articles.text)


# create_button=driver.find_element_by_class_name('create')


# This will click the button

# create_button.click()



# portals_link= driver.find_element_by_link_text('All portals')
# This will find the element with this text which has a link

# portals_link.click()





# You Tube



# driver.get('https://www.youtube.com/')

# search_bar=driver.find_element_by_name('search_query')
# search_bar.send_keys('Python')

# serach_button=driver.find_element_by_id('search-icon-legacy')
# serach_button.click()

# This will do auto search




# driver.find_element_by_link_text('SIGN IN').click()

# driver.find_element_by_xpath('//*[@id="button"]').click()
# sign_in_button.click()

# sign_in_button=driver.find_elements_by_css_selector('tp-yt-paper-button')[1]

# print(sign_in_button.text)


# import time
# time.sleep(2)

# sign_in_button.click()

# time.sleep(2)

# email_input=driver.find_element_by_xpath('//*[@id="identifierId"]')

# email_input.send_keys('nreena078@gmail.com')


# time.sleep(2)


# next_button=driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')

# next_button.click()





driver.get('https://vtopcc.vit.ac.in/vtop/initialProcess')



login_button_1=driver.find_element_by_class_name('btn-success')
login_button_1.click()

# driver.quit()

# driver.quti() is used to close the whole browser

import time

time.sleep(2)

login_button_2=driver.find_element_by_class_name('btn-primary')
login_button_2.click()

# Xpath is a another way to get a html element  