import psycopg2
import config

#establishing the connection
conn = psycopg2.connect(
   database="config.database", user='config.username', password='config.password', host='config.host', port= 'config.port'
)

#Setting auto commit false
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Retrieving data
query='''SELECT id, electricity_currently_delivered, electricity_currently_returned  FROM public.dsmr_datalogger_dsmrreading
ORDER BY id DESC LIMIT 1'''
cursor.execute(query)

#Fetching 1st row from the table
result = cursor.fetchone();
print(result)

#Fetching 1st row from the table
result = cursor.fetchall();
print(result)

#Commit your changes in the database
conn.commit()

#Closing the connection
conn.close()