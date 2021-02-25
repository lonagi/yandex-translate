#!/usr/bin/env python3
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import sys, time

def main(args):
	trans = "ru-en"
	if len(args)==3:
		trans=args[2]

	if len(args)>1:
		word=args[1]
	else:
		return False

	chrome = ChromeDriverManager(log_level=0, print_first_line=False).install()
	o = Options()
	headless = False
	o.headless = headless
	o.add_argument('--no-sandbox')
	o.add_argument('--disable-dev-shm-usage')
	driver = WebDriver(chrome, options=o)
	URL = f"https://translate.yandex.ru/?lang={trans}&text={word}"
	driver.get(URL)
	time.sleep(3)
	elem = driver.find_element_by_css_selector("#translation > span > span")
	driver.close()
	return elem.text

print(main(sys.argv))