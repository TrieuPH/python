from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
### GECKODRIVER
from webdriver_manager.firefox import GeckoDriverManager

### CHROMDRIVER
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.utils import ChromeType

### IE
#from webdriver_manager.microsoft import IEDriverManager

### Calculate time execute code
from time import time

### Webdriver Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def openSite(url):
    options = Options()

    ## Set Headless true or false
    options.headless = True

    ## Service
    service = Service(GeckoDriverManager().install())
    ## Set time out
    timeout = 10
    ### USING CHROME
    #driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    ### USING IE
    #driver = webdriver.Ie(IEDriverManager().install())
    ### USING GECKODRIVER
    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options= options)

    s = GeckoDriverManager().install()
    driver = webdriver.Firefox(executable_path=s, options= options)

    ## Navigate web
    driver.get(url)

    driver.find_element_by_id("name").send_keys('080161')
    driver.find_element_by_id("txtPassword").send_keys("p%q!cPFG)qxu97>>")
    driver.find_element_by_id("btnLogin").click()
    
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'menu2')))
    except TimeoutException:
        print("Timed out waiting for page to load menu2")
    finally:
        print("Page loaded")    

    driver.get("https://webtrading.ssi.com.vn/#Portfolio_ListProperties")
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'hrefListProperties')))
    except TimeoutException:
        print("Timed out waiting for page to load hrefListProperties")
    finally:
        print("Porfolio loaded")  
      
    driver.get("https://webtrading.ssi.com.vn/#Portfolio_CapablityBuy")
    try:
        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, 'col-lg-3 col-md-3 col-sm-6 col-sx-12 portfolio_div')))
    except TimeoutException:
        print("Timed out waiting for page to load Porfolio status")
    finally:
        print("Porfolio status loaded")  
    
    total_equity = driver.find_element_by_id("0_FO_CM_PM_spanTotalEquity").text
    print("Total Equity: %s" % (total_equity))
    
    ## DELETE all Cookies
    driver.delete_all_cookies()
    ## Close driver
    driver.close()
    return total_equity

if __name__ == '__main__':
    start_time = time()
    url = 'https://webtrading.ssi.com.vn/Logon'
    temp = openSite(url).replace(".",",")
    print("New Total Equity: %s" %(temp))
    print("Time to run %s sec" % (time() - start_time))

