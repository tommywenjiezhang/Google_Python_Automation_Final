#!/usr/bin/env python3

from datetime import date
import os
from reports import generate_report
from emails import generate_email,send


sender = 'automation@example.com'
to = 'username@example.com'
email_body = "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
attachment = '/tmp/processed.pdf'
input_path = "./"

def getNameAndWeight(input_path, sep):
    output = []
    for f in os.listdir(input_path):
        with open(os.path.join(input_path, f), "r") as txtFile:
            lines = iter(txtFile.readlines())
            name = next(lines)
            weight = next(lines)
            outstr = f"name: {name}{sep}{sep}weight: {weight}{sep}{sep}{sep}"
            output.append(outstr)
    return output


if __name__ == "__main__":
    output = getNameAndWeight(input_path,"<br/>")
    today = date.today()
    today_str = today.strftime("%d %B, %Y")
    process_str = "Processed Update on {}".format(today_str)
    output_para = "".join(output)
    generate_report(attachment,process_str,output_para)
    email = generate_email(sender,to ,email_body ,attachment)
    send(email)


