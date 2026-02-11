import os
import requests
import sys
import time
import json

def validate_address(vat):

   url = "https://api.vatcomply.com/vat"
   params = {
       "vat_number": vat
   }



   r = requests.get(url, params=params)
   data = r.json()

   parsed = {
       'is_valid': data['valid'],
       'vat_number': data['vat_number'],
       "name": data['name'],
       "address": data['address'],
       "country_code": data['country_code'],
   }

   formatted_json = json.dumps(parsed, indent=4)

   return formatted_json









