import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

if __name__ == "__main__":
    ''' #test func on lib.py file
    from lib import writtingjson, readingjson
    writtingjson()
    readingjson()
    '''
    # Options for chromedriver
    options = webdriver.ChromeOptions()

    print("Choose option:")
    print("Option 1: Open Chrome")
    print("Option 2: Without Open Chrome")
    print("Your choice: ")
    input = int(input())
    if input == 1:
        options.add_argument("headless")
        options.add_argument("disable-gpu")
        pass
    elif input == 2:
        pass
    else:
        print("Please choose 1 or 2")
        pass
    #options.add_argument("headless")
    #options.add_argument("disable-gpu")
    # Set up driver
    try:
        driver = webdriver.Chrome(executable_path="./resources/chromedriver", options=options)
        # Go to Url
        driver.get("https://webtrading.ssi.com.vn/")
    except WebDriverException as er:
        print(er)
        pass
    
    
    pass