import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Wcssm1229,",
  database="statestreet"
)

mycursor = mydb.cursor()

df = pd.read_sql('SELECT * FROM MKC', con=mydb)

print(df)