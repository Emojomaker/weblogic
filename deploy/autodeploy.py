#coding: utf-8
import zipfile
import cx_Oracle
import paramiko
import os
import sys
import glob
import subprocess
import wget
import shutil
 
#Функция получения файлов в папке

def files_on_dir(path):

    file_in_folder = []

    folders = os.listdir(path)

    for folder in folders:

        file_from_folder = os.path.splitext(folder)[0]

        file_in_folder.append(file_from_folder)

    return file_in_folder

#Открываем файлы для удаления и добавления данных
log = open('/u01/scripts/install/log','w')
log.close()
file = open('/u01/scripts/install/result.log','w')
file.write('Установлены следующие модули:\n'+'\n')
file.close
 
#Определяем каталоги, с которыми работает скрипт
upload='/u01/Middleware/user_projects/domains/wl_domain/servers/AdminServer/upload/'
mod = os.listdir('/u01/scripts/install/release')
release = '/u01/scripts/install/release'

 #Скачиваем файл по ссылке, распаковываем в папку для установки
url = sys.argv[1]
wget.download(url, '/u01/scripts/install/release/release_pack.zip')
pack = os.listdir('/u01/scripts/install/release')
fantasy_zip = zipfile.ZipFile('/u01/scripts/install/release/release_pack.zip')
fantasy_zip.extractall('/u01/scripts/install/release')
fantasy_zip.close()
os.chdir('/u01/scripts/install/release/')

for file in pack:
    if file.endswith('.zip'):
        os.remove(file)
        print ('\n ##############Архив удален##############')

#Создаём коннет до базы TAF
con = cx_Oracle.connect('', '', '')
cur=con.cursor()

#Задаём каталоги, с которыми будем работать
mod = os.listdir('/u01/scripts/install/release')
dir = '/u01/scripts/install/release'

 #Цикл проверки модулей на существование

for m in mod:
    releasedir = dir + '/' + m
    modules=os.path.splitext(m)[0]
    modul=modules.split('-')
    cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY')) and module_name LIKE '%"+modul[0]+"%'")
    getinfo=cur.fetchone()

 #Проверка условий и установка
    if getinfo==[]:
        print ('Модуль'+' '+modules+' '+'не установлен, т.к. он является новым для ESB TC')
    elif getinfo[2] == 'weblogic':

        #Создаём deployplan в каталоге upload

        dir = ''
        for m in mod:
            pathdir= upload + dir +  m + '/' + 'app'
            modules=os.path.splitext(m)[0]
            modul=modules.split('-')
            src = release + '/' + m
            dst = pathdir + '/' + m
            if not os.path.isdir(pathdir):
                os.makedirs(pathdir)
                shutil.copy(src, dst)
        os.system('sudo -u siebel sh /u01/scripts/install/wlst.sh')
 
        #Условие, если модуль должен быть установлен на *******
    else:
        os.system ('scp'+' '+releasedir+' '+'******@******:/u01/scripts/install/release')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
                ssh.connect('******', username='******', password='*******')
        except paramiko.SSHException:
                print "Не удалось подключиться к хосту"
                quit()
        stdin,stdout,stderr = ssh.exec_command("sh /u01/scripts/install/autodeploy.sh")
        list = stdout.readlines()
        output = [line.rstrip() for line in list]
        log = open('/u01/scripts/install/log', 'a')
        log.write('\n'.join(output))
        log.close()
        ssh.close()
        curtarget = getinfo[1]
        file = open('/u01/scripts/install/result.log','a')
        file.write(modules+' -- '+curtarget+'\n')
        file.close
        os.remove(releasedir)


#Функция записи информации в результирующий лог
if files_on_dir('/u01/scripts/install/release') == []:
    file = open('/u01/scripts/install/result.log','a')
    file.write('\n'+'Все модули установлены'+'\n')
    file.close()
else:
    file = open('/u01/scripts/install/result.log','a')
    file.write('___________________________'+'\n')
    file.write('Не установленны модули:'+'\n')
    for module_name in files_on_dir('/u01/scripts/install/release'):
        file.write(module_name +'\n')
    file.close()

сur.close()

con.close()