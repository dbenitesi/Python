import pyshark
import smtplib

filter_list = [
    "tcp.dstport == 80",
    "ip.src == 192.168.1.1",
    "tcp.flags.push == 1"
    "tcp.flags.reset == 1 and tcp.flags.ack == 1"
]

capture = pyshark.LiveCapture(interface='eth0')

sender_email = "dbenitesi.db@gmail.com"
receiver_email = "dbenitesi.db@gmail.com"
password = "aspoyxnanyzmraoo"

def send_email(subject, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, password)
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

for packet in capture.sniff_continuously():
    for filter in filter_list:
        if eval(filter):
            send_email("Filter matched!", str(packet))
            print("Filter matched:", filter)
            print("Packet:", packet)
