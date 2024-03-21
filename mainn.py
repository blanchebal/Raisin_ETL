#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
raisin_data = pd.read_excel('Raisin_Dataset.xlsx')
print(raisin_data.columns)

colonnes = ['area', 'major_axis_length', 'minor_axis_length', 'eccentricity','convex_area', 'extent', 'perimeter', 'class']
raisin_data.columns = colonnes 
print('----------------------------------------------------------------')
print(raisin_data.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='db_raisin',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in raisin_data.iterrows():
        sql = """INSERT INTO domaine (area,major_axis_length,minor_axis_length, eccentricity,convex_area,extent,perimeter,class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
