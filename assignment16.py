 #$Q.1- Create a database. Create the following tables:
 #1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors
# Refer to the diagram below
#Ans-
import pymysql as py
db=py.connect("localhost",'root',"123","library")
book="create table book(book_id int,title char(20),loc char(20), gener char(20))"
titles="create table titles(title_id int ,title char(20),ISBN char(20),publisher_id int,publication_year int)"
publisher="create table publisher(publisher_id int ,name char(20), street_add  varchar(20),street_no int,zip_code_id int)"
zip_code="create table zip_code(zip_code_id int, city char(20),state char(20),zip_code int)"
auth_title="create table auth_title(auth_id int , auther_id int , title_id int) "
author ="create table author (author_id int ,First_name char(20), middle_name char(20),last_name char(20))"
cursor=db.cursor()
cursor.execute(book)
cursor.execute(titles)
cursor.execute(publisher)
cursor.execute(zip_code)
cursor.execute(auth_title)
cursor.execute(author)
print(cursor.execute("show tables"))
print(cursor.fetchall())
db.close()

# Q.2- Insert values in the tables.
# Ans-
import pymysql as py

db=py.connect("localhost","root","123","library")
cursor=db.cursor()
cursor.execute("insert into book values(001,'looking for sahil','india','fiction')")
cursor.execute("insert into titles values(001,'looking for sahil','1001',101,2005)")
cursor.execute("insert into publisher values(001,'ABC','usa',10002,11001)")
cursor.execute("insert into zip_code values(001,'ismailabad','haryana',136129)")
cursor.execute("insert into auth_title values(001,10010,1012012)")
cursor.execute("insert into author values(001,'john','null','green')")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()

#Q3. Update any values in any of the tables. Print the original and updated values.

import pymysql as py

db=py.connect("localhost","root","123","library")
cursor=db.cursor()
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
cursor.execute("update book set gener='romance' where book_id=001")
ursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()