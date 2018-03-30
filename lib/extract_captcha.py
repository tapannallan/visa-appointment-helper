import sys
import os
import re
from bs4 import BeautifulSoup
import base64

root_folder = sys.argv[1]
captcha_file = sys.argv[2]
captcha_selector_id = sys.argv[3]

print(root_folder,captcha_file,captcha_selector_id)
htmlfilepath = os.path.join(root_folder,"target",captcha_file)
outputfile = os.path.join(root_folder,"target","captcha.jpg")
base64img = None

with open(htmlfilepath) as htmlfile:

    soup = BeautifulSoup(htmlfile.read(), 'html.parser')
    image_style = soup.find("form",{"id":captcha_selector_id}).div.captcha.div['style']
                
    m = re.match("background:white url\('data:image/jpg;base64,(.+)'\).*", image_style)
    if(m):
        base64img = m.groups(0)[0]
    else:
        #log error
        exit(1)

#save to jpg file
with open(outputfile,"wb") as op:
    jpg_recovered = base64.b64decode(base64img.encode('utf-8'))
    op.write(jpg_recovered)
