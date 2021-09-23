from base64 import b64decode
import time
from selenium import webdriver
import chromedriver_binary

#options = webdriver.ChromeOptions()
#options.add_argument("--headless")
#driver = webdriver.Chrome()#(options=options)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--window-size=1420,1080')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://omniglot.com/language/phrases/malayalam.php')

#a = driver.find_element_by_css_selector("#loanamountslider")
#webdriver.ActionChains(driver).click(
#    a).click_and_hold().move_by_offset(0, 0).perform()

a = driver.execute_cdp_cmd(
    "Page.printToPDF", {"path": 'html-page.pdf', "format": 'A4'})
#print(a)

b64 = a['data']

bytes = b64decode(b64, validate=True)


if bytes[0:4] != b'%PDF':
    raise ValueError('Missing the PDF file signature')

f = open('file.pdf', 'wb')
f.write(bytes)
f.close()

while True:
    time.sleep(1000)
