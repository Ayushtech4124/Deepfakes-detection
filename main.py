import os
import time
import requests
import smtplib
import psutil
from email.mime.text import MIMEText

# Downloader Component
def download_file(url, local_filename):
    response = requests.get(url)
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded file saved as {local_filename}")

# Payload Component
def create_hidden_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    print(f"Hidden directory '{directory_name}' created")

def write_log_file(directory_name, log_filename, message):
    with open(os.path.join(directory_name, log_filename), 'a') as log_file:
        log_file.write(message + '\n')
    print(f"Log entry written to {log_filename}")

def read_sensitive_file(file_path, log_file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as sensitive_file:
            content = sensitive_file.read()
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"Sensitive file content: {content}\n")
        print(f"Sensitive file content logged")
    else:
        print(f"Sensitive file '{file_path}' not found")

def send_notification(email_address, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = email_address

    # Note: Replace 'smtp.example.com' with your SMTP server and configure as needed
    with smtplib.SMTP('smtp.example.com') as server:
        server.sendmail(email_address, [email_address], msg.as_string())
    print(f"Notification sent to {email_address}")

# System Behavior Check
def log_system_resource_usage(log_file_path, duration=60, interval=10):
    for _ in range(duration // interval):
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        with open(log_file_path, 'a') as log_file:
            log_file.write(f"CPU Usage: {cpu_usage}%, Memory Usage: {memory_info.percent}%\n")
        time.sleep(interval - 1)
    print("System resource usage logged")

def main():
    url = 'https://example.com/harmless.txt'
    local_filename = 'downloaded_file.txt'
    hidden_directory = '.trojan_files'
    log_filename = 'log.txt'
    sensitive_file = 'sensitive_info.txt'
    email_address = 'your_email@example.com'

    download_file(url, local_filename)
    create_hidden_directory(hidden_directory)
    log_file_path = os.path.join(hidden_directory, log_filename)
    write_log_file(hidden_directory, log_filename, 'This is a simulated Trojan log entry.')
    read_sensitive_file(sensitive_file, log_file_path)
    send_notification(email_address, 'Trojan Notification', 'This is a simulated exfiltration notification.')
    log_system_resource_usage(log_file_path)

    print("Script has completed running")

if __name__ == "__main__":
    main()