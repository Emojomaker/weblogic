import sys

import xml.etree.ElementTree as ET

config = ET.parse('/u01/Middleware/user_projects/domains/wl_domain/config/smbp.xml')

root = config.getroot()

 

#Функция смены адреса по тегу

def change_endpoint(tag, address):

    for string in root.iter(tag):

        string.set('endpoint', address)

    config.write('/u01/Middleware/user_projects/domains/wl_domain/config/smbp.xml')

    return print('succefull change EP for tag '+ tag)

 

#Подготовка массивов и словаря с данными из тестового файла

tags_in_file = []

endpoints_in_file = []

values_for_function = {}

with open('/u01/scripts/changer/values') as file_handler:

    for lines in file_handler:

        elements = lines.split(' ')

        for i in elements:

            if len(i) < 15:

                tags_in_file.append(i)

            else:

                endpoints_in_file.append(i)

 

#Заполнение словаря значениями из массивов

for x, y in zip(tags_in_file, endpoints_in_file):

    values_for_function[x] = y

 

#Изменение адресов в конфигурационном файле

for retult_tag, result_address in values_for_function.items():

    change_endpoint(retult_tag, result_address)

 

#Очистка файла с адресами для изменений

file = open('/u01/scripts/changer/values','w')

file.close()

