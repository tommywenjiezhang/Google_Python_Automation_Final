#!/usr/bin/env python3
import requests
import glob

url =  "http://localhost/upload/"
for image in glob.glob("./supplier-data/images/*.jpeg"):
    with open(image, 'rb') as  opened:
        r = requests.post(url, files = {'file': opened})
