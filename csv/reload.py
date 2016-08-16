import csv
import MySQLdb
import getpass
import traceback

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+LL_dictionary')
cursor = mydb.cursor()

test_csv_path = "reload_test.csv"
num_header_rows = 3
tbl_name = "reload_test"

create = "DROP TABLE IF EXISTS {0}; \
            CREATE TABLE {0} (".format(tbl_name)

csv_data = csv.reader(file(test_csv_path,'rU'))

col_data = zip(*csv_data[:num_header_rows])
for col in col_data:
    create += "{} {} COMMENT \'{}\',".format(*col)

create = create[:-1]+") CHARACTER SET ascii; "
#done with create table

for row in csv_data[num_header_rows:]:
    try:
        cursor.execute('INSERT INTO {}'.format(tbl_name)+"VALUES{}".format(row))
        mydb.commit()
    except Exception:
        mydb.rollback()
        traceback.print_exc()
        print("Error adding this row to database:\n"+" ".join(row))

cursor.close()
print "Done"
