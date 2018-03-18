import sys
import os
import requests

#curl -v -F username=workingaccount -F password=qwe123 -F captchafile=@"/home/tapan/consulatecheck/captcha.jpg" http://api.dbcapi.me/api/captcha

imagepath = "/home/tapan/consulatecheck/captcha.jpg"
posturl = "http://api.dbcapi.me/api/captcha"

multipart_form_data = {
    'captchafile': open(imagepath, 'rb'),
    'username': ('', 'workingaccount'),
    'password': ('', 'qwe123')
}

response = requests.post('http://api.dbcapi.me/api/captcha', files=multipart_form_data)

import pprint
pprint.pprint(response.content)
