import csv
import MySQLdb
import getpass
import traceback

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+cloudmining')
cursor = mydb.cursor()

create = "source
create = create[:-1]+") CHARACTER SET utf8; "
print("Command sent to MySQL: "+create)
cursor.execute(create)
cursor.close()
#done with create table

cursor = mydb.cursor()
for row in csv_data:
    try:
        cursor.execute('INSERT INTO {}'.format(tbl_name)+" VALUES{}".format(tuple(row)))
        mydb.commit()
    except Exception:
        traceback.print_exc()
        print("Error adding this row to database:\n"+" ".join(row))

cursor.close()
print "Done"
