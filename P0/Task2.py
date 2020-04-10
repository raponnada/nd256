"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # default dictionary to keep duration of each phone in #seconds 
    longest_duration = defaultdict(int)
    # update max_duration if a new longest duration is found. 
    max_duration = 0
    max_ph = None
    for call in calls:
        call_time = int(call[3])
        longest_duration[call[0]] += call_time
        longest_duration[call[1]] += call_time
        if max_duration < longest_duration.get(call[0]):
            max_duration = longest_duration.get(call[0])
            max_ph = call[0]
        if max_duration < longest_duration.get(call[1]):
            max_duration = longest_duration.get(call[1])
            max_ph = call[1] 
        
    print(f"{max_ph} spent the longest time, {max_duration} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""