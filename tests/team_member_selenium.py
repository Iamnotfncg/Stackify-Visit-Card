import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestTeamPage(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:3000")

    def test_success_team_page(self):
        team_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "team-button"))
        )
        team_button.click()

        self.assertEqual(self.driver.current_url, "http://localhost:3000")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome to Stackify')]"))
        )
        text_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Welcome to Stackify')]")
        self.assertEqual(text_element.text, "Welcome to Stackify")

    def test_invalid_team_page(self):
        team_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "team-button"))
        )
        team_button.click()

        self.assertEqual(self.driver.current_url, "http://localhost:3000/team")

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Ihor Hudzyk')]"))
        )
        text_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Ihor Hudzyk')]")
        self.assertEqual(text_element.text, "Ihor Hudzyk")

if __name__ == "__main__":
    unittest.main()