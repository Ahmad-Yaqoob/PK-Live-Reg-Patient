import Links
import Preferences
import data
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get(Links.homepageURL)
print("Login Page displayed")
username = driver.find_element(By.ID, Links.loginID)
username.send_keys(data.asstloginID)
if username.is_displayed():
    print("Username entered")
password = driver.find_element(By.ID, Links.passwordID)
password.send_keys(data.asstpassword)
if password.is_displayed():
    print("Password Entered")
driver.find_element(By.XPATH, Links.loginButtonXpath).click()
print("Login Button Clicked")
time.sleep(5)
driver.find_element(By.XPATH, Links.RegbuttXpath).click()
header = driver.find_element(By.XPATH, '//*[@id="header"]/h2')
if header.is_displayed():
    print("Registration Page Displayed")

def regForm():
    firstName = driver.find_element(By.ID, Links.fNameID)
    randstring = ''.join(random.choices(string.ascii_uppercase, k=6))
    firstName.send_keys(randstring)
    print("First Name Entered")
    lastName = driver.find_element(By.ID, Links.lNameID)
    randstring = ''.join(random.choices(string.ascii_uppercase, k=6))
    lastName.send_keys(randstring)
    print("Last Name Entered")
    mobileNo = driver.find_element(By.ID, Links.mNoID)
    randstring = ''.join(random.choices(string.digits, k=14))
    mobileNo.send_keys(randstring)
    print("Mobile No Entered")
    cnic = driver.find_element(By.ID, Links.cnicID)
    randstring = ''.join(random.choices(string.digits, k=14))
    cnic.send_keys(randstring)
    print("CNIC Entered")
    driver.find_element(By.ID, Links.stateID).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Links.stateNameID).click()
    print("state name Selected")
    time.sleep(2)
    driver.find_element(By.ID , Links.cityID).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Links.cityNameID).click()
    print("City Name Selected")
    time.sleep(2)
    cPerson = driver.find_element(By.ID, Links.cPersonID)
    randstring = ''.join(random.choices(string.ascii_uppercase, k=6))
    cPerson.send_keys(randstring)
    print("Contact Person Name Entered")
    cPersonMobID = driver.find_element(By.ID, Links.cPersonMobID)
    randstring = ''.join(random.choices(string.digits, k=14))
    cPersonMobID.send_keys(randstring)
    print("Contact Person Mobile No entered")
    driver.find_element(By.ID, Links.cPersonRelID).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Links.cPersonRelNameXpath).click()
    print("Contact Person Relation Selected")
    driver.find_element(By.ID, Links.empStatusID).click()
    time.sleep(2)
    driver.find_element(By.XPATH, Links.empStatusNameXpath).click()
    print("Employee Status Selected")
    driver.find_element(By.ID, Links.empDeptID).click()
    print("Employee status Department selected")
    time.sleep(2)
    driver.find_element(By.XPATH, Links.empDeptNameXpath).click()
    print("Employee Department Name Selected")
    driver.find_element(By.ID, Links.proceedID).click()
    time.sleep(2)
    thankyou = driver.find_element(By.ID, Links.regCmpID)
    if thankyou.is_displayed():
        print("Registration without Mandatory preference Completed")
    else:
        print("Registration Failed")
    driver.find_element(By.ID, "_SignUp_WAR_CloudClinikportlet_:assistantConfirmation:okBtn").click()
    time.sleep(2)


regForm()
Preferences.test()
driver.refresh()
regForm()
print("Registration With Mandatory Preferences Completed")