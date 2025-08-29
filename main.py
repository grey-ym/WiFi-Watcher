# Description: This script monitors a network for a specific device using its MAC address via SNMP

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import time
import datetime

# Email settings
sender_email = "sender@yahoo.com" # Replace with your email
receiver_email = "receiver@example.ru" # Replace with recipient email
password = "udvgafwtazvzvsgssd" # Replace with your email password
sleep_time = 30 # Time to wait between scans in seconds

current_time = datetime.datetime.now().time()

# Replace with the MAC address of the device to monitor
target_mac_address = "c:2f:b0:6d:87:d2" 


def send_email(message):
    # Creating the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "SNMP Alert: Target Device Connected"

    # Message body
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Email sending process
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}") 


def scan_for_mac():
    # SNMP command to scan the network
    snmp_command = ["snmpwalk", "-v", "2c", "-c", "vnc", "192.168.1.1"] # Replace with your SNMP community and router IP

    try:
        # Executing the SNMP command
        result = subprocess.run(snmp_command, capture_output=True, text=True)
        if result.returncode == 0:
            output = result.stdout
            print("Scan completed successfully") 

            if target_mac_address.lower() in output.lower(): # Searching for the target MAC address in the output
                message = f"The device Galaxy A70 connected to the network" # Customize the message as needed
                send_email(message)
                print(message)
            else:
                print(f"Target device not found in the network")

        else:
            print("Error executing SNMP command:", result.stderr)

    except Exception as e:
        print(f"Error executing snmpwalk command: {e}")

# Main loop to continuously scan the network
while True:
    print(f"Scanning the network and looking for the device with the specified MAC address {current_time}")
    scan_for_mac()

    # Waiting before the next scan
    time.sleep(sleep_time)
