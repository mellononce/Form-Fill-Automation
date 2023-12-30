from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import time

# Path to your geckodriver
geckodriver_path = r'C:\Users\miller\Documents\geckodriver-v0.33.0-win64\geckodriver.exe'

# Setup WebDriver with Service
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)
driver.get("https://www.roboform.com/filling-test-all-fields")

# Fill out the form fields
# Replace 'field_name' and 'value' with the actual field names and values you want to input
try:
    driver.find_element(By.NAME, "01___title").send_keys("Ms.")
    driver.find_element(By.NAME, "02frstname").send_keys("Jessica")
    driver.find_element(By.NAME, "03middle_i").send_keys("H.")
    driver.find_element(By.NAME, "04lastname").send_keys("Miller")
    driver.find_element(By.NAME, "04fullname").send_keys("Jessica H. Miller")
    driver.find_element(By.NAME, "05_company").send_keys("Advii Treuhand KLG")
    driver.find_element(By.NAME, "06position").send_keys("CEO")
    driver.find_element(By.NAME, "10address1").send_keys("Beispielstrasse 76")
    driver.find_element(By.NAME, "13adr_city").send_keys("Nirgendwo")
    driver.find_element(By.NAME, "14adrstate").send_keys("Zürich")
    driver.find_element(By.NAME, "16addr_zip").send_keys("7777")
    driver.find_element(By.NAME, "23cellphon").send_keys("+41791234567891")
    driver.find_element(By.NAME, "24emailadr").send_keys("jessica.miller@gmail.com")
    driver.find_element(By.NAME, "66mm").send_keys("Jan")
    driver.find_element(By.NAME, "67dd").send_keys("08")
    driver.find_element(By.NAME, "68yy").send_keys("2000")
    # driver.find_element(By.NAME, "another_field_name").send_keys("Value for another field")

    # Wait to see filled fields before closing
    time.sleep(10)

except Exception as e:
    print("An error occurred:", e)

finally:
    driver.quit()
