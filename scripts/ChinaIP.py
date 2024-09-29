'''
Author: Ness
Date: 2024-09-29 15:53:24
LastEditors: Ness
LastEditTime: 2024-09-29 15:52:20
FilePath: /ASN-China/syncIP.py


Copyright © 2022 by Ness, All Rights Reserved. 
'''

import requests

allChina = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china.list"

v4China = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china4.list"

v6China = "https://raw.githubusercontent.com/cbuijs/ipasn/master/country-asia-china6.list"

r = requests.get(allChina) 
with open("IP.China.list", "wb") as allChinaIP:
         allChinaIP.write(r.content)

r = requests.get(v4China) 
with open("IPv4.China.list", "wb") as v4ChinaIP:
         v4ChinaIP.write(r.content)

r = requests.get(v6China) 
with open("IPv6.China.list", "wb") as v6ChinaIP:
         v6ChinaIP.write(r.content)
