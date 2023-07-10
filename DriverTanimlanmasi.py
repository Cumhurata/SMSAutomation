import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from DatabaseBaglantisi import OracleDB


class ChromeDriver:
    import time

    def __init__(self):
        self.options = Options()
        # self.options.add_argument('--headless')
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
    return folder_path


def take_screenshot(name):
    username = os.environ['USERNAME']
    file_name = now + "-" + name + ".png"
    chrome.driver.save_screenshot(
        r'C:\Users\LENOVO\PycharmProjects\SMSAutomation-master\{1}\{2}'.format(username, folder_name, file_name))


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
        chrome.driver.find_element(By.ID, "txtPassword").send_keys("Akbank2030*")
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
        chrome.driver.find_element(By.LINK_TEXT, 'Run').click()
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
        for i in range(100):

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
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucket$pBucketName").click()
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucket$pBucketName").send_keys(bucketName)
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
        locator = (By.XPATH, '//*[@id="bodyTbl_right"]/tbody/tr[2]/td[5]')
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
        chrome.driver.find_element(By.NAME, "$PGeneratorTab$pBucket$pBucketName").click()
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


class DB_CHECK:
    @staticmethod
    def simplify_text(text):
        text = str(text).replace("(", "")
        text = str(text).replace(")", "")
        text = str(text).replace("'", "")
        text = str(text).replace(",", "")
        text = str(text).replace("[", "")
        text = str(text).replace("]", "")
        return text

    @staticmethod
    def simplify_text_sms_content(text):
        text = str(text).replace("(", "")
        text = str(text).replace(")", "")
        text = str(text).replace("[", "")
        text = str(text).replace("]", "")
        text = str(text).replace('"', '')
        text = str(text).rstrip(',')
        return text

    @staticmethod
    def db_check_operations(self, batch_output_data, b_outcome_temp):
        print("\n----------------------------Database Checks Started-------------------------------------\n")
        print("Current Offer: {}".format(str(b_outcome_temp[1]['graph_name'])))
        print("db den gelen veriler: {}".format(batch_output_data))
        print("offer catalogue: {}".format(b_outcome_temp))
        condition1 = "CASE_ID = " + "'" + str(batch_output_data[0][0]) + "' AND TREATMENT_NAME = '" + str(
            b_outcome_temp[14]['Treatment_Name']) + "' AND MUSTERI_ID = '" + str(b_outcome_temp[3]['CustomerID']) + "'"
        print(condition1)
        condition2 = "CASE_ID = " + "'" + str(batch_output_data[0][0]) + "' AND TREATMENT_NAME = '" + str(
            b_outcome_temp[14]['Treatment_Name']) + "'"
        print(condition2)
        # Check for mgts_content_type
        mgts_content_type = database.select("PBO.BATCH_OUTPUT_STATUS", "MGTS_DELIVERY_JOB_TYPE", condition2)
        mgts_content_type = DB_CHECK.simplify_text(mgts_content_type)
        print("MGTS from DB: {}".format(mgts_content_type))
        print(str(b_outcome_temp[4]['mgts_content_type']))
        if str(b_outcome_temp[4]['mgts_content_type']) != "":
            if str(b_outcome_temp[4]['mgts_content_type']) == mgts_content_type:
                print("\nMGTS CONTENT TYPE IS MATCHED! PASSED!\n")
            else:
                print("\nMGTS CONTENT TYPE IS NOT MATCHED! FAILED!\n")
        else:
            print("\nMGTS CONTENT TYPE IS NULL\n")

        # Check for MgtsSmsBudgetUnit
        mgts_sms_budget_unit = database.select("PBO.BATCH_OUTPUT_STATUS", "BUDGET_DEPT_ID", condition2)
        mgts_sms_budget_unit = DB_CHECK.simplify_text(mgts_sms_budget_unit)
        print("MgtsSmsBudgetUnit from DB: {}".format(mgts_sms_budget_unit))
        print(str(b_outcome_temp[5]['MgtsSmsBudgetUnit']))
        if str(b_outcome_temp[5]['MgtsSmsBudgetUnit']) != "":
            if str(b_outcome_temp[5]['MgtsSmsBudgetUnit']) == mgts_sms_budget_unit:
                print("\nMGTS SMS BUDGET UNIT IS MATCHED! PASSED!\n")
            else:
                print("\nMGTS SMS BUDGET UNIT IS NOT MATCHED! FAILED!\n")
        else:
            print("\nMGTS SMS BUDGET UNIT IS NULL\n")

        # Check for IysId
        iys_id = database.select("PBO.BATCH_OUTPUT_STATUS", "CMS_REF_ID", condition2)
        iys_id = DB_CHECK.simplify_text(iys_id)
        print("iys_id from DB: {}".format(iys_id))
        print(str(b_outcome_temp[6]['IysId']))
        if str(b_outcome_temp[6]['IysId']) != "":
            if str(b_outcome_temp[6]['IysId']) == iys_id:
                print("\nIYS ID IS MATCHED! PASSED!\n")
            else:
                print("\nIYS ID IS NOT MATCHED! FAILED!\n")
        else:
            print("\nIYS ID IS NULL\n")

        # Check for ToMobileNumber
        to_mobile_number = database.select("PBO.BATCH_OUTPUT", "MOBILE_PHONE_NO", condition1)
        to_mobile_number = DB_CHECK.simplify_text(to_mobile_number)
        print("to_mobile_number from DB: {}".format(to_mobile_number))
        print(str(b_outcome_temp[7]['ToMobileNumber']))
        if str(b_outcome_temp[7]['ToMobileNumber']) != "":
            if str(b_outcome_temp[7]['ToMobileNumber']) == to_mobile_number:
                print("\nMOBILE NUMBER IS MATCHED! PASSED!\n")
            else:
                print("\nMOBILE NUMBER  IS NOT MATCHED! FAILED!\n")
        else:
            print("\nMOBILE NUMBER IS NULL\n")

        # Check for SMSContent
        sms_content = database.select("PBO.BATCH_OUTPUT_STATUS", "DELIVERY_CONTENT", condition2)
        sms_content = DB_CHECK.simplify_text_sms_content(sms_content)
        print("SMSContent from DB: {}".format(sms_content))
        print(str(b_outcome_temp[8]['SMSContent']))
        if str(b_outcome_temp[8]['SMSContent']) != "":
            if str(b_outcome_temp[8]['SMSContent']) == sms_content:
                print("\nSMS CONTENT IS MATCHED! PASSED!\n")
            else:
                print("\nSMS CONTENT IS NOT MATCHED! FAILED!\n")
        else:
            print("\nSMS CONTENT IS NULL\n")

        # Check for FromAlias
        from_alias = database.select("PBO.BATCH_OUTPUT_STATUS", "SMS_ALIAS", condition2)
        from_alias = DB_CHECK.simplify_text(from_alias)
        print("from_alias from DB: {}".format(from_alias))
        print(str(b_outcome_temp[9]['FromAlias']))
        if str(b_outcome_temp[9]['FromAlias']) != "":
            if str(b_outcome_temp[9]['FromAlias']) == from_alias:
                print("\nFROM ALIAS IS MATCHED! PASSED!\n")
            else:
                print("\nFROM ALIAS IS NOT MATCHED! FAILED!\n")
        else:
            print("\nFROM ALIAS IS NULL\n")

        # Check for Seed_List
        seed_list = database.select("PBO.BATCH_OUTPUT_STATUS", "SEED_LIST", condition2)
        seed_list = DB_CHECK.simplify_text(seed_list)
        print("Seed_List from DB: {}".format(seed_list))
        print(str(b_outcome_temp[10]['Seed_List']))
        if str(b_outcome_temp[10]['Seed_List']) != "":
            if str(b_outcome_temp[10]['Seed_List']) == seed_list:
                print("\nSEED LIST IS MATCHED! PASSED!\n")
            else:
                print("\nSEED LIST IS NOT MATCHED! FAILED!\n")
        else:
            print("\nSEED LIST IS NULL\n")

        # Check for mgts_delivery_start_hr DELIVERY HOUR
        mgts_delivery_start_hr = database.select("PBO.BATCH_OUTPUT_STATUS", "mgts_delivery_start_hr", condition2)
        mgts_delivery_start_hr = DB_CHECK.simplify_text(mgts_delivery_start_hr)
        print("mgts_delivery_start_hr from DB: {}".format(mgts_delivery_start_hr))
        print(str(b_outcome_temp[11]['mgts_delivery_start_hr']))
        if str(b_outcome_temp[11]['mgts_delivery_start_hr']) != "":
            if str(b_outcome_temp[11]['mgts_delivery_start_hr']) == mgts_delivery_start_hr:
                print("\nDELIVERY HOUR IS MATCHED! PASSED!\n")
            else:
                print("\nDELIVERY HOUR IS NOT MATCHED! FAILED!\n")
        else:
            print("\nDELIVERY HOUR IS NULL\n")

        # Check for ContentLanguage
        content_language = database.select("PBO.BATCH_OUTPUT_STATUS", "language_cd", condition2)
        content_language = DB_CHECK.simplify_text(content_language)
        print("content_language from DB: {}".format(content_language))
        print(str(b_outcome_temp[12]["content_language"]))
        if str(b_outcome_temp[12]["content_language"]) != "":
            if str(b_outcome_temp[12]["content_language"]) == content_language:
                print("\nCONTENT LANGUAGE IS MATCHED! PASSED!\n")
            else:
                print("\nCONTENT LANGUAGE IS NOT MATCHED! FAILED!\n")
        else:
            print("\nCONTENT LANGUAGE IS NULL\n")

        # Check for Valid Days
        valid_days = database.select("PBO.BATCH_OUTPUT_STATUS", "VALID_DAYS", condition2)
        valid_days = DB_CHECK.simplify_text(valid_days)
        print("valid_days from DB: {}".format(valid_days))
        print(str(b_outcome_temp[13]["VALID_DAYS"]))
        if str(b_outcome_temp[13]["VALID_DAYS"]) != "":
            if str(b_outcome_temp[13]["VALID_DAYS"]) == valid_days:
                print("\nVALID DAYS IS MATCHED! PASSED!\n")
            else:
                print("\nVALID DAYS IS NOT MATCHED! FAILED!\n")
        else:
            print("\nVALID DAYS IS NULL\n")

        # Check cmdCampaignID
        ih_cust_id = "'" + str(batch_output_data[0][3]) + "'"
        condition_ih = "CUSTOMERID = " + ih_cust_id
        ih_result = database.select("INTERACTION_HISTORY_V", "*", condition_ih)
        print("ih_result from DB: {}".format(ih_result))
        if str(ih_result).__contains__(str(batch_output_data[0][3])):
            print("\nIH RECORD EXIST! PASSED!\n")
        else:
            print("\nIH RECORD IS NULL\n")
        print("\n----------------------------Database Checks End-------------------------------------\n")


