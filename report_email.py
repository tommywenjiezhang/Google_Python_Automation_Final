from datetime import date
import os
from reports import generate_report


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
    output = getNameAndWeight("./google_project","<br/>")
    today = date.today()
    today_str = today.strftime("%d %B, %Y")
    process_str = "Processed Update on {}".format(today_str)
    output_para = "".join(output)
    generate_report('./new.pdf',process_str,output_para)


