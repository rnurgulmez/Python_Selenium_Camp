from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# Selenium,tarayicida yaptigimiz isleri otomatize eder.

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.de/")
sleep(2)
popUp = driver.find_element(By.XPATH,"//*[@id='L2AGLb']/div")
popUp.click()
input = driver.find_element(By.NAME,"q")
sleep(2)
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME,"btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
# bu sefer elements dedik 
listOfCourses = driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"Kodlamaio sitesinde su anda {len(listOfCourses)} adet kurs var.")
# sleep(5)
while True:
    continue
# HTML Locators : HTML'deki elementlerin konumunu ogrenmek

# en tepedeki elementten aradigimiz elemente yol cizer
# /html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a : full xpath en tepeden baslar
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a : xpath en yakin unique alandan baslar
# ancak xpath kullanirken rso kismi tek tirnak yapmaliyiz

# web scraping
# data scraping