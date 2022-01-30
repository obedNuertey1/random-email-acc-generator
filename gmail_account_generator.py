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
    c_t_2 = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','','','','','','','','','','']
    pass_word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','','','','','','','','','','','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    gen = ['male','female']
    gmail_ad_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '', '', '', '', '']

    res_arr = []