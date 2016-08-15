import csv
import MySQLdb
import getpass

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+LL_dictionary')
cursor = mydb.cursor()
cursor.execute("SELECT * FROM dummy_dictionary")
print(cursor.fetchall())
csv_file = raw_input("Enter path of csv file:")
sql = """LOAD DATA LOCAL INFILE '{}' \
      INTO TABLE dummy_dictionary \
      FIELDS TERMINATED BY ',' \
      OPTIONALLY ENCLOSED BY '"'  \
      LINES TERMINATED BY '\r\n' \
      IGNORE 0 LINES;;"""
try:
    print(sql.format(csv_file))
    cursor.execute(sql.format(csv_file))
    mydb.commit()
except Exception:
    mydb.rollback()
    print("Error adding lines to database")
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"
