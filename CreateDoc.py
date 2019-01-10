import psycopg2
import PGSPARAMS as CREDS
import sys,os
import numpy as np
import pandas as pd

foo = 100


def conn_pgsdb():

     try:

         connection = psycopg2.connect(user=CREDS.PGUSER,
                                       password=CREDS.PGPASSWORD,
                                       host=CREDS.PGHOST,
                                       port=CREDS.PGPORT,
                                       database=CREDS.PGDATABASE)
         cursor = connection.cursor()
        ## print(connection.get_dsn_parameters(), "\n")
         return connection , cursor
     except (Exception, psycopg2.Error) as error:
         print("Error while connecting to PostgreSQL", error)

def  writeblob_rec( doc_id, path_to_file, file_extension):
    try:
     drawing = open(path_to_file, 'rb').read()
     postgres_insert_query = """ INSERT INTO etl_pdf(srcname,srcdoc)  VALUES (%s,%s)"""

     con, cur = conn_pgsdb()
     print(con.get_dsn_parameters(), "\n")
     print(doc_id, path_to_file, file_extension)
     cur.execute("INSERT INTO etl_pdf(srcname,srcdoc) " +
                 "VALUES(%s,%s)",
                 (doc_id, psycopg2.Binary(drawing)))
     # commit the changes to the database
     con.commit()
     # close the communication with the PostgresQL database
     cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
     print(error)
    finally:
        if con is not None:
            con.close()

if __name__ == "__main__":
 print("Executing as main program")
 print("Value of __name__ is: ", __name__)
 ##writeblob_rec( 'First','c:\Ramana_Python\data\sample.pdf','pdf')
 writeblob_rec( 'First','c:\Ramana_Python\data\BankofAmerica_10Q.pdf','pdf')
 writeblob_rec( 'First','c:\Ramana_Python\data\google_10Q.pdf','pdf')
 writeblob_rec( 'First','c:\Ramana_Python\data\microsoft_10k.pdf','pdf')

