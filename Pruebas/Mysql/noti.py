import subprocess
import re
import smtplib

# List of 30 regex rules
regex_rules = [
    ".*error.*",
    ".*fail.*",
    ".*denied.*",
    ".*unauthorized.*",
    ".*unavailable.*",
    ".*warning.*",
    ".*alert.*",
    ".*critical.*",
    ".*exception.*",
    ".*fatal.*",
    ".*bad.*",
    ".*problem.*",
    ".*issue.*",
    ".*bug.*",
    ".*defect.*",
    ".*trouble.*",
    ".*disaster.*",
    ".*problematic.*",
    ".*inconsistent.*",
    ".*incorrect.*",
    ".*invalid.*",
    ".*wrong.*",
    ".*not correct.*",
    ".*not valid.*",
    ".*not working.*",
    ".*not functional.*",
    ".*not responding.*",
    ".*not accessible.*",
    ".*not available.*"
]

# Tshark command to capture and filter packets
tshark_cmd = "tshark -i wlan0 -l -T fields -e frame.protocols -e ip.src -e ip.dst"
#"tshark", "-i", "wlan0", "-l", "-T", "fields", "-e", "frame.protocols", "-e", "ip.src", "-e", "ip.dst"], stdout=subprocess.PIPE)
#tshark_process = subprocess.Popen(["tshark", "-i", "wlan0", "-l", "-T", "fields", "-e", "frame.protocols", "-e", "ip.src", "-e", "ip.dst"], stdout=subprocess.PIPE)
# Run the Tshark command and get the output
tshark_output = subprocess.run(tshark_cmd, capture_output=True, text=True, shell=True).stdout

# Split the Tshark output into lines
lines = tshark_output.splitlines()

# Loop through each line and check if it matches any of the regex rules
for line in lines:
    for regex in regex_rules:
        if re.search(regex, line):
            # If a match is found, send an email notification
            sender = "dbenitesi.db@gmail.com"
            receiver = "dbenitesi.db@gmail.com"
            message = "Subject: Tshark Alert\n\nA Tshark alert has been triggered:\n\n" + line
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, "aspoyxnanyzmraoo")
            server.sendmail(sender, receiver, message)
            server.quit()
