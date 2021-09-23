import json
from selenium import webdriver

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account": ""
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')
#chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.get('https://merahindi.com/category/hindi-sentences/3')
#driver.get('https://omniglot.com/language/phrases/malayalam.php')
driver.get('https://ilearntamil.com/tamil-sentence-formation/')
#driver.get('file://C:/Users/goeln/Documents/intern/Mahindra_n_Mahindra/Demand_notice_POC/trial.html')
driver.execute_script('window.print();')
driver.quit()
