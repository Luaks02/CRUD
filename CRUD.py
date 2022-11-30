import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="batata",
    database="teste",
)
cursor = conexao.cursor()

# CRUD

# CREATE

nome = "placa_solar"
quantidade = 10

cursor.execute("INSERT INTO galpao (produtos_nome, produtos_qnt) VALUES (%s, %s)" , (nome, quantidade))
conexao.commit()

# READ

cursor.execute("SELECT * FROM galpao")
for resultado in cursor:
    print(resultado)



# UPDATE

nome = "placa_solar"

quantidade = 30

cursor.execute("UPDATE galpao SET produtos_qnt = %s WHERE produtos_nome = %s", (quantidade, nome) )

conexao.commit()



# DELETE

id = 5

cursor.execute("DELETE FROM galpao WHERE idgalpao = {id}")

conexao.commit()

cursor.close()
conexao.close()