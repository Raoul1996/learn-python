# backup script
import os
import time

source = ['/Users/zhoubao/workplace/python/zip']

target_dir = '/Users/zhoubao/workplace/python/backup'
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'
if not os.path.exists(today):
    os.mkdir(today)

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
