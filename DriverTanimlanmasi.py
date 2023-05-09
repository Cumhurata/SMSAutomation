import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DatabaseBaglantisi import OracleDB
from Screenshot import Screenshot


class ChromeDriver:
    import time

    def __init__(self, headless=False):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=self.options)

    def quit(self):
        self.driver.quit()


chrome = ChromeDriver()
database = OracleDB()
now = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
folder_name = now + "-screenshots"


def wait_sometime():
    chrome.time.sleep(3)


def create_folder():
    # Yeni bir klasör oluşturun
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    folder_path = os.path.abspath(folder_name)


def take_screenshot(name):
    username = os.environ['USERNAME']
    file_name = now + "-" + name + ".png"
    chrome.driver.save_screenshot(r'C:\Users\{}\PycharmProjects\SMSAutomation\{}/{}'.format(username, folder_name, file_name))


class Pega:

    @staticmethod
    def login_page():
        # go to link
        chrome.driver.get("http://akbank-shippingtest.adqura.com/prweb/")

        # Wait until the login form is visible
        login_form = WebDriverWait(chrome.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "txtUserID"))
        )

        # Fill in the username and password fields
        chrome.driver.find_element(By.ID, "txtUserID").send_keys("caglar.sinik@adqura.com")
        chrome.driver.find_element(By.ID, "txtPassword").send_keys("Akbank2028*")
        take_screenshot('LoginPage')

        # Click the login button
        chrome.driver.find_element(By.ID, "sub").click()


class UI:

    @staticmethod
    def navigate_ui():
        # Launch Portal
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, "Launch portal").click()
        wait_sometime()
        take_screenshot('LaunchPortal')
        # UI
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, "CRM Designer Portal").click()
        wait_sometime()
        take_screenshot('CRMDesignerPortal')

    @staticmethod
    def click_run_button_navigate():
        # Run
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, 'Çalıştır').click()
        chrome.time.sleep(5)
        take_screenshot('NavigateRunButton')

    @staticmethod
    def click_run_button():
        chrome.driver.implicitly_wait(20)
        chrome.driver.switch_to.frame("PegaGadget1Ifr")
        chrome.driver.find_element(By.CSS_SELECTOR, '#start-run > button > i').click()
        chrome.time.sleep(5)
        take_screenshot('RunButton')

    @staticmethod
    def check_ui_state():
        locator = (By.XPATH, '//*[@id="RULE_KEY"]/div[1]/div/div/div[2]/span')
        for i in range(50):

            status_check = chrome.driver.find_element(*locator).text

            # Refresh
            chrome.driver.implicitly_wait(10)
            wait_sometime()

            if status_check == "Complete":
                break
            else:
                wait_sometime()
                if i % 10 == 0:
                    chrome.driver.refresh()

    def running_batch(self):
        self.click_run_button_navigate()
        self.click_run_button()
        self.check_ui_state()


