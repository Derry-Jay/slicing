import re
from pymysql import connect
# from pydantic import BaseModel
from truckpad.bottle.cors import CorsPlugin
#, enable_cors
from bottle import Bottle

#, request, response, post, get, put, delete, run
app = Bottle(__name__)
email_pattern = re.compile(r'^[a-z0-9]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
password_pattern = re.compile(
    r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
con = connect(host='localhost',
              user='root',
              password="", database='world_x')
cur = con.cursor()
# i = 1
# while i <= 10:
#     print(i)

# request.body.read().decode('utf8')  ast.
print("done")


def generateUpdateStatement(tableName, data):
    snt = '''update ''' + tableName + ''' set '''
    k = 0
    pk = ''
    for i in data.keys():
        if re.search('_id', i) is None:
            snt += (i + '''=%s''')
            if k < len(data.keys()) - 2:
                snt += ''', '''
            else:
                snt += ''' '''
            k += 1
        else:
            pk = re.search('_id', i).string
    snt += ('''where ''' + pk + '''=%s''')
    return snt


def generateCountStatement(tableName, data, primaryKey):
    cqs = '''select count(''' + primaryKey + ''') from ''' + \
          tableName + ''' where '''
    k = 0
    for i in data.keys():
        if re.search('_id', i) is None:
            cqs += (i + '''=%s''')
            if k < len(data.keys()) - 2:
                cqs += ''' and '''
            k += 1
    return cqs


def generateInsertStatement(tableName, data):
    inst = '''insert into ''' + tableName + '''('''
    k = 0
    for i in data.keys():
        inst += i
        if k < len(data.keys()) - 1:
            inst += ''', '''
        else:
            inst += ''') '''
        k += 1
    inst += '''values('''
    for i in range(len(data.keys())):
        inst += '''%s'''
        if i < len(data.keys()) - 1:
            inst += ''', '''
        else:
            inst += ''')'''
    return inst


def getListFromDict(data):
    g = []
    pk = ''
    for i in data.keys():
        if re.search('_id', i) is None:
            g.append(data[i])
        else:
            pk = re.search('_id', i).string
    if pk != '':
        g.append(data[pk])
    return g


# n=int(input("enter the no."))
# print(fact(n))

# a = compose(square, dec)
# print(a(10))

# a=int(input("enter the no."))
# b=cube(a)
# print(b)

# l = int(input('Enter Limit:'))
# i = 1
# while i <= 10:
#     print(i)
#             if (isArms(j)):
#                 print(j)


if __name__ == "__main__":
    app.install(CorsPlugin(
        origins=['http://localhost:8080/#/', 'http://localhost:8080/', 'http://localhost:8080']))
    app.run(host='127.0.0.1', port='8000', reloader=True)
