import csv
import MySQLdb
import getpass

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+LL_dictionary')
cursor = mydb.cursor()

csv_data = csv.reader(file(raw_input("Enter path of csv file:")))
for row in csv_data:
    try:
        cursor.execute('INSERT INTO testcsv(names, \
              classes, mark )' \
              'VALUES("%s", "%s", "%s")', 
              row)
        mydb.commit()
    except Exception:
        mydb.rollback()
        print("Error adding this row to database:\n".join(row))

cursor.close()
print "Done"
