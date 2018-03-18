import sys
import os
import re
import pprint

searchkey = sys.argv[1]
querygroups = sys.argv[2].split('&')
for group in querygroups:
    tokens=group.split("=")
    if(len(tokens) == 2 and tokens[0] == searchkey):
        print(tokens[1])


