from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import unittest
import time


class MkoverforallTest(unittest.TestCase):
    driver = None
    service = None

    @classmethod
    def setUpClass(cls):
        cls.service = Service("C:\drivers\chromedriver\chromedriver.exe")
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()

    def test_homepage(self):
        """Get URL"""
        self.driver.get('https://www.makeoverforall.com/')
        """Title page"""
        self.assertEqual('Home | Make Over', self.driver.title, 'webpage title is different')
        # close pop-ads
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[1]/i').click()
        self.driver.implicitly_wait(5)

    @unittest.skip
    def test_registerEmail(self):
        """Click the account icon"""
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[2]').click()
        self.driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div[2]/div/div[1]/a[2]').click()  # click register
        self.driver.find_element(By.ID, 'register-email').send_keys('aaa@gmail.com')  # input email
        self.driver.find_element(By.ID, 'register-fullname').send_keys('ATMOS')  # input full name
        self.driver.find_element(By.ID, 'register-phone_number').send_keys('089845612145')  # input phone number
        self.driver.find_element(By.ID, 'register-password').send_keys('12345abcde')  # input password
        self.driver.find_element(By.ID, 'register-confirm_password').send_keys('12345abcde')  # input confirm password
        self.driver.implicitly_wait(5)  # gives an implicit wait for 5 seconds
        try:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button').click()  # click register button
        except ElementClickInterceptedException:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button').click()  # click register button

    def test_invalidLoginEmail(self):
        """Click the account icon"""
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[2]').click()
        self.driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/div[2]/div/div[1]/a[1]')  # click login

        # Login with invalid email - valid password
        self.driver.find_element(By.ID, 'login-email').send_keys('zxcvb@gmail.com')  # input invalid email
        self.driver.find_element(By.ID, 'login-password').send_keys('12345abcde')  # input valid password
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button')  # click login
        # clear input from textbox
        self.driver.implicitly_wait(3)
        for i in range(0, 20):
            self.driver.find_element(By.XPATH, '//*[@id="login-email"]').send_keys(Keys.BACKSPACE)
        for i in range(0, 20):
            self.driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(Keys.BACKSPACE)

        # Login with valid email - invalid password
        self.driver.find_element(By.ID, 'login-email').send_keys('aaa@gmail.com')  # input invalid email
        self.driver.find_element(By.ID, 'login-password').send_keys('poiuy09876')  # input valid password
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button')  # click login
        # clear input from textbox
        self.driver.implicitly_wait(3)
        for i in range(0, 20):
            self.driver.find_element(By.XPATH, '//*[@id="login-email"]').send_keys(Keys.BACKSPACE)
        for i in range(0, 20):
            self.driver.find_element(By.XPATH, '//*[@id="login-password"]').send_keys(Keys.BACKSPACE)

    def test_validLoginEmail(self):
        # click account
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[2]').click()
        self.driver.implicitly_wait(10)  # gives an implicit wait for 10 seconds
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/div[2]/div/div[1]/a[1]')  # click login
        self.driver.implicitly_wait(2)
        self.driver.find_element(By.ID, 'login-email').send_keys('aaa@gmail.com')  # input invalid email
        self.driver.find_element(By.ID, 'login-password').send_keys('12345abcde')  # input valid password
        try:
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button').click()  # click login
        except ElementClickInterceptedException:
            self.driver.implicitly_wait(5)
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section/div/div[2]/div/div[2]/div[2]/form/button').click()  # click login

    time.sleep(10)

    #@unittest.skip
    def test_sale(self):
        self.driver.find_element(By.ID, 'nav-item 41').click()
        self.driver.implicitly_wait(10)

    #@unittest.skip
    def test_addItem(self):
        # Click add to bag
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div/button').click()
        for i in range(0, 5):  # Click + 5x
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section[1]/div/div/div[2]/section/div[4]/div/div[2]/button').click()
        for i in range(0, 2):  # click - 2x
            self.driver.find_element(By.XPATH,
                                     '//*[@id="__next"]/main/section[1]/div/div/div[2]/section/div[4]/div/div[1]/button').click()

        # click add to bag button
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section[1]/div/div/div[2]/section/div[5]/div[1]/button').click()
        self.driver.implicitly_wait(5)
        # View bag
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[3]/div[2]/div[1]/a').click()
        # Click + to add
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/button[2]').click()
        # Click - to reduce
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/button[1]').click()
        # Add to wishlist
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[3]/button[1]').click()
        # Remove
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div[3]/button[2]').click()
        # Continue shopping
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/a').click()

    time.sleep(5)

    @unittest.skip('Checkout - This method is skipped')
    def test_checkout(self):
        # Click wishlist icon
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[1]').click()
        # Add to bag
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/main/section/div/div/div/div/div/div[2]/div/div[2]/div/button').click()
        # Add to bag again
        self.driver.find_element(By.XPATH,
                                 '/html/body/div[4]/div/div/div/div[2]/div/section/div/div/div[2]/section/div[6]/div[1]/button').click()
        # View bag
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[3]/div[2]/div[1]/a').click()
        # Proceed to check out
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/main/section/div/div/div[2]/div/div[1]/button').click()

    #@unittest.skip
    def test_logout(self):
        self.driver.implicitly_wait(20)
        # click account
        self.driver.find_element(By.XPATH,
                                 '//*[@id="__next"]/div[2]/nav/div/div[2]/div/div[1]/div[1]/ul[2]/li[2]').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID, 'item logout')  # Click log out

    @classmethod
    def tearDownClass(cls):
        #cls.driver.quit()
        print('Test completed.....')


if __name__ == "__main__":
    unittest.main()