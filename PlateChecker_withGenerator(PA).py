import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


vary = False
# takes user input for parameters to be used for plate generation
print("Valid plate characters are: A-Z, 0-9, -, and a space\nenter 'all' for all characters")
chars = input("Enter characters to be used: ")
if chars == "all":
   chars = "abcdefghijklmnopqrstuvwxyz01234567890- "
print("A plate can contain up to seven characters plus a space or dash.")
digitMin = input("Enter the min amount of digits: ")
digitMax = input("Enter the max amount of digits: ")

x = input("Enter number of strings to generate: ")
print("Enter a filename, ex 'output.txt' file will be outputted to same folder as script")
filename = input("Input name for output file:")
# creates output files. output 1 is the initial output of random strings, output 2 contains plates considered valid
output = open(filename,"w+")
output2 = open(filename+"2", "w")
def range2(min, max,repeat):
   x = repeat
   for x in range(x):
      c = random.randint(min, max)
      if c == 0:
         rand = random.choices(chars, k=0)
      if c == 1:
         rand = random.choices(chars, k=1)
         if "-" not in rand and " " not in rand:
            print(''.join(rand))
            output.write(''.join(rand))
            output.write("\n")
      if c == 2:
         rand = random.choices(chars, k=2)
         if "-" not in rand and " " not in rand:
            print(''.join(rand))
            output.write(''.join(rand))
            output.write("\n")
      if c == 3:
         rand = random.choices(chars, k=3)
         if rand[0] != " " and rand[0] != "-" and rand[2] != " " and rand[2] != "-":
            if " " and "-" in rand:
               sleep(.1)
            else:
               print(''.join(rand))
               output.write(''.join(rand))
               output.write("\n")
      if c == 4:
         rand = random.choices(chars, k=4)
         if rand[0] != " " and rand[0] != "-" and rand[3] != " " and rand[3] != "-":
            if " " and "-" in rand:
               sleep(.1)
            else:
               print(''.join(rand))
               output.write(''.join(rand))
               output.write("\n")
      if c == 5:
         rand = random.choices(chars, k=5)
         if rand[0] != " " and rand[0] != "-" and rand[4] != " " and rand[4] != "-":
            if " " and "-" in rand:
               sleep(.1)
            else:
               print(''.join(rand))
               output.write(''.join(rand))
               output.write("\n")
      if c == 6:
         rand = random.choices(chars, k=6)
         if rand[0] != " " or rand[0] != "-" and rand[5] != " " or rand[5] != "-":
            if " " and "-" in rand:
               sleep(.1)
            else:
               print(''.join(rand))
               output.write(''.join(rand))
               output.write("\n")
      if c == 7:
         rand = random.choices(chars, k=7)
         if rand[0] != " " or rand[0] != "-" and rand[6] != " " or rand[6] != "-":
            if " " and "-" in rand:
               sleep(.1)
            else:
               print(''.join(rand))
               output.write(''.join(rand))
               output.write("\n")
      if c == 8:
         rand = random.choices(chars, k=8)
         if rand[0] != " " and rand[0] != "-" and rand[7] != " " and rand[7] != "-":
            if "-" or " " in rand:
               if "-" and " " in rand:
                  sleep(.1)
               else:
                  print(''.join(rand))
                  output.write(''.join(rand))
                  output.write("\n")
range2(int(digitMin),int(digitMax),int(x))

options = webdriver.ChromeOptions()
options.add_argument('--headless')
headless = input("headless browser window? (y/n): ")
if headless == "y":
   driver = webdriver.Chrome(options=options)
if headless == "n":
    driver = webdriver.Chrome()




# opens a chrome window using selenium, and makes it headless


# opens the site, and navigates to the correct page
driver.get("https://www.dmv.pa.gov/VEHICLE-SERVICES/Registration%20Plates/Pages/Personalized%20Availability.aspx")
sleep(1)
button1 = driver.find_element(By.LINK_TEXT,"CHECK PERSONALIZED PLATE AVAILABILITY").click()
sleep(1)
driver.close()
driver.switch_to.window(driver.window_handles[0])
button2 = driver.find_element(By.ID,"standard").click()
button3 = driver.find_element(By.NAME,"continueButton").click()
button4 = driver.find_element(By.LINK_TEXT,"Passenger").click()

# closes and re-opens output to be used as input for site
output.close()
output3 = open(filename,"r")

# reads the output of the generated list
h = output3.readlines()


def check(c): # this function determines the number of characters in a string, and inputs them as such.
   # (the characters need to be inputted individually because each character is its own field on the website for whatever reason)

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

   driver.find_element(By.ID, "9").click()
   sleep(1) #gives the page a second to catch up
   Av = driver.find_element(By.ID, "A").is_displayed() # determines if the plate is available or not
   driver.find_element(By.ID, "1").clear() # clears each field
   driver.find_element(By.ID, "2").clear()
   driver.find_element(By.ID, "3").clear()
   driver.find_element(By.ID, "4").clear()
   driver.find_element(By.ID, "5").clear()
   driver.find_element(By.ID, "6").clear()
   driver.find_element(By.ID, "7").clear()
   driver.find_element(By.ID, "8").clear()

#prints if the plate is available or not, and records valid plates to txt file.
   if Av == True:

      output2.write(str.rstrip(c))
      output2.write("\n")
      print(str.rstrip(c + "Is Valid!"))
      output2.flush()
   else:
      print(str.rstrip(c + "Is Invalid!"))

# runs the above function for every line in the file.
for c in h: check(c)

output2.close()


















