import csv
import MySQLdb
import getpass
import traceback

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+LL_dictionary')
cursor = mydb.cursor()

csv_data = csv.reader(file(raw_input("Enter path of csv file:"),'rU'),dialect=csv.excel_tab)
for row in csv_data:
    try:
        cursor.execute('INSERT INTO `TABLE 2`' \
              'VALUES("%s", "%s")', 
              row)
        print("got through execute command for a row")
        mydb.commit()
    except Exception:
        mydb.rollback()
        traceback.print_exc()
        print("Error adding this row to database:\n"+" ".join(row))

cursor.close()
print "Done"
