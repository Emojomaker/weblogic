import cx_Oracle

import os

import time

import datetime

import re

 

clWL = '/u01/Middleware/user_projects/domains/wl_domain/servers/wl_server1/stage/'

clWS = '/u01/Middleware/user_projects/domains/wl_domain/servers/ws_server1/stage/'

clPAPI = '/u01/Middleware/user_projects/domains/wl_domain/servers/papi_server1/stage/'

clSO = '/u01/Middleware/user_projects/domains/wl_domain/servers/so_server1/stage/'

clMNP = '/u01/Middleware/user_projects/domains/wl_domain/servers/mnp_server1/stage/'

clOUI = '/u01/Middleware/user_projects/domains/wl_domain/servers/oui_server1/stage/'

con = cx_Oracle.connect('******', '*******', '*******')

cur=con.cursor()

 

for root,dirs, files in os.walk(clWL):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clWL + "/" + dir

            cluster1 = curD.split('/')

            dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                               break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                               cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                               break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

 

for root,dirs, files in os.walk(clWS):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clWS + dir

            cluster1 = curD.split('/')

           dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '%"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                           if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

 

for root,dirs, files in os.walk(clPAPI):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clPAPI + "/" + dir

            cluster1 = curD.split('/')

            dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '%"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

 

for root,dirs, files in os.walk(clSO):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clSO + "/" + dir

            cluster1 = curD.split('/')

            dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '%"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                               cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                               break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

 

for root,dirs, files in os.walk(clMNP):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clMNP + "/" + dir

            cluster1 = curD.split('/')

            dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '%"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                               cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

 

for root,dirs, files in os.walk(clOUI):

    result= ""

    resultcut= ""

    for dir in dirs:

        if '-' in dir and re.match('.*[1-9].*', dir):

            curD = clOUI + "/" + dir

            cluster1 = curD.split('/')

            dircut=dir.split('-')

            tempdate = (os.path.getmtime(curD))

            change=datetime.datetime.fromtimestamp(tempdate)

            changeone=change - datetime.timedelta(seconds = 1)

            datech = (change.strftime("%d.%m.%Y %H:%M:%S"))

            datechone = (changeone.strftime("%d.%m.%Y %H:%M:%S"))

            cur.execute("select * from weblogic_modules_int where date_end=(to_date('01.01.9999', 'DD.MM.YYYY'))and module_name LIKE '%"+dircut[0]+"%'")

            result = cur.fetchone()

            if 'server1' in cluster1[7]:

                temp=cluster1[7].split('_')

                cluster=temp[0] + '_cluster'

                if result == None:

                    cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                    con.commit()

                elif '-ear-' in dir:

                    resultcut=result[0].split('-ear-')

                    dircurrentcut=dir.split('-ear-')

                    old = resultcut[-1].split('.')

                    new = dircurrentcut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                else:

                    resultcut=result[0].split('-')

                    old = resultcut[-1].split('.')

                    new = dircut[-1].split('.')

                    if len(old) == len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[i]) == int(new[i]):

                                continue

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) < len(new):

                        for i in range(0,len(old)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-1]) == int(new[-2]):

                               cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

                    if len(old) > len(new):

                        for i in range(0,len(new)):

                            if int(old[i]) > int(new[i]):

                                break

                            if int(old[-2]) == int(new[-1]):

                                break

                            if int(old[i]) < int(new[i]):

                                cur.execute("update weblogic_modules_int set date_end=(to_date('"+ datechone +"','DD.MM.YYYY hh24:mi:ss')) where module_name='"+result[0]+"'")

                                con.commit()

                                cur.execute("insert into weblogic_modules_int values('"+dir+"','"+ cluster +"','weblogic',(to_date('"+ datech +"','DD.MM.YYYY hh24:mi:ss')),to_date('01.01.9999', 'DD.MM.YYYY'))")

                                con.commit()

                                break

cur.close()

con.close()