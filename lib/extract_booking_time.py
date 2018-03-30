import sys
import os
import re
from bs4 import BeautifulSoup
import base64

root_folder = sys.argv[1]
booking_html_filename = sys.argv[2]

htmlfilepath = os.path.join(root_folder,"target",booking_html_filename)

with open(htmlfilepath) as htmlfile:

    soup = BeautifulSoup(htmlfile.read(), 'html.parser')
    datetime_elem = soup.find("div",{"id":"content"}).div.fieldset.find_all("div")[1]
                
    print(datetime_elem.text)

exit(0)