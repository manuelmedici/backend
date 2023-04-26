import mysql.connector
from pathlib import Path
from datawrapper import Datawrapper
import pandas as pd

## AGGIORNA GRAFICO SPECIFICO SU DATAWRAPPER
def aggiornaGrafico(csv):
    dw = Datawrapper(access_token="PjtAbDR94YWCUvL3XWw3qNHVJpBi3KdVtwgqERvCZDtYyfhAkV9eby3nNAzHdtaC")
    df = pd.read_csv(csv
        # "https://raw.githubusercontent.com/chekos/datasets/master/data/datawrapper_example.csv",
        # sep=";",
        # "popolazione_regioni.csv"
    )
    dw.add_data(chart_id="wWa2f", data=df)
    dw.publish_chart(chart_id="wWa2f")

## STAMPA IL CONTENUTO DELLA TABELLA
def export_table(tb_name):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM " + tb_name)
    myresult = mycursor.fetchall()
    # for x in myresult:
    #     print(x)
    return myresult

## CONNESSIONE A DB
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database= "fujidata_database",
 )

## DEBUGGING
# print(export_table("popolazione_regioni"))

## INSERIMENTO SINGOLO RECOD CON COMMIT
# mycursor = mydb.cursor()
# sql = "INSERT INTO popolazione_regioni (Regione, Popolazione_residenti) VALUES (%s, %s)"
# val = ("Romaldia", 123435)
# mycursor.execute(sql, val)
# mydb.commit()

## RIMOZIONE DI UN SINGOLO RECORD CON COMMIT
# mycursor = mydb.cursor()
# sql = "DELETE FROM popolazione_regioni WHERE Regione = 'Romaldia'"
# mycursor.execute(sql)
# mydb.commit()

df = pd.DataFrame(export_table("popolazione_regioni"))
filepath = Path("popolazione_regioni.csv")
df.to_csv(filepath, index=False, header=False)
aggiornaGrafico(filepath)








# inserimento iniziale di tutta la tabella, il csv era laborioso...
# sql = "INSERT INTO popolazione_regioni (Regione, Popolazione_residenti) VAlUES(%s,%s)"
# val = [
#     ('Lombardia', 9943004),
#     ('Lazio', 5714882),
#     ('Campania', 5624420),
#     ('Veneto', 4847745),
#     ('Sicilia', 4833329),
#     ('Emilia-Romagna', 4425366),
#     ('Piemonte', 4256350),
#     ('Puglia', 3922941),
#     ('Toscana', 3663191),
#     ('Calabria', 1855454),
#     ('Sardegna', 1587413),
#     ('Liguria', 1509227),
#     ('Marche', 1487150),
#     ('Abruzzo', 1275950),
#     ('Friuli Venezia Giulia', 1194647),
#     ('Trentino-Alto Adige', 1073574),
#     ('Umbria', 858812),
#     ('Basilicata', 541168),
#     ('Molise', 292150),
#     ('Valle dAosta', 123360),
# ]
# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")

