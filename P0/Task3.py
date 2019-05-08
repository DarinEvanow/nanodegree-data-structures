"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import bisect
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

def get_fixed_line_area_code(number):
    second_bracket_position = number.find(')')
    return number[1:second_bracket_position]


def get_mobile_phone_prefix(number):
    return number[0:4]


def get_telemarketer_area_code(number):
    return number[0:3]


def is_fixed_line(number):
    return number[0] == '('


def is_mobile_phone(number):
    return number.find(' ') > 0


def is_telemarketer(number):
    return number[0:3] == '140'


def is_bangalore(number):
    return number[0:5] == '(080)'


all_called_area_codes = set()
total_number_of_calls_from_bangalore = 0
total_number_of_calls_to_bangalore_from_bangalore = 0
for call in calls:
    if is_bangalore(call[0]):
        total_number_of_calls_from_bangalore += 1
        if is_fixed_line(call[0]):
            if is_fixed_line(call[1]):
                all_called_area_codes.add(get_fixed_line_area_code(call[1]))

            if is_mobile_phone(call[1]):
                all_called_area_codes.add(get_mobile_phone_prefix(call[1]))

            if is_telemarketer(call[1]):
                all_called_area_codes.add(get_telemarketer_area_code(call[1]))

        if is_bangalore(call[1]):
            total_number_of_calls_to_bangalore_from_bangalore += 1



print('The numbers called by people in Bangalore have codes:')
for area_code in sorted(all_called_area_codes):
    print(area_code)

percentage = '{:.2%}'.format(total_number_of_calls_to_bangalore_from_bangalore / total_number_of_calls_from_bangalore)

print(f'{percentage} of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')


