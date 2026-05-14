import xml.etree.ElementTree as ET
import re

tree = ET.parse('modified_sms_v2.xml')
root = tree.getroot()

total_received = 0
total_payment = 0
for sms in root:
    body = sms.get('body')
    if 'received' in body.lower():
        match = re.search(r'([\d,]+)\s*RWF', body)
        if match:
            amount = int(match.group(1).replace(',', ''))
            total_received += amount
    if 'payment' in body.lower():
        match = re.search(r'([\d,]+)\s*RWF', body)
        if match:
            amount = int(match.group(1).replace(',', ''))
            total_payment += amount
    elif 'transferred' in body.lower():
        match = re.search(r'([\d,]+)\s*RWF', body)
        if match:
            amount = int(match.group(1).replace(',', ''))
            total_payment += amount

print(f'Total amount received: {total_received}')
print(f'Total amount paid: {total_payment}')
