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

def acc_generator():
    a_t_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','','','','','','','','','','']
    a_t_2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    v_t_1 = ['A','E','I','O','U']
    v_t_2 = ['a','e','i','o','u']
    c_t_1 = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']