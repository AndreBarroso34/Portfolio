import sqlite3 #Importar o sql
from pathlib import Path #Import para buscar o caminho do ficheiro


#Instalar um programa para ser a tabela de base de dados 
#---------  dbeaver  ----------------------------------



#Diretorio para importar ficheiro
ROOT_DIR = Path(__file__).parent

#Nome da base de dados
DB_NAME = "db.sqlite3"

#Caminho do ficheiro
DB_FILE = ROOT_DIR / DB_NAME

#Nome da tabela
TABLE_NAME = "customers"

#Conectar à base de dados
con = sqlite3.connect(DB_FILE)

#Variavel que vai executar todas as operações na base de dados
cursor = con.cursor()

sql = f'SELECT * FROM {TABLE_NAME}'
cursor.execute(sql)
row = cursor.fetchone()
print(row)