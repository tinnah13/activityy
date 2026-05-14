import xml.etree.ElementTree as ET
import re

tree = ET.parse("modified_sms_v2.xml")
root = tree.getroot()

received_regex = re.compile(r'You have received (\d+) RWF')
sent_regex = re.compile(r'Your payment of ([\d,]+) RWF')

total_received = 0
total_sent = 0

for sms in root.findall("sms"):
    body = sms.get("body")

    received = received_regex.search(body)
    if received:
        amount = int(received.group(1))
        total_received += amount
        print(f"Received: {amount} RWF")

    sent = sent_regex.search(body)
    if sent:
        amount = int(sent.group(1).replace(",", ""))
        total_sent += amount
        print(f"Sent: {amount} RWF")

print(f"\nTotal received: {total_received:,} RWF")
print(f"Total sent:     {total_sent:,} RWF")
