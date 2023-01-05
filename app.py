######################## https://github.com/Muhammad1997 ########################

######################## Imports ########################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
from datetime import datetime
import random
# pip install playsound==1.2.2 
from playsound import playsound
######################## Variables ########################
# number of sound tracks in soundFiles folder
num_of_tracks = 18
# initial value for EGP currency
pre_currency = 25.00
# currency refresh rate in seconds
refresh_rate = 30
######################## APIs ########################
# function to play random sound track
def play_sound():
    try:
        sound_track = str(random.randint(1,num_of_tracks))+".mp3"
        playsound('soundFiles/'+sound_track)
    except Exception as error:
        print(error) 

# function to update the current currency
def update_currency():
    global pre_currency
    try:
        # disable webdriver output and GUI
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=options)
        # open google search web page
        google_url = "https://www.google.com/search?q=usd+to+egp"
        driver.get(google_url)
        time.sleep(1)
        # parse HTML to find the new currency value
        soup = BeautifulSoup(driver.page_source,'lxml')
        result_div = soup.find('div',attrs={'class' : 'dDoNo'})
        currency_span = result_div.find('span', class_='DFlfde')
        # round the currency to two digits
        currency = round(float(currency_span['data-value']),1)
        # close the session
        driver.close() 
        # get the current timestamp
        timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        # print the new currency
        print(timestamp,":",currency,"EGP")
        # play new sound if current currency is greater
        if (currency > pre_currency):play_sound()
        pre_currency = currency   
    except Exception as error:
        print(error)        

######################## MAIN ########################
while(1):
    update_currency()
    time.sleep(refresh_rate)