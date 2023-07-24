from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


# main module
if __name__ == "__main__":
    
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode (without opening browser window)

    # Set path to chromedriver executable
    try:
        chromedriver_path = r'C:\Users\trieu.pham\OneDrive - BTM Global Consulting\Projects\chromedriver'  # Replace with your actual path to chromedriver
    except:
        chromedriver_path = r'C:\Users\trieu.pham\OneDrive - BTM Global Consulting\Projects\chromedriver.exe'  # Replace with your actual path to chromedriver

    symbol = 'HOSE-VN30'

    # Start the WebDriver and open TradingView
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.tradingview.com/symbols/{symbol}/")
    print("Opened:", driver.title)
    # Wait for the page to load
    time.sleep(5)

    # Find and print the live price
    live_price_element = driver.find_element(By.CLASS_NAME, 'tv-symbol-price-quote__value')
    live_price = live_price_element.text
    print("Live Price:", live_price)

    # Find and print the percent change
    percent_change_element = driver.find_element(By.CLASS_NAME, 'tv-symbol-price-quote__percent')
    percent_change = percent_change_element.text
    print("Percent Change:", percent_change)

    # Close the WebDriver
    driver.quit()
    pass