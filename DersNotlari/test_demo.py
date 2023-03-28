from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
# prefix => test_
# postfix
class Test_DemoClass:
    # her testen once cagirilir
    def setup_method(self):
        self.driver =webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        # günün tarihini al bu tarih ile bir klasor var mi kontrol et yoksa olustur
        self.folderPath = str(date.today())
        # 24.03.2023
        Path(self.folderPath).mkdir(exist_ok=True)
    # her testen sonra cagirilir
    def teardown_method(self):
        self.driver.quit()

    # setup -> test_demoFunction -> teardown
    def test_demoFunction(self):
        print("demo test")
        # 3A ACT ARRANGE ASSERT
        text = "hello"
        assert text == "hello"
# test_ one eki ile olmali cunku test classin da olsa bile o class icinde normal fonksiyonlar olabilir.Pytestin test olarak algilamasi icin test_ on ekine ihtiyacimiz var.
    # setup -> test_demo2 -> teardown
    def test_demo2(self):
        assert True

    # pytest anotasyonlar(decoratorler)
    @pytest.mark.parametrize("username,password",[("1","1"),("kullanciAdim","sifrem")])
    def test_invalid_login(self,username,password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput  = self.driver.find_element(By.ID,"user-name")
        self.waitForElementVisible((By.ID,"password"),10)
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form//h3[@data-test='error']")
        # assert'un yanindaki kosul dogru ise testi basarili yap degilse basariiz yap olarak dusunulebilir.
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def waitForElementVisible(self,locator,timeout=5):
       WebDriverWait(self.driver,5).until(ec.visibility_of_element_located(locator)) 