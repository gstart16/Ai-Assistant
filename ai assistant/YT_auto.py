from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Music:
    def __init__(self):
        # Use WebDriver Manager to install ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def play(self, query):
        """Search and play a video on YouTube."""
        self.driver.get("https://www.youtube.com/results?search_query=" + query)
        
        # Wait for the page to load
        time.sleep(3)  # Adjust as necessary

        # Find and click on the first video
        try:
            video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')
            video.click()

            # Wait for the video page to load completely
            time.sleep(5)  # Adjust as necessary to ensure the video loads

            print(f"Now playing: {query}")

        except Exception as e:
            print(f"An error occurred: {e}")

    def close_driver(self):
        """Close the browser."""
        self.driver.quit()