pega = Pega()
stf = STF()
ui = UI()
db_checks = DB_CHECK()

product_offer_outcome = [
    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "DOBKazananAkbankliCP_SMS"},
     {"graph_prefix": "10137"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "5259"},
     {"IysId": "9873"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Sevgili Akbankli, 5.000 TL'ye varan chip-para kazanmak icin Kazanan Akbankli programina katilabilir; ek olarak EFT, havale ve daha bircok bankacilik hizmetinden ucretsiz faydalanabilirsiniz. Basvuru icin: Akbank.com/kazanan-akbankli-ol Detayli bilgi icin: Akbank.com/kazanan-akbankli Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "39684|64195|64633|54157"},
     {"mgts_delivery_start_hr": "11:30"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "DOBKazananAkbankliCP_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BirebirKOLASIletisim_SMS"},
     {"graph_prefix": "10151"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "7829"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Sevgili Akbankli, para transferlerini hizlica hesabiniza almak icin IBAN yerine cep telefonu numaraniz veya TCKN bilginizi kolay adres olarak tanimlayabilirsiniz. Kolay adres tanimi yapmak icin linke tiklamaniz yeterli: akbank.com/KolayAdresTanimlama. Detayli bilgi icin: akbank.com/KolayAdres. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis: 0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|64325|60747|63191"},
     {"mgts_delivery_start_hr": "11:15"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BirebirKOLASIletisim_SMS"}
     ],
    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "DOBKazananAkbankli_SMS"},
     {"graph_prefix": "10149"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "5259"},
     {"IysId": "9838"}, {"ToMobileNumber": "5555555555"},
     {
         "Sevgili Akbankli, 5.000 TL'ye varan chip-para kazanmak icin hemen mobilden Akbankli olup Kazanan Akbankli programina katilabilir; ek olarak EFT, havale ve daha bircok bankacilik hizmetinden ucretsiz faydalanabilirsiniz. Mobilden Akbankli olmak icin: akbank.com/AkbankMobiliAc Basvuru icin: Akbank.com/kazanan-akbankli-ol Detayli bilgi: Akbank.com/kazanan-akbankli Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "39684|64195|64633|54157"},
     {"mgts_delivery_start_hr": "12:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "DOBKazananAkbankli_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BireyselKKBasvuru_SMS"},
     {"graph_prefix": "10152"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "9153"}, {"ToMobileNumber": "5555555555"},
     {
         "Degerli Akbankli, Axess veya Wings kredi kartina basvurarak kampanya ve firsatlardan hemen yararlanmaya baslayabilirsiniz. Hemen basvurmak icin: https://www.wingscard.com.tr/06r5. Detayli bilgi icin: https://akbank.com/kart-kampanyalari. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "64325|63191|60747|28270"},
     {"mgts_delivery_start_hr": "15:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BireyselKKBasvuru_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BirebirAkbankMobil_SMS"},
     {"graph_prefix": "10153"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "7751"}, {"ToMobileNumber": "5555555555"},
     {
         "Sevgili Akbankli, Akbank Mobil ile size ozel hazirlanan kampanyalara katilip bankacilik islemlerinizi kolay ve hizli bir sekilde, dilediginiz yerden, 7/24 gerceklestirebilirsiniz. Hemen indirmek icin: akbank.com/AkbankMobiliAc. Detayli bilgi icin: akbank.com/Akbank-Mobil. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Iyi gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|64325|60747|63191"},
     {"mgts_delivery_start_hr": "16:45"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BirebirAkbankMobil_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "AkbankKartBasvuru_SMS"},
     {"graph_prefix": "10155"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "9065"}, {"ToMobileNumber": "5555555555"},
     {
         "Degerli Akbankli, dilediginiz ATM'den para cekip yatirabileceginiz, alisverislerinizden chip-para kazanabileceginiz, temassiz ozellikli Akbank Kart 1e1'e, Akbank Mobil uzerinden hemen basvurabilirsiniz. Simdi basvurmak icin: akbank.com/akbank-kart Detayli bilgi icin: https://akbank.com/akbankkart. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Iyi gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "64325|63191|60747|35304"},
     {"mgts_delivery_start_hr": "14:45"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "AkbankKartBasvuru_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "Birebir6ayKriterindeOlanVadeliAcmaBlg_SMS"},
     {"graph_prefix": "10157"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "7730"}, {"ToMobileNumber": "5555555555"},
     {
         "Sevgili Akbankli, yeni vadeli mevduat hesabi acarak 1e1 hizmet sundugumuz Akbanklilara ozel ayricalikli faiz oranindan yararlanabilirsiniz. Vadeli mevduat hesabinizi hemen acmak icin sizi akbank.com/vadeli-hesap sayfasina bekliyoruz. Detayli bilgi icin: akbank.com/vadeli-faiz-oranlari. Birebir Bankacilik hizmeti almanin diger ayricaliklari icin: Akbank.com/1e1AyricaliklarDunyasi. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|63191|60747|64325|61018"},
     {"mgts_delivery_start_hr": "16:18"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "Birebir6ayKriterindeOlanVadeliAcmaBlg_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "HaftasonuTAKampRec_SMS"},
     {"graph_prefix": "10159"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9089"},
     {"IysId": "2697"}, {"ToMobileNumber": "5555555555"},
     {
         "Axess'ten nakit ihtiyacinizi 7/24 karsilayabileceginiz Taksitli Avans firsatini kacirmayin! Hafta sonu subeler kapali olsa bile www.akbank.com/taksitli-avans linkine tiklayabilir, size ozel faiz oranlari ve vade secenekleri ile Taksitli Avans'inizi aninda kullanabilirsiniz. Detayli bilgi: 4442525 Juzdan'i henuz indirmediyseniz tiklayin: www.axess.com.tr/d032 Saglikli gunler dileriz Ucretsiz SMS'lerimizi almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AXESS"}, {"Seed_List": "34061|62757"},
     {"mgts_delivery_start_hr": "14:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "HaftasonuTAKampRec_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BirebirOtomatikVergiTalimatIBilgilendirme_SMS"},
     {"graph_prefix": "10161"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "8472"}, {"ToMobileNumber": "5555555555"},
     {
         "Sevgili Akbankli, vergi odemeleriniz icin kredi kartinizdan otomatik odeme talimati vererek son odeme tarihini dusunmemenin rahatligini yasayabilirsiniz. Akbank Internet veya size en yakin subemizden vergi odeme ve sorgulama islemlerinizi yapabilirsiniz. Detayli bilgi icin: akbank.com/vergi-odemeleri Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|63191|60747|64325"},
     {"mgts_delivery_start_hr": "15:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BirebirOtomatikVergiTalimatİBilgilendirme_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "JuzdanEkstreKesimOncesiTaksitKamp_SMS"},
     {"graph_prefix": "10162"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "8934"},
     {"IysId": "9185"}, {"ToMobileNumber": "5555555555"},
     {
         "Kredi karti ekstre kesim tarihine cok az kaldi. Hemen Juzdan'a girip donem ici islemlerinden uygun harcamalarini taksitlendirebilirsin. Juzdan'a gitmek icin linke tikla: www.axess.com.tr/fvvp Ucretsiz SMS'lerimizi almak istemiyorsan 'smsistemiyorum' yazip 8885'e gonderebilirsin. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|58507|58946|64577|65479"},
     {"mgts_delivery_start_hr": "16:50"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "JuzdanEkstreKesimOncesiTaksitKamp_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "TaksitliBorcTransferiKampanyasi_SMS"},
     {"graph_prefix": "10163"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9089"},
     {"IysId": "9799"}, {"ToMobileNumber": "5555555555"},
     {
         "Degerli Akbankli, diger bankalardaki kredi karti borclarinizi uygun faiz oraniyla Bireysel kredi kartiniza aktarabilir, ucretsiz 12 aya kadar taksitlendirebilirsiniz. Hemen tasimak icin: akbank.com/taksitli-borc-transferi Detayli bilgi icin: akbank.com/tbt Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "34061|61556"},
     {"mgts_delivery_start_hr": "12:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "TaksitliBorcTransferiKampanyasi_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "MobilChurnTeklifleri_SMS"},
     {"graph_prefix": "10126"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "8873"},
     {"IysId": "3065"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Sana ozel kredi limitini ogrenmek ister misin? Hemen Akbank Mobil'e gir, basvuru ve nakit ihtiyaclar menusune tikla, istedigin urune ait limitini ogrenerek kolayca basvurunu yap. Akbank Mobil icin: akbank.com.gat76t Detayli bilgi: akbank.com.Akbank-Mobil Ucretsiz SMS'lerimizi almak istemiyorsan 'smsistemiyorum' yazip 8885'e gonderebilirsin. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "39684|62394"},
     {"mgts_delivery_start_hr": "11:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "MobilChurnTeklifleri_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "OnonayliArtiPara_SMS"},
     {"graph_prefix": "10129"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9036"},
     {"IysId": "9033"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Degerli Akbankli, nakit ihtiyaclariniz icin 600 TL'ye kadar on onayli Arti Para'niz sizi bekliyor. Hemen basvurarak, limitinizi tanimlamak icin: www.akbank.com/artipara-basvuru. Detayli bilgi icin: 444 25 25. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304,59225,48779"},
     {"mgts_delivery_start_hr": "11:30"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "OnonayliArtiPara_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BireyselKKTaksitKampanyasi_SMS"},
     {"graph_prefix": "10134"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9089"},
     {"IysId": "9617"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Axess ile yapacaginiz harcamalariniz icin taksit firsatlari sizi bekliyor! Giyim'den elektronige, egitim ve vergi odemelerinden seyahat harcamalarina farkli sektorlerde size ozel taksit firsatlarini gormek ve hemen faydalanmaya baslamak icin Akbank Mobil - Juzdan uzerinden kampanyalara katilabilirsiniz. Hemen katilmak icin: www.axess.com.tr.mfc2 Detayli bilgi icin: www.axess.com.tr.11c6 Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AxsessKartSahibi"}, {"Seed_List": "34061|61556"},
     {"mgts_delivery_start_hr": "13:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BireyselKKTaksitKampanyasi_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BirebirAyricalikliVadeliMevduatFaiz_SMS"},
     {"graph_prefix": "10135"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "7730"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Sevgili Akbankli, yeni vadeli mevduat hesabi acarak 1e1 hizmet sundugumuz Akbanklilara ozel ayricalikli faiz oranindan yararlanabilirsiniz. Vadeli mevduat hesabinizi hemen acmak icin sizi akbank.com/vadeli-hesap sayfasina bekliyoruz. Detayli bilgi icin: akbank.com/vadeli-faiz-oranlari . Birebir Bankacilik hizmeti almanin diger ayricaliklari icin: Akbank.com/1e1AyricaliklarDunyasi. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|63191|60747|64325|61018"},
     {"mgts_delivery_start_hr": "12:51"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BirebirAyricalikliVadeliMevduatFaiz_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "BirebirBankacilikTanitimVideosu_SMS"},
     {"graph_prefix": "10138"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9113"},
     {"IysId": "9064"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Degerli Akbankli, Birebir Bankacilik'a hos geldiniz. Birebir Bankacilik'in ayricaliklarla dolu dunyasini incelemek icin tiklayabilirsiniz: https://akbank.com/ayricaliklar-dunyasi Tanitim videomuz ve detayli bilgi icin: https://akbank.com/Birebir Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Iyi gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|64325|63191"},
     {"mgts_delivery_start_hr": "13:55"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "BirebirBankacilikTanitimVideosu_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "AM30FazlaGundurLoginOlmayan_SMS"},
     {"graph_prefix": "10140"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "8934"},
     {"IysId": "0"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Sen yokken neler oldu, biliyor musun? Hemen Juzdan'a giris yaparak sana iyi gelecek teklifleri kesfet! www.axess.com.tr/2032 Ucretsiz sms almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "52965"},
     {"mgts_delivery_start_hr": "12:32"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "AM30FazlaGundurLoginOlmayan_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "AxessMobilYeniDownload_SMS"},
     {"graph_prefix": "10141"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "8934"},
     {"IysId": "0"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Hayatini kolaylastirmak ister misin? Tek yapman gereken Juzdan'i indirmek! Juzdan'a ozel firsatlarla daha cok Chip-Para kazanmak icin hemen uygulamamizi indir. www.axess.com.tr/bb37 Ucretsiz sms almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "52965"},
     {"mgts_delivery_start_hr": "12:30"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "AxessMobilYeniDownload_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "KKLimitArtirimi_SMS"},
     {"graph_prefix": "10052"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9089"},
     {"IysId": "1827"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Duzenli Limit artis talimatinizla ihtiyaciniz halinde limitinizin artirilmasini kolaylikla saglayabilirsiniz. Talimat vermek icin; TALIMAT bosluk TC Kimlik Numaranizi yazip 5990'a gondermeniz yeterlidir. (Ornek SMS: TALIMAT 12301230123) Ucretsiz SMS'lerimizi almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz.Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "62784|54365|34061"},
     {"mgts_delivery_start_hr": "11:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "KKLimitArtirimi_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "SozlesmesiBitenMaasLimitArtirim_SMS"},
     {"graph_prefix": "10145"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9089"},
     {"IysId": "1310"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Wings kartinizla limitinizi arttirmak cok kolay! LIMIT, kredi karti numaranizin son 4 hanesi, aylik net gelirinizi ve talep ettiginiz limiti aralarinda birer bosluk birakarak 4566'ya gonderin, degerlendirme sonucunuz SMS ile gelsin. (ORNEK SMS: LIMIT 1234 1300 3000) Detayli bilgi: 4442525 Ucretsiz SMS'lerimizi almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "WingsKartSahibi"}, {"Seed_List": "34061|64284"},
     {"mgts_delivery_start_hr": "14:00"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "SozlesmesiBitenMaasLimitArtirim_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "UcAyErtelemeliIhtiyacKredi_SMS"},
     {"graph_prefix": "10146"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9036"},
     {"IysId": "9664"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Degerli Akbankli, 3 aya kadar ertelemeli ihtiyac kredisi basvurunuzu Akbank Mobil ve Internet, 444 25 25 ve tum subelerimizden kolayca yapabilirsiniz. Hemen basvurmak icin: www.akbank.com/kredibasvuru Detayli bilgi icin: 444 25 25 Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mutlu gunler dileriz. Mersis:0015001526400497"},
     {"FromAlias": "AKBANK"}, {"Seed_List": "35304|49755|30944|48779|59225|64913"},
     {"mgts_delivery_start_hr": "15:16"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "UcAyErtelemeliIhtiyacKredi_SMS"}],

    [{"bucket_name": "Phase3 - SMS"},
     {"graph_name": "AxessAdLIsikTaksit_SMS"},
     {"graph_prefix": "10148"}, {"CustomerID": ""},
     {"mgts_content_type": "881"}, {"MgtsSmsBudgetUnit": "9691"},
     {"IysId": "9137"}, {"ToMobileNumber": "5555555555"},
     {
         "SMSContent": "Axess'e ozel adL ve adL.com.tr'de pesin fiyatina 7 aya varan taksit firsatini kacirmayin! Son gun: 28 Subat 2023 Detayli bilgi: www.axess.com.tr/99ab. Juzdan'i henuz indirmediyseniz tiklayin: www.axess.com.tr/d032. Ucretsiz SMS almak istemiyorsaniz 'smsistemiyorum' yazip 8885'e gonderebilirsiniz. Mersis:0015001526400497"},
     {"FromAlias": "AXESS"}, {"Seed_List": "64974|2827"},
     {"mgts_delivery_start_hr": "12:30"}, {"content_language": "0"},
     {"VALID_DAYS": "2"}, {"Treatment_Name": "AxessAdLIsikTaksit_SMS"}]
]


def return_cust_id_from_prefix(prefix):
    prefix = "'%" + prefix + "%'"
    customer_id = database.select("PGA_TMUSTERI_V", "MUSTERI_ID",
                                  "MUSTERI_ID LIKE " + prefix + "AND TARIH >SYSDATE-1 ORDER BY MUSTERI_ID DESC FETCH FIRST 1 ROWS ONLY")
    customer_id = str(customer_id).replace("[(", "")
    customer_id = str(customer_id).replace(",)]", "")
    return customer_id


def sms_check_operations():
    create_folder()
    pega.login_page()
    count = 0
    # Creating Datas
    for b_outcome in product_offer_outcome:
        bucket_name_tmp = str(b_outcome[0]['bucket_name'])
        graph_name_tmp = str(b_outcome[1]['graph_name'])
        prefix1_tmp = str(b_outcome[2]['graph_prefix'])

        creating_datas(bucket_name_tmp, graph_name_tmp)

        primary_customer_id_tmp = return_cust_id_from_prefix(prefix1_tmp)
        product_offer_outcome[count][3]['CustomerID'] = primary_customer_id_tmp
        print(primary_customer_id_tmp)
        count += 1

    # Running Batch
    running_ui()

    for b_outcome in product_offer_outcome:
        customer_id = b_outcome[3]['CustomerID']
        print(customer_id)
        database_check_sms(customer_id, b_outcome)


def change_web_window(window):
    # Go To New Window
    chrome.driver.switch_to.window(window)


def creating_datas(bucketName, graphName):
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


def database_check_sms(customer_id, b_outcome_temp):
    condition = "MUSTERI_ID = " + customer_id
    batch_output_data = database.select("PBO.BATCH_OUTPUT", "*", condition)
    # Caseid selected
    print(batch_output_data)
    # select * from PBO.BATCH_OUTPUT result = batch_output_data , b_outcome_temp = our list
    DB_CHECK.db_check_operations(batch_output_data, b_outcome_temp)


def main_operation():
    sms_check_operations()
    database.close_connection()
