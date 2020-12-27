import psutil
from emails import generate_email, send
import socket
import time
import shutil

total, used, free = shutil.disk_usage("/")

if __name__ == "__main__":
    cpu_percent = psutil.cpu_percent()
    disk_usage = used/ total
    p = psutil.Process()
    memory_usage = p.memory_full_info().rss / (1024 ** 2)
    host_ip = socket.gethostbyname("localhost")
    sender = "automation@example.com"
    to = "username@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    while(True):
        time.sleep(60)
        if cpu_percent > 0.8:
            message = "Error - CPU usage is over 80%"
            email = generate_email(sender, to, message, body)
            send(email)
        elif disk_usage < 0.2:
            message =  "Error - Available disk space is less than 20%"
            email = generate_email(sender, to,message, body)
            send(email)
        elif memory_usage < 500:
            message = "Error - Available memory is less than 500MB"
            email = generate_email(sender, to, message , body )
            send(email)
        elif host_ip != '127.0.0.1':
            message = "Error - Available memory is less than 500MB"
            email = generate_email(sender, to, message, body )
            send(email)