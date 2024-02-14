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
    ".*SYN.*"
]

def run_tshark():
    tshark_process = subprocess.Popen(["tshark", "-i", "1", "-Y", "'tcp.flags.syn == 1 and tcp.flags.ack == 0'"], stdout=subprocess.PIPE)
    
    lines = tshark_process.stdout.readline()
    lines = lines.decode("utf-8").strip()

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

if __name__ == "__main__":
    run_tshark()
