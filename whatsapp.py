from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Whatsapp:
    def __init__(self, group_name='test'):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.group_name = group_name

        self.loadWebapp()

    def sendGroupMessage(self, message, title=None):
        self.openGroup()

        if title:
            self.message_input.send_keys(title, Keys.SHIFT, Keys.ENTER)
            self.message_input.send_keys(Keys.SHIFT, Keys.ENTER)

        lines = message.split('\n')

        for line in lines:
            self.message_input.send_keys(line.strip(), Keys.SHIFT, Keys.ENTER)

        self.message_input.send_keys(Keys.ENTER)

    def loadWebapp(self):
        self.driver.get('https://web.whatsapp.com/')

        self.waitLanding()

    def waitLanding(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.landing-title'))
            )
        except:
            self.driver.quit()

    def openGroup(self):
        group_title = self.driver.find_element(By.XPATH, "//span[@title='{}']".format(self.group_name))
        group_title.click()

        self.message_input = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="conversation-compose-box-input"]');

    def logout(self):
        menu_icon = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="menu"data-testid="menu"]');
        menu_icon.click()

        logout_button = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Log out"]');
        logout_button.click()

        self.waitLanding()

    def close(self):
        self.logout()
        self.driver.close()
