"""
Created on Dec 18, 2018

    @author: Vedha
"""
from pymysql import connect

con = connect(user='root', password='root', host='localhost', database='emp')
cur = con.cursor()
name = input('enter name')
emp_id = int(input('enter id'))
bp = float(input('enter basic pay'))
da = float(input('enter da'))
ta = float(input('enter ta'))
hra = float(input('enter hra'))
pf = float(input('enter pf'))
lic = float(input('enter lic'))
gp = bp + da + ta + hra
np = gp - (pf + lic)
print(np, "\n")
print(gp)
cur.execute("insert into empinfo values('%s','%d','%d','%d','%d','%d','%d','%d','%d','%d')" % (
    name, emp_id, bp, da, ta, hra, pf, lic, np, gp))
con.commit()
res = cur.execute("select * from empinfo")
print(cur.fetchall())
