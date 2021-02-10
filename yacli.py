#!/usr/bin/env python3
import requests
import json
import sys

def curl(data, URL):
	agent = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36",
		"Accept-Language": "ru,ru-RU;q=0.9,en-US;q=0.8,en;q=0.7,ro;q=0.6,pt;q=0.5,de;q=0.4,bg;q=0.3",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Connection": "keep-alive"
	}

	s = requests.Session()
	response = s.post(URL, headers=agent, data=data)
	return response.text

def main(args):
	trans = "ru-en"
	if len(args)==3:
		trans=args[2]

	if len(args)>1:
		word=args[1]
	else:
		return False
	
	SessionID="51782baa.6021c46e.4fbb1883.74722d74657874-6-0"
	URL = f"https://translate.yandex.net/api/v1/tr.json/translate?id={SessionID}&srv=tr-text&lang={trans}&reason=auto&format=text"

	r = curl({"text":word,"options":4}, URL)
	return json.loads(r)["text"][0]

print(main(sys.argv))