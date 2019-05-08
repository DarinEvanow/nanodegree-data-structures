"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
time_spent_on_phone_by_number = {}

for call in calls:
    if call[0] not in time_spent_on_phone_by_number:
        time_spent_on_phone_by_number[call[0]] = int(call[3])
    else:
        time_spent_on_phone_by_number[call[0]] += int(call[3])

    if call[1] not in time_spent_on_phone_by_number:
        time_spent_on_phone_by_number[call[1]] = int(call[3])
    else:
        time_spent_on_phone_by_number[call[1]] += int(call[3])

number_with_longest_call_time = max(time_spent_on_phone_by_number, key=time_spent_on_phone_by_number.get)
longest_call_time = max(time_spent_on_phone_by_number.values())

print(f'{number_with_longest_call_time} spent the longest time, {longest_call_time}, on the phone during September 2016.')