import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class WordPressDarkModeTests(unittest.TestCase):
    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.wp_admin_url = "https://your-wordpress-site/wp-admin"
        self.username = "your_username"
        self.password = "your_password"

    def login(self):
        # Login to WordPress admin
        driver = self.driver
        driver.get(self.wp_admin_url)

        # Fill in the login form
        self.wait.until(EC.visibility_of_element_located((By.ID, "user_login"))).send_keys(self.username)
        self.wait.until(EC.visibility_of_element_located((By.ID, "user_pass"))).send_keys(self.password)
        self.wait.until(EC.element_to_be_clickable((By.ID, "wp-submit"))).click()

    def check_and_install_wp_dark_mode(self):
        # Navigate to the Plugins page
        driver = self.driver
        driver.get(self.wp_admin_url + "/plugins.php")

        # Check if "WP Dark Mode" is installed and active
        if "WP Dark Mode" not in driver.page_source:
            # Install and activate the plugin if not found
            driver.get(self.wp_admin_url + "/plugin-install.php")
            self.wait.until(EC.visibility_of_element_located((By.ID, "plugin-search-input"))).send_keys("WP Dark Mode")
            self.wait.until(EC.element_to_be_clickable((By.ID, "search-submit"))).click()
            # Find and install the plugin
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Install Now']"))).click()
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Activate']"))).click()

    def test_dark_mode_configuration(self):
        driver = self.driver
        self.login()
        self.check_and_install_wp_dark_mode()

        # Enable Admin Dashboard Dark Mode
        driver.get(self.wp_admin_url + "/admin.php?page=wp-dark-mode-settings")
        self.wait.until(EC.element_to_be_clickable((By.ID, "enable_admin_dark_mode"))).click()

        # Check if Dark Mode is active by checking background color or a specific icon
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "body.dark-mode")))
        dark_mode_active = self.driver.find_element(By.CSS_SELECTOR, "body").get_attribute("class")
        self.assertTrue("dark-mode" in dark_mode_active)

    def tearDown(self):
        # Close the browser after tests
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
