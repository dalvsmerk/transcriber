from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Whatsapp:
    def __init__(self, logger, group_name='test'):
        self.logger = logger
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.group_name = group_name
        self.message_input = None

        self.load_webapp()

    def send_group_message(self, message, title=None):
        self.open_group()

        if title:
            self.message_input.send_keys(title, Keys.SHIFT, Keys.ENTER)
            self.message_input.send_keys(Keys.SHIFT, Keys.ENTER)

        lines = message.split('\n')

        for line in lines:
            self.message_input.send_keys(line.strip(), Keys.SHIFT, Keys.ENTER)

        self.message_input.send_keys(Keys.ENTER)

    def load_webapp(self):
        self.driver.get('https://web.whatsapp.com/')

        self.wait_landing()

    def wait_landing(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.landing-title'))
            )
        except:
            self.driver.quit()

    def open_group(self):
        chat_list = self.driver.find_element(By.CSS_SELECTOR, '[id="pane-side"]');
        group_title = None
        error = None
        
        # scroll chat list until visible
        while group_title is None:
            try:
                group_title = self.driver.find_element(By.XPATH, "//span[@title='{}']".format(self.group_name))
            except Exception as e:
                error = e
                self.driver.execute_script('arguments[0].scrollBy(0, 100)', chat_list)
                self.driver.implicitly_wait(0.1)
                continue

        if group_title is None:
            # this would not be executed ever
            self.logger.log(self.logger.ERROR, 'Couldn\'t find chat by title {}'.format(self.group_name))
            self.logger.log(self.logger.ERROR, error)
        else:
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
