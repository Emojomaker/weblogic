import os
import sys
import glob
sys.setdefaultencoding("utf8")
from com.ziclix.python.sql import zxJDBC
jdbc_url = "jdbc:oracle:thin:@******"
username = "******"
password = "******"
driver = "oracle.jdbc.xa.client.OracleXADataSource"
conn = zxJDBC.connect(jdbc_url, username, password, driver)
cursor = conn.cursor()
mod = os.listdir('/u01/scripts/install/release')
upload='/u01/Middleware/user_projects/domains/wl_domain/servers/AdminServer/upload/'
dir = '/u01/scripts/install/release'

#Функция получения файлов в папке

def files_on_dir(path):
    file_in_folder = []
    folders = os.listdir(path)
    for folder in folders:
        file_from_folder = os.path.splitext(folder)[0]
        file_in_folder.append(file_from_folder)
    return file_in_folder

for m in mod:
    pathdir= upload + m + '/' + 'app' + '/' + m
    releasedir = dir + '/' + m
    modules=os.path.splitext(m)[0]
    modul=modules.split('-')
    cursor.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY')) and module_name LIKE '%"+modul[0]+"%'")
    getinfo=cursor.fetchall()
    curtarget=""
    for r in getinfo:
        existingmod = r[0]
        modul1=existingmod.split('-')
        curtarget=r[1]
    if getinfo==[]:
        print ('Модуль'+' '+modules+' '+'не установлен, т.к. он является новым для ESB TC')
    else:
        old = modul1[-1].split('.')
        new = modul[-1].split('.')
        if len(old) == len(new):
            for i in range(0,len(new)):
                if int(old[i]) > int(new[i]):
                    break
                if int(old[i]) == int(new[i]):
                    continue
                if int(old[i]) < int(new[i]):
                    edit()
                    startEdit()
                    stopApplication(existingmod)
                    undeploy(existingmod)
                    deploy(appName=modules, path=pathdir, targets=curtarget)
                    save()
                    activate()
                    file = open('/u01/scripts/install/result.log','a')
                    file.write(modules+' -- '+curtarget+'\n')
                    file.close()
                    os.remove(releasedir)
                    break
        if len(old) < len(new):
            for i in range(0,len(old)):
                if int(old[i]) > int(new[i]):
                    break
                if int(old[-1]) == int(new[-2]):
                    edit()
                    startEdit()
                    stopApplication(existingmod)
                    undeploy(existingmod)
                    deploy(appName=modules, path=pathdir, targets=curtarget)
                    save()
                    activate()
                    file = open('/u01/scripts/install/result.log','a')
                    file.write(modules+' -- '+curtarget+'\n')
                    file.close()
                    os.remove(releasedir)
                    break
                if int(old[i]) < int(new[i]):
                    edit()
                    startEdit()
                    stopApplication(existingmod)
                    undeploy(existingmod)
                    deploy(appName=modules, path=pathdir, targets=curtarget)
                    save()
                    activite()
                    file = open('/u01/scripts/install/result.log','a')
                    file.write(modules+' -- '+curtarget+'\n')
                    file.close()
                    os.remove(releasedir)
                    break
        if len(old) > len(new):
            for i in range(0,len(new)):
                if int(old[i]) > int(new[i]):
                    break
                if int(old[-2]) == int(new[-1]):
                    break
                if int(old[i]) < int(new[i]):
                    edit()
                    startEdit()
                    stopApplication(existingmod)
                    undeploy(existingmod)
                    deploy(appName=modules, path=pathdir, targets=curtarget)
                    save()
                    activate()
                    file = open('/u01/scripts/install/result.log','a')
                    file.write(modules+' -- '+curtarget+'\n')
                    file.close()
                    os.remove(releasedir)
                    break

print('\n #########    UPDATING DATABASE     ######### \n ')
os.system("/u01/scripts/versioning/modules.sh")
print('\n #########  INSTALLATION COMPLETED  ######### \n ')
cursor.close()
conn.close()
exit()

 