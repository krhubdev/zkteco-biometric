from zk import ZK, const
import csv
from datetime import datetime

zk = ZK('192.168.1.208', port=4370, timeout=5, password=208)
conn = None

try:
    print('Connecting to device ...')
    conn = zk.connect()
    print('Disabling device ...')
    conn.disable_device()

    # Get and save users
    users = conn.get_users()
    with open('zk_users.csv', mode='w', newline='', encoding='utf-8') as user_file:
        user_writer = csv.DictWriter(user_file, fieldnames=['UID', 'Name', 'Privilege', 'Password', 'Group ID', 'User ID'])
        user_writer.writeheader()
        for user in users:
            privilege = 'Admin' if user.privilege == const.USER_ADMIN else 'User'
            user_writer.writerow({
                'UID': user.uid,
                'Name': user.name,
                'Privilege': privilege,
                'Password': user.password,
                'Group ID': user.group_id,
                'User ID': user.user_id
            })

    # Get and save attendance
    attendance = conn.get_attendance()
    with open('zk_attendance.csv', mode='w', newline='', encoding='utf-8') as att_file:
        att_writer = csv.DictWriter(att_file, fieldnames=['User ID', 'Timestamp', 'Status'])
        att_writer.writeheader()
        for att in attendance:
            att_writer.writerow({
                'User ID': att.user_id,
                'Timestamp': att.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'Status': att.status  # 0 = Check-In, 1 = Check-Out (device-dependent)
            })

    print('Voice Test ...')
    conn.test_voice()
    print('Enabling device ...')
    conn.enable_device()

    print('✅ Export completed: zk_users.csv and zk_attendance.csv')

except Exception as e:
    print(f'❌ Process terminated: {e}')

finally:
    if conn:
        conn.disconnect()
