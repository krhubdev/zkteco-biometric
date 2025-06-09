from zk import ZK, const
import csv

conn = None
zk = ZK('192.168.1.208', port=4370, timeout=5, password=208)

try:
    print('Connecting to device ...')
    conn = zk.connect()
    print('Disabling device ...')
    conn.disable_device()

    print('Firmware Version: {}'.format(conn.get_firmware_version()))

    users = conn.get_users()

    # Create and write to CSV
    with open('zk_users.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['UID', 'Name', 'Privilege', 'Password', 'Group ID', 'User ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for user in users:
            privilege = 'User'
            if user.privilege == const.USER_ADMIN:
                privilege = 'Admin'

            writer.writerow({
                'UID': user.uid,
                'Name': user.name,
                'Privilege': privilege,
                'Password': user.password,
                'Group ID': user.group_id,
                'User ID': user.user_id
            })

            print(f'- UID #{user.uid}')
            print(f'  Name       : {user.name}')
            print(f'  Privilege  : {privilege}')
            print(f'  Password   : {user.password}')
            print(f'  Group ID   : {user.group_id}')
            print(f'  User ID    : {user.user_id}')

    print('Voice Test ...')
    conn.test_voice()
    print('Enabling device ...')
    conn.enable_device()

except Exception as e:
    print("Process terminated: {}".format(e))

finally:
    if conn:
        conn.disconnect()
