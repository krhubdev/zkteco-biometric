# https://github.com/fananimi/pyzk/blob/master/zk/base.py
# -*- coding: utf-8 -*-
import os
import sys

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

my_array = [
	{'9999': 'CASIÑO, KENT RUSSELL'},
]
 

from zk import ZK, const
import zk 
conn = None
zk = ZK('192.168.5.20', port=4370, verbose=True)
try:
    conn = zk.connect()

    for item in my_array:
        for key, value in item.items():
            print(f"{key}: {value}")
            conn.set_user(uid= (int(key)), name=value, privilege=const.USER_ADMIN, password='1234')

        print() 
   #
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()