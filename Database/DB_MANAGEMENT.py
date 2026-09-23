import sqlite3 as sql

conn = sql.connect("rooms.db")
c = conn.cursor()

c.executescript('''CREATE TABLE suite_rooms(
                 room_no INTEGER PRIMARY KEY,
                 floor_no TEXT,
                 availability BOOL);
                 
                 CREATE TABLE two_seater(
                 room_no INTEGER PRIMARY KEY,
                 floor_no TEXT,
                 availability BOOL);
                 
                 CREATE TABLE family_room(
                 room_no INTEGER PRIMARY KEY,
                 floor_no TEXT,
                 availability BOOL);
                 

''')


suite_rooms_l = [(401,"4th floor",True),(402,"4th floor",True),(403,"4th floor",True),(404,"4th floor",True),(405,"4th floor",True),
              (501,"5th floor",True),(502,"5th floor",True),(503,"5th floor",True),(504,"5th floor",True),(505,"5th floor",True)]

two_seater_l = [(301,"3rd floor",True),(302,"3rd floor",True),(303,"3rd floor",True),(304,"3rd floor",True),(305,"3rd floor",True),(306,"3rd floor",True),(307,"3rd floor",True),(308,"3rd floor",True),
              (201,"2nd floor",True),(202,"2nd floor",True),(203,"2nd floor",True),(204,"2nd floor",True),(205,"2nd floor",True),(206,"2nd floor",True),(207,"2nd floor",True),(208,"2nd floor",True)]

family_room_l = [(101,"1st floor",True),(102,"1st floor",True),(103,"1st floor",True),(104,"1st floor",True),(105,"1st floor",True)]


c.executemany("INSERT INTO suite_rooms VALUES(?,?,?)", suite_rooms_l)
c.executemany("INSERT INTO two_seater VALUES(?,?,?)", two_seater_l)
c.executemany("INSERT INTO family_room VALUES(?,?,?)", family_room_l)

c.execute("SELECT * FROM suite_rooms")
print(c.fetchall())
print(" ")
c.execute("SELECT * FROM two_seater")
print(c.fetchall())
print(" ")
c.execute("SELECT * FROM family_room")
print(c.fetchall())
print(" ")

conn.commit()
conn.close()