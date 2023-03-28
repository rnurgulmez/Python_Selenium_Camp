from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

class Test_Sauce:

    def test_invalid_login(self):
        # en fazla 5 saniye olacak sekilde user-name id'li elementin gorunmesini bekle
        # cift parantez sebebi tek parametre halinde gondermek icin By.ID,"user-name" bu kismi tuple olarak gondermemiz.
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput  = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.ID,"password")
        sleep(2)
        usernameInput.send_keys("1")
        password.send_keys("1")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3/button")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Sonucu : {testResult}")
    
    def valid_login(self):
        self.driver.get("https://www.saucedemo.com")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput  = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,"password")))
        password = self.driver.find_element(By.ID,"password")
        sleep(2)
        # Action Chains
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(usernameInput,"standard_user")
        actions.send_keys_to_element(password,"secret_sauce")
        # bu 2 aksiyonu perform dedigimiz anda ard arda sirayla calistirilir.
        actions.perform()
        # usernameInput.send_keys("standard_user")
        # password.send_keys("secret_sauce")
        sleep(2)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,500)")
        sleep(20)
        

         

testClass = Test_Sauce()
testClass.test_invalid_login()
testClass.valid_login()

