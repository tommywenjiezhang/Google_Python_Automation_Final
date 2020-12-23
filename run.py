#! /usr/bin/env python3
import os
import requests
import re


dir="./supplier-data/descriptions/"
url= "http://34.69.16.100/fruits/"

for file in os.listdir(dir):
    tipos = ["name","weight","description"]
    datos = {}
    print(file)
    with open(os.path.join(dir,file),"r") as txtfile:
        x = 0
        for line in txtfile:
            if x <= 2 and "description":
                datos[tipos[x]] =  line.rstrip("\n")
                if re.search(r"([0-9]+) lbs", line.rstrip("\n")):
                    datos[tipos[x]] = int(re.search(r"([0-9]+) lbs",line.rstrip("\n")).group(1)) 
            x += 1
    ext = os.path.splitext(file)[0]
    datos["image_name"] = ext +  ".jpeg"
    print(datos)
    response = requests.post(url,json=datos)
    print(response.status_code)
    if response.status_code != requests.codes.ok:
        response.raise_for_status()
