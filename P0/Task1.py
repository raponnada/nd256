"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
telephone_numbers = set()


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        tele_ph1 = text[0].replace(' ','').replace('(','').replace(')','')
        tele_ph2 = text[1].replace(' ','').replace('(','').replace(')','')
        telephone_numbers.add(tele_ph1)
        telephone_numbers.add(tele_ph2)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        tele_ph1 = call[0].replace(' ','').replace('(','').replace(')','')
        tele_ph2 = call[2].replace(' ','').replace('(','').replace(')','')
        telephone_numbers.add(tele_ph1)
        telephone_numbers.add(tele_ph2)


print(f"There are {len(telephone_numbers)} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""