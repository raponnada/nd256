"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

def getAreaCode(phone_number):
    if phone_number.startswith('('):
      area_code = phone_number.split(')')[0].strip('(')
    elif phone_number.startswith('140'):
      area_code = '140'
    else:
      area_code = phone_number[:4]
    return area_code

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

    area_codes_set = set()
    total_fixed_calls = 0
    total_calls_recieved = 0
    
    for call in calls:
      if call[0].startswith('(080)'):
        area_code = getAreaCode(call[1])
        area_codes_set.add(area_code)
        total_fixed_calls += 1
        if area_code == '080':
          total_calls_recieved += 1

    # part A
    print("The numbers called by people in Bangalore have codes:")
    area_codes_ordered = sorted(area_codes_set)
    for area_code in area_codes_ordered:
      print(area_code)
    
    # part B
    fixed_call_percent = round((total_calls_recieved/total_fixed_calls) * 100,2)
    print(f"{fixed_call_percent} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")
    

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""