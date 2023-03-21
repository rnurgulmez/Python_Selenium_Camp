from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class Test_Sauce:
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        # en fazla 5 saniye olacak sekilde user-name id'li elementin gorunmesini bekle
        usernameInput  = driver.find_element(By.ID,"user-name")
        password = driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        password.send_keys("1")
        sleep(2)
        loginBtn = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu : {testResult}")

testClass = Test_Sauce()
testClass.test_invalid_login()

