#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

# clear the terminal
os.system("clear")

# import the chrome driver
WEBDRIVER_PATH= 'bin/chromedriver'
driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH)


# get world data
def dataMonde() :
    # get the website
    driver.get('https://coronavirus.politologue.com/')

    # find data by xpath 
    casMonde = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[2]/div[2]/div[1]/div/span").text
    mortMonde = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[2]/div[2]/div[2]/div/span[1]").text
    gueris = driver.find_element_by_xpath("/html/body/form/div[3]/div/div/div[2]/div[2]/div[3]/div/span[1]").text


    # print data
    print("\n-------------- MONDE ---------------\n")
    print("cas confirmés : "+casMonde)
    print("décès : "+mortMonde)
    print("patients guéris : "+gueris)
    #close the browser
    driver.close()

dataMonde()