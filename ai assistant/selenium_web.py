from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Inflow:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_info(self, query):
        self.query = query
        # Navigate to Wikipedia
        self.driver.get("https://www.wikipedia.org")
        #search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')

        # Find the search input field and enter the query
        search_input = self.driver.find_element(By.NAME, "search")
        search_input.send_keys(self.query)

        # Submit the search form
        search_input.submit()

        # Wait for the page to load (you can use WebDriverWait for better practice)
        time.sleep(3)  # Adjust time as needed

        # Get the title of the page as an example of information retrieval
        page_title = self.driver.title
        print(f"Page Title: {page_title}")

    def close_driver(self):
        self.driver.quit()

# Instantiate the Inflow class and call get_info
'''assist = Inflow()
assist.get_info("neutron star")

# Keep the window open until user decides to close it
input("Press Enter to close the browser...")  # Wait for user input before closing

assist.close_driver()'''