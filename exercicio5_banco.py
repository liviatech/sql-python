import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()
# Criar uma Tabela e Inserir Dados - Crie uma tabela chamada "clientes" com os campos:id(chave primária), nome(texto), idade(inteiro) e saldo(float). Insira alguns registros de clientes na tabela.
#cursor.execute(' CREATE TABLE clientes ( id INT PRIMARY KEY,  nome VARCHAR(100),  idade INT,   saldo REAL ); ')
cursor.execute(' INSERT INTO clientes(id, nome, idade, saldo ) VALUES (1, "Ana Silva", 30, 1500.00)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES  (2, "João Oliveira", 45, 2200.50)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (3, "Maria Santos", 28, 3200.75)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (4, "Carlos Souza", 35, 1800.40)')
cursor.execute('INSERT INTO clientes(id, nome, idade, saldo ) VALUES   (5, "Fernanda Lima", 40, 2500.00)')





conexao.commit()
conexao.close()