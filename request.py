# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 23:45:59 2021

@author: HT-ICT
"""

import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':5, 'sales_in_first_month':200, 'sales_in_second_month':400})

print(r.json())