import sys
import os
import re
from bs4 import BeautifulSoup

root_folder = sys.argv[1]
html_page_name = sys.argv[2]

htmlfilepath = os.path.join(root_folder,"target",html_page_name)

with open(htmlfilepath) as htmlfile:
    soup = BeautifulSoup(htmlfile.read(), 'html.parser')
    anchorelems = soup.find("div",{"id":"content"}).find_all("a",{"class":"arrow"})

    #First link is the url to the current month. So, start from second link
    print(anchorelems[1]["href"])

exit(0)

