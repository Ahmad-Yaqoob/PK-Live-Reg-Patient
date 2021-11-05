import time
import Links
import data
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def test():
    print("Now Loging with Admin to Change Preferences")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(Links.homepageURL)
    username = driver.find_element(By.ID, Links.loginID)
    username.send_keys(data.admloginID)
    password = driver.find_element(By.ID, Links.passwordID)
    password.send_keys(data.admPassword)
    driver.find_element(By.XPATH, Links.loginButtonXpath).click()
    time.sleep(1)
    print("Logged In with Admin")
    driver.find_element(By.ID, Links.anncFormID).click()
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.XPATH, Links.confgXpath).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Links.HFprefXpath).click()
    time.sleep(2)
    print("HF Preferences open")
    cnicCB = driver.find_element(By.ID, Links.pCNICID)
    time.sleep(2)
    print("CNIC Checked")
    scroll = ActionChains(driver)
    scroll.move_to_element(cnicCB)
    cnicCB.click()
    time.sleep(2)
    lNameCB = driver.find_element(By.ID, Links.pLastNameID)
    scroll.move_to_element(lNameCB)
    lNameCB.click()
    print("Last Name Checked")
    time.sleep(2)
    ecm = driver.find_element(By.ID, Links.pEmcID)
    scroll.move_to_element(ecm)
    ecm.click()
    print("Emp Status Checked")
    time.sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    driver.find_element(By.ID, Links.pDeptID).click()
    time.sleep(2)
    print("Dept Checked")
    driver.find_element(By.ID, Links.pSaveID).click()
    time.sleep(2)
    print("Preferences Saved")
    print("routing Back to Registration Page")