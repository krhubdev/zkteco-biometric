from zk import ZK, const
import json
conn = None
zk = ZK('192.168.5.20', port=4370, timeout=5)
try:
    print('Connecting to device ...')
    conn = zk.connect()
    print('Disabling device ...')
    conn.disable_device()
    print('Firmware Version: : {}'.format(conn.get_firmware_version()))
    # print '--- Get User ---'
    users = conn.get_templates()
    print(users)
    for user in users:
       print(user.uid)
       print(json.dumps(user).encode())

    print ("Voice Test ...")
    conn.test_voice()
    print ('Enabling device ...')
    conn.enable_device()
except Exception as e:
    print ("Process terminate : {}".format(e))
finally:
    if conn:
        conn.disconnect()