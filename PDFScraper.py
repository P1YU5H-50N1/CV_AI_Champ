from selenium import webdriver
import time
#Script to get 50 the pdfs frome LinkedIn

options = webdriver.ChromeOptions() 

DOWNLOAD_DIR = '<DOWNLOAD DIRECTORY>'

prefs = {"download.default_directory": DOWNLOAD_DIR,"download.prompt_for_download": False}
options.add_experimental_option("prefs", prefs)

CHROME_EXECUTABLE = '<CHROME_EXECUTABLE>'

driver = webdriver.Chrome(CHROME_EXECUTABLE,options=options)
driver.maximize_window()
driver.get('https://www.linkedin.com/login')

PAUSE_TIME = 3

Email = '<LINKEDIN EMAIL>'
Password = '<LINKEDIN PASSWORD>'

EmailInput = driver.find_element_by_xpath('//*[@id="username"]')
EmailInput.send_keys(Email)
PasswordInput = driver.find_element_by_xpath('//*[@id="password"]')
PasswordInput.send_keys(Password)
SubmitButton = driver.find_element_by_css_selector('button[type="submit"]')
SubmitButton.click()

time.sleep(PAUSE_TIME)
driver.execute_script('window.stop()')

ConnectionPageURL = 'https://www.linkedin.com/mynetwork/invite-connect/connections/'
driver.get(ConnectionPageURL)


# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


ProfileLinkElements = driver.find_elements_by_class_name('mn-connection-card__picture')
AllProfileLinks = [element.get_attribute('href') for element in ProfileLinkElements]
ProfileLinks = AllProfileLinks[0:50]

#The program is paused in many steps because LinkedIn might block the request which occurs in milliseconds or seems automated
for Link in ProfileLinks:
    driver.get(Link)
    time.sleep(PAUSE_TIME)
    MoreButton = driver.find_element_by_class_name('pv-s-profile-actions__overflow-toggle')
    MoreButton.click()
    time.sleep(1)
    action = webdriver.common.action_chains.ActionChains(driver)
    action.move_to_element_with_offset(MoreButton, 0, 85)
    action.click()
    action.perform()
    time.sleep(30)
    
driver.quit()