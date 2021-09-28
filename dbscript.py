import sqlite3
from sqlite3 import Error


def create_db(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("DROP TABLE IF EXISTS MOVIES")

        # Creating table
        table = """ CREATE TABLE MOVIES (
                    Movie_Name VARCHAR(255) NOT NULL,
                    Actor_Name CHAR(25) NOT NULL,
                    Actress_Name CHAR(25),
                    Director CHAR(25) NOT NULL,
                    Year_Of_Release INT
                ); """

        conn.execute(table)
        print("Created table")
        sql = ''' INSERT INTO MOVIES(Movie_Name,Actor_Name,Actress_Name,Director,Year_Of_Release)
              VALUES('JILLA','VIJAY','NIVETHA','MANIRATNA',2004) '''
        cur = conn.cursor()
        cur.execute(sql)
        sql = ''' INSERT INTO MOVIES(Movie_Name,Actor_Name,Actress_Name,Director,Year_Of_Release)
              VALUES('YODHA','MOHANLAL','HANSIKA','PRIYADARSAN',1997) '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

        print("Inserted values to MOVIES table")
        #getting all data in the table
        print("printing all data from MOVIE table")
        cur.execute("SELECT * FROM MOVIES")
        rows = cur.fetchall()

        for row in rows:
            print(row)
        cur.execute("SELECT * FROM MOVIES WHERE Actor_Name = 'VIJAY' ")
        rows = cur.fetchall()
        print("printing the specified data using actor_name")
        for row in rows:
            print(row)

        # Close the coonection
        conn.close()
    except Error as e:
        print(e)

create_db(r"D:\Work\pythonsqlite.db")
