"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

unique_ph_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        unique_ph_numbers.add(text[0])
        unique_ph_numbers.add(text[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        unique_ph_numbers.add(call[1])
    
    telemarketers = set()
    for call in calls:
        if call[0] in unique_ph_numbers:
            continue
        else:
            telemarketers.add(call[0])
        
    print("These numbers could be telemarketers: ")
    telemarketers_ordered = sorted(telemarketers)
    for ph in telemarketers_ordered:
      print(ph)
"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
