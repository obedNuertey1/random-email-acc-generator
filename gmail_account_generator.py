# This program shows the dictionary of email accounts

#This is a program that gives multiple google accounts with their account names and their passwords

import random
from datetime import datetime

def date_o_birth_gen(age):
    _month = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sept", "oct", "nov", "dec"]
    month_num = random.randint(1, len(_month))
    date_o_birth = {
        "day": random.randint(1, 28),
        "month": _month[month_num-1],
        "month_number": month_num,
        "year": int(datetime.today().year) - age
    }
    return date_o_birth