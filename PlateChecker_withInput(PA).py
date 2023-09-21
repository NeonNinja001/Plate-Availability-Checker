from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--headless')


inputFilePath = input(str("Enter input .txt file path: "))
outputFilePath = input("Enter output . txt file path: ")

output2 = open(outputFilePath, "w")
headless = input("Headless browser window? (y/n): ")

if headless == "y":
   driver = webdriver.Chrome(options=options)
if headless == "n":
    driver = webdriver.Chrome()



driver.get("https://www.dmv.pa.gov/VEHICLE-SERVICES/Registration%20Plates/Pages/Personalized%20Availability.aspx")
sleep(1)
button1 = driver.find_element(By.LINK_TEXT,"CHECK PERSONALIZED PLATE AVAILABILITY").click()
sleep(1)
driver.close()
driver.switch_to.window(driver.window_handles[0])
button2 = driver.find_element(By.ID,"standard").click()
button3 = driver.find_element(By.NAME,"continueButton").click()
button4 = driver.find_element(By.LINK_TEXT,"Passenger").click()
j = open(inputFilePath,"r")
h = j.readlines()
def check(c):
    if len(c) == 1:
        driver.find_element(By.ID, "1").send_keys(c[0])
    elif len(c) == 2:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
    elif len(c) == 3:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
    elif len(c) == 4:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
        driver.find_element(By.ID, "4").send_keys(c[3])
    elif len(c) == 5:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
        driver.find_element(By.ID, "4").send_keys(c[3])
        driver.find_element(By.ID, "5").send_keys(c[4])
    elif len(c) == 6:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
        driver.find_element(By.ID, "4").send_keys(c[3])
        driver.find_element(By.ID, "5").send_keys(c[4])
        driver.find_element(By.ID, "6").send_keys(c[5])
    elif len(c) == 7:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
        driver.find_element(By.ID, "4").send_keys(c[3])
        driver.find_element(By.ID, "5").send_keys(c[4])
        driver.find_element(By.ID, "6").send_keys(c[5])
        driver.find_element(By.ID, "7").send_keys(c[6])
    elif len(c) == 8:
        driver.find_element(By.ID, "1").send_keys(c[0])
        driver.find_element(By.ID, "2").send_keys(c[1])
        driver.find_element(By.ID, "3").send_keys(c[2])
        driver.find_element(By.ID, "4").send_keys(c[3])
        driver.find_element(By.ID, "5").send_keys(c[4])
        driver.find_element(By.ID, "6").send_keys(c[5])
        driver.find_element(By.ID, "7").send_keys(c[6])
        driver.find_element(By.ID, "8").send_keys(c[7])

    driver.find_element(By.ID,"9").click()
    sleep(1)
    Av = driver.find_element(By.ID,"A").is_displayed()
    driver.find_element(By.ID,"1").clear()
    driver.find_element(By.ID, "2").clear()
    driver.find_element(By.ID, "3").clear()
    driver.find_element(By.ID, "4").clear()
    driver.find_element(By.ID, "5").clear()
    driver.find_element(By.ID, "6").clear()
    driver.find_element(By.ID, "7").clear()
    driver.find_element(By.ID, "8").clear()


    if Av == True:

        output2.write(str.rstrip(c))
        output2.write("\n")
        print(str.rstrip(c+"Is Valid!"))
        output2.flush()
    else:
        print(str.rstrip(c+"Is Invalid!"))

for c in h: check(c)
output2.close()