class STF:

    @staticmethod
    def navigate_stf():
        # Launch Portal
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, "Launch portal").click()
        wait_sometime()

        # STF
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, "STF").click()
        wait_sometime()
        take_screenshot('STF')

    @staticmethod
    def click_data_generator_stf():
        # Data Generator
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.LINK_TEXT, "Data Generator").click()
        wait_sometime()
        take_screenshot('DataGenerator')

    @staticmethod
    def write_bucket_name_stf(bucketName):
        # Click Bucket Name and Write it
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").click()
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").send_keys(bucketName)
        wait_sometime()

        # Click one more time
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, "//span[.='" + bucketName + "']").click()
        wait_sometime()
        take_screenshot('BucketName')

    @staticmethod
    def write_graph_name_stf(graphName):
        # Click GraphName and Write GraphName
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').click()
        chrome.driver.find_element(By.NAME, '$PGeneratorTab$pGraphName').send_keys(graphName)
        chrome.driver.find_element(By.XPATH, "//span[.='" + graphName + "']").click()
        wait_sometime()
        take_screenshot('graphName')

    @staticmethod
    def enter_number_records_stf():
        # Enter Number of Records
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.NAME, '$PGeneratorTab$pRecordCount').click()
        chrome.driver.find_element(By.NAME, '$PGeneratorTab$pRecordCount').send_keys("1")
        wait_sometime()

    @staticmethod
    def click_refresh_button_stf():
        # Refresh one time
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
        wait_sometime()

    @staticmethod
    def click_generate_button_stf():
        # Click Generate Button
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, "//button[.='Generate']").click()
        wait_sometime()
        take_screenshot('Generate')

    @staticmethod
    def check_completed_text_stf():
        # complete text must be shown on screen for specified graph the latest generation
        locator = (By.XPATH, '//*[@id="$PpgRepPgSubSectionStatusB$ppxResults$l1"]/td[4]/div/span')
        for i in range(10):

            status_check = chrome.driver.find_element(*locator).text

            # Refresh
            chrome.driver.implicitly_wait(10)
            chrome.driver.find_element(By.XPATH, "//button[.='Refresh']").click()
            wait_sometime()

            if status_check == "Complete":
                break
            else:
                wait_sometime()

    @staticmethod
    def clear_bucket_name_stf():
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucketName").click()
        wait_sometime()

    @staticmethod
    def click_down_arrow_stf():
        chrome.driver.implicitly_wait(10)
        # chrome.driver.find_element(By.NAME, '$PGeneratorTab$pRecordCount').clear()
        chrome.driver.find_element(By.XPATH,
                                   '//*[@id="RULE_KEY"]/div/div[1]/div[3]/div/div[1]/div/div/button/i').click()
        wait_sometime()

    @staticmethod
    def click_x_button_stf():
        chrome.driver.implicitly_wait(10)
        chrome.driver.find_element(By.XPATH, '//*[@id="autocompleAG_Clear_Icon"]').click()
        wait_sometime()

    def generating_data_graph(self, bucketName, graphName):
        # Data Generator
        self.click_data_generator_stf()

        # Click Bucket Name and Write it
        self.write_bucket_name_stf(bucketName)

        # Click GraphName and Write GraphName
        self.write_graph_name_stf(graphName)

        # Enter Number of Records
        self.enter_number_records_stf()

        chrome.time.sleep(2)

        # Refresh one time
        self.click_refresh_button_stf()

        # Click Generate Button
        self.click_generate_button_stf()

        # complete text must be shown on screen for specified graph the latest generation
        self.check_completed_text_stf()

        # clear bucket name
        self.clear_bucket_name_stf()

        # Click down arrow
        self.click_down_arrow_stf()

        # click clear 'x' button
        self.click_x_button_stf()

        # Refresh
        self.click_refresh_button_stf()


pega = Pega()
stf = STF()
ui = UI()

product_offer_outcome = [
    [{"bucket_name": "SMS-Phase1"},
     {"graph_name": "TicariKartOFOKamp_SMS"},
     {"graph_prefix": "10050"}, {"CustomerID": ""}
     ]]


def return_cust_id_from_prefix(prefix):
    prefix = "'%" + prefix + "%'"
    customer_id = database.select("PGA_TMUSTERI_V", "MUSTERI_ID",
                                  "MUSTERI_ID LIKE " + prefix + "AND TARIH >SYSDATE-1 ORDER BY MUSTERI_ID DESC FETCH FIRST 1 ROWS ONLY")
    customer_id = str(customer_id).replace("[(", "")
    customer_id = str(customer_id).replace(",)]", "")
    return customer_id


def suppression_check():
    # Creating Datas
    for b_outcome in product_offer_outcome:
        bucket_name_tmp = str(b_outcome[0]['bucket_name'])
        graph_name_tmp = str(b_outcome[1]['graph_name'])
        prefix1_tmp = str(b_outcome[2]['graph_prefix'])

        creating_datas(bucket_name_tmp, graph_name_tmp)

        primary_customer_id_tmp = return_cust_id_from_prefix(prefix1_tmp)
        b_outcome[3]['CustomerID'] = primary_customer_id_tmp
        print(primary_customer_id_tmp)
    # Running Batch
    running_ui()

    for b_outcome in product_offer_outcome:
        customer_id = b_outcome[3]['CustomerID']
        condition_db = "CUSTOMERID = '" + customer_id + "'"
        print(database.select("INTERACTION_HISTORY_V", "*", condition_db))


def change_web_window(window):
    # Go To New Window
    chrome.driver.switch_to.window(window)


def creating_datas(bucketName, graphName):
    create_folder()
    pega.login_page()
    stf.navigate_stf()
    window_before = chrome.driver.window_handles[0]
    window_after = chrome.driver.window_handles[1]
    change_web_window(window_after)
    stf.generating_data_graph(bucketName, graphName)
    change_web_window(window_before)


def running_ui():
    ui.navigate_ui()
    window_after = chrome.driver.window_handles[2]
    change_web_window(window_after)
    ui.running_batch()


def main_operation():
    suppression_check()
    database.close_connection()
