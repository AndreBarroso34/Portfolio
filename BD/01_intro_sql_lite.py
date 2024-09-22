import sqlite3  # Importar o sql
from pathlib import Path  # Import para buscar o caminho do ficheiro

# Diretório para importar ficheiro
ROOT_DIR = Path(__file__).parent

# Nome da base de dados
DB_NAME = "db.sqlite3"

# Caminho do ficheiro
DB_FILE = ROOT_DIR / DB_NAME

# Nome da tabela
TABLE_NAME = "customers"

# Conectar à base de dados
con = sqlite3.connect(DB_FILE)

# Variável que vai executar todas as operações na base de dados
cursor = con.cursor()

# Criar uma tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} '
    '('
        'id INTEGER PRIMARY KEY AUTOINCREMENT, '
        'name TEXT, '
        'weigth REAL'
    ')'
)

# Executar o comando na Base de Dados
con.commit()

# Inserir dados na tabela(db.sqlite3)
sql = f'INSERT INTO {TABLE_NAME} (name, weigth) VALUES (?, ?)'  # Correção do número de placeholders
cursor.execute(sql, ('Carlos', 23))
con.commit()

# Inserir registro utilizando dicionário
sql = f'INSERT INTO {TABLE_NAME} (name, weigth) VALUES (:nome, :peso)'
cursor.execute(sql, {'nome': 'Joana silvaa', 'peso': 63.2})
cursor.executemany(sql, ({'nome': 'Joana Mendes', 'peso': 100.2}, {'nome': 'Rui Moura', 'peso': 93.4}))
con.commit()

print("Inserções realizadas com sucesso.")

# Eliminar um registro
sql = f'DELETE FROM {TABLE_NAME} WHERE id = ?'
cursor.execute(sql, (5,))  # Corrigido para passar uma tupla
con.commit()

# Atualizar os dados de um registro
sql = f'UPDATE {TABLE_NAME} SET name = ?, weigth = ? WHERE id = ?'
cursor.execute(sql, ("Marcelo", 88, 3))  # Correção na passagem dos parâmetros como tupla
con.commit()

# Inserir mais de um registro simultaneamente
sql = f'INSERT INTO {TABLE_NAME} (name, weigth) VALUES (?, ?)'
cursor.executemany(sql, [('Mauro', 18), ('Paula', 47), ('Alice', 29)])
con.commit()

# Selecionar dados da tabela
sql2 = f'SELECT * FROM {TABLE_NAME} WHERE id BETWEEN ? AND ?'
data = cursor.execute(sql2, (3, 5))  # Correção no tipo dos valores (inteiros, não strings)
for row in data:
    print(row)

# Fechar conexão
cursor.close()
con.close()
