import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from links import github_urls
from config import gh_username, gh_password

# Initiate webdriver
driver = webdriver.Chrome()
# Navigate to userpage and login
driver.get("https://github.com/" + gh_username)
driver.find_element_by_link_text('Sign in').click()
driver.find_element_by_name('login').send_keys(gh_username)
driver.find_element_by_name('password').send_keys(gh_password)
driver.find_element_by_name('commit').click()

# Iterate through friends
for url in github_urls:
  github_handle = url.split('/')[-1]

  try:
    driver.get(url)
    time.sleep(0.5)
  except:
    print('ERROR: Invalid URL:' + url)
    continue
  
  try:
    driver.find_elements_by_xpath("//button[@aria-label='Follow this person']")[1].click()
    print('SUCCESS: added ' + github_handle + "'s Github")
  except:
    print('WARNING: ' + github_handle + "'s Github handle may be incorrect or, you are already following them")
  time.sleep(0.5)

driver.close()