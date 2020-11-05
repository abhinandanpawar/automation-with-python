from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from PIL import Image 
from selenium.webdriver.chrome.options import Options 


driver = webdriver.Chrome(ChromeDriverManager().install())  
#--------------------------------------headless code -------------------------------------------------
#importing end 
#options = Options()
#options.headless = True
#driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)  

#--------------------------------------headless code -------------------------------------------------

#function areana
#jumping on announcement 
def ann():
    a=driver.find_element_by_link_text("Announcement")
    a.click()
    driver.save_screenshot("Announcement.png")
    #image = Image.open("Announcement.png")
    #image.show()
    driver.back()
#jumping on Event
def event():
    a=driver.find_element_by_link_text("Events")
    a.click()
    driver.save_screenshot("Events.png")
    #image = Image.open("Events.png")
    #image.show()
    driver.back()
#jumping on job 
def job():
    a=driver.find_element_by_link_text("Jobs")
    a.click()
    driver.save_screenshot("Jobs.png")
    #image = Image.open("Jobs.png")
    #image.show()
    driver.back()

#login to the page

def login(username,password):
    driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="imgSubmit"]').click()


#this get method will direct to google.com 
driver.get("http://placement.bitmesra.ac.in")
print(driver.title)
print("Please Enter your Email")
username=input()
print("Please Enter your Password")
password=input()
#login page work 
login(username,password)
driver.maximize_window()
driver.save_screenshot("home.png")
#image = Image.open("home.png")
#image.show()

# taking user's choice 
ann()
event()
job()
time.sleep(5)
driver.quit()

