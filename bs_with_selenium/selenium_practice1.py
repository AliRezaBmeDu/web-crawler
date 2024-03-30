# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

driver.get("https://finance.yahoo.com/quote/TSLA/history?p=TSLA")
js_content = driver.page_source

soup = BeautifulSoup(js_content, "html.parser")

# # Find all HTML elements with the class attribute
# elements_with_class = soup.find_all(class_=True)

# # Extract and print the class names
# for element in elements_with_class:
#     class_names = element.get('class')
#     if class_names:
#         print("Class Names:", class_names)
        
# Wait for the element with the text 'Mar 30, 2023 - Mar 30, 2024' to be clickable
element_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Mar 30, 2023 - Mar 30, 2024')]")))

# Click on the element
element_1.click()

# Wait for the element with the text 'Max' to be clickable
element_2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Max')]")))
    
# Click on the element
element_2.click()

# Wait for the element with the text 'Download' to be clickable
element_3 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Download')]")))
    
# Click on the element
element_3.click()
# Find the HTML element with the content text 'download'
# max_elements = soup.find_all(string='Mar 30, 2023 - Mar 30, 2024')

# print('.........length of max elements: ', len(max_elements))
# # If the element with content text 'download' is found, get its parent element and retrieve the id attribute
# if max_element:
#     max_element = max_element.parent
#     max_id = max_element.get('id')
#     if max_id:
#         print("ID of the element with content text 'download':", max_id)
#     else:
#         print("No ID attribute found for the element with content text 'download'")
# else:
#     print("Element with content text 'download' not found")
    

# # Find all occurrences of the content text 'Download'
# download_elements = soup.find_all(text='Download')

# # Count the number of elements containing the text 'Download'
# num_download_elements = len(download_elements)

# print("Number of elements with content text 'Download':", num_download_elements)

driver.quit()