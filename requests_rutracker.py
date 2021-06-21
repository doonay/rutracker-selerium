import time
import requests
import lxml.html as html
from bs4 import BeautifulSoup
from lxml import etree as et

login=''
password=''

main_page = 'https://rutracker.org/forum/'
#response = requests.get(main_page + 'index.php')

#POST запрос с логином
payload = {'login_username': login, 'login_password': password}
r = requests.post(main_page + 'index.php', data=payload)
print(r.text)

#r = requests.get(main_page + 'tracker.php')
#print(r.text)

# Используйте pretty_print = True для отступов в HTML

#Request URL: https://rutracker.org/forum/login.php
#Request Method: POST
#Location: https://rutracker.org/forum/index.php
#Set-Cookie: bb_session=0-17306222-CmMIAaJekRqOUST58COr; expires=Sat, 22-Feb-2031 12:03:18 GMT; Max-Age=315360000; path=/forum/; domain=.rutracker.org; secure; HttpOnly
#Cookie: bb_guid=pSVRgFmmuvXL; bb_ssl=1; bb_t=a%3A15%3A%7Bi%3A4824458%3Bi%3A1612045742%3Bi%3A6014364%3Bi%3A1614126906%3Bi%3A6008221%3Bi%3A1612972530%3Bi%3A5673367%3Bi%3A1612934861%3Bi%3A5782400%3Bi%3A1610139989%3Bi%3A5967431%3Bi%3A1611638035%3Bi%3A5988945%3Bi%3A1612376630%3Bi%3A5689401%3Bi%3A1612376940%3Bi%3A5593548%3Bi%3A1612456993%3Bi%3A5954170%3Bi%3A1612545486%3Bi%3A4569147%3Bi%3A1612679872%3Bi%3A5865831%3Bi%3A1612680592%3Bi%3A5691998%3Bi%3A1612532994%3Bi%3A5968965%3Bi%3A1612285065%3Bi%3A5989953%3Bi%3A1610886227%3B%7D; _ym_uid=1612348875210595871; _ym_d=1612348875; _ym_isad=2

#Upgrade-Insecure-Requests: 1
#User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
