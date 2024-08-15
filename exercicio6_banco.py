import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# # #cursor.execute(' CREATE TABLE clientes ( id INT PRIMARY KEY,  nome VARCHAR(100),  idade INT,   saldo REAL ); ')
# # cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo ) VALUES (1, "Ana Silva", 30, 1500.00)')
# # cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES  (2, "João Oliveira", 45, 2200.50)')
# # cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (3, "Maria Santos", 28, 3200.75)')
# # cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (4, "Carlos Souza", 35, 1800.40)')
# # cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (5, "Fernanda Lima", 40, 2500.00)')

# # Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:
# # a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
visualizar = cursor.execute('SELECT nome, idade  FROM  clientes WHERE idade > 30') 
for  clientes in visualizar: 
     print (clientes)
# # b) Calcule o saldo médio dos clientes.
visualizar = cursor.execute('SELECT AVG(saldo) FROM clientes ') 
saldo_medio = cursor.fetchone()[0]
print(f'Saldo médio dos clientes: {saldo_medio:.2f}')

# # c) Encontre o cliente com o saldo máximo.
visualizar = cursor.execute('SELECT * FROM  clientes ORDER BY saldo DESC') 
for  clientes in visualizar: 
    print (clientes)

# d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo >= 1600.00')
for clientes in dados:
      print(clientes)




conexao.commit()
conexao.close()