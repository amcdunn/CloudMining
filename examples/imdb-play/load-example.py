import csv
import MySQLdb
import getpass
import traceback

mydb = MySQLdb.connect(host='sql.mit.edu',
    user='amcdunn',
    passwd=getpass.getpass("Password for sql.mit.edu:"),
    db='amcdunn+imdb_sample')
cursor = mydb.cursor()

test_csv_path = "../examples/imdb-play/sql/imdb.csv"
num_header_rows = 3
tbl_name = "reload_test"

create = "DROP TABLE IF EXISTS {0}; \
            CREATE TABLE {0} (".format(tbl_name)

csv_data = csv.reader(file(test_csv_path,'rU'))

header_rows = []
for counter, row in enumerate(csv_data):
    header_rows.append(row)
    if counter==num_header_rows-1:
        break
col_data = zip(*header_rows)
for col in col_data:
    create += "{} {} COMMENT \'{}\',".format(*col)

create = create[:-1]+") CHARACTER SET ascii; "
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